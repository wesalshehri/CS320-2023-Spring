####################################################
#!/usr/bin/env python3
####################################################
import sys
sys.path.append('./../../../05')
sys.path.append('./../../../../mypylib')
from mypylib_cls import *
####################################################
"""
HX-2023-03-14: 30 points
BU CAS CS320-2023-Spring: Image Processing
"""
####################################################
import math
####################################################
import kervec
import imgvec
####################################################
from PIL import Image
####################################################

def load_color_image(filename):
    """
    Loads a color image from the given file and returns a dictionary
    representing that image.

    Invoked as, for example:
       i = load_color_image("test_images/cat.png")
    """
    with open(filename, "rb") as img_handle:
        img = Image.open(img_handle)
        img = img.convert("RGB")  # in case we were given a greyscale image
        img_data = img.getdata()
        pixels = list(img_data)
        width, height = img.size
        return imgvec.image(height, width, pixels)
    # return None

def save_color_image(image, filename, mode="PNG"):
    """
    Saves the given color image to disk or to a file-like object.  If filename
    is given as a string, the file type will be inferred from the given name.
    If filename is given as a file-like object, the file type will be
    determined by the "mode" parameter.
    """
    out = Image.new(mode="RGB", size=(image.width, image.height))
    out.putdata(image.pixlst)
    if isinstance(filename, str):
        out.save(filename)
    else:
        out.save(filename, mode)
    out.close()
    # return None

####################################################
def grey_of_color(clr):
    (rr, gg, bb) = clr
    return round(0.299*rr+0.587*gg+0.114*bb)
####################################################

def image_invert_grey(ximg):
    return imgvec.image_make_map(ximg, lambda pix: 255 - pix)
def image_invert_color(ximg):
    return imgvec.image_make_map(ximg, lambda clr: 255 - grey_of_color(clr))

####################################################
#
# towers = \
#     load_color_image("INPUT/towers.jpg")
# balloons = \
#     load_color_image("INPUT/balloons-real.png")
# balloons_090l = imgvec.image_trans_090l(balloons)
# balloons_090r = imgvec.image_trans_090r(balloons)
#
####################################################
#
# save_color_image(image_invert_color(towers), "OUTPUT/towers_invert.png")
# save_color_image(image_invert_color(balloons), "OUTPUT/balloons_invert.png")
#
####################################################

def image_edges_grey(image):
    """
    This is an implementation of the Sobel operator.
    """
    krow = \
        kervec.kernel_make_pylist\
        (3, [-1, -2, -1, 0, 0, 0, 1, 2, 1])
    kcol = \
        kervec.kernel_make_pylist\
        (3, [-1, 0, 1, -2, 0, 2, -1, 0, 1])
    imgrow = \
        imgvec.image_kernel_correlate(image, krow, 'extend')
    imgcol = \
        imgvec.image_kernel_correlate(image, kcol, 'extend')
    imgres = \
        imgvec.image_make_z2map\
        (imgrow, imgcol, lambda x, y: math.sqrt(x*x + y*y))
    return imgvec.image_round_and_clip(imgres)

def image_edges_color(image):
    return image_edges_grey\
        (imgvec.image_make_map(image, lambda clr: grey_of_color(clr)))

####################################################

def image_blur_bbehav_grey(image, ksize, bbehav):
    ksize2 = ksize*ksize
    kernel = \
        kervec.kernel_make_pylist\
        (ksize, ksize2*[1.0/ksize2])
    return imgvec.image_round_and_clip\
        (imgvec.image_kernel_correlate(image, kernel, bbehav))

####################################################

def color_filter_from_greyscale_filter(filt):
    """
    Given a filter that takes a greyscale image as input and produces a
    greyscale image as output, returns a function that takes a color image as
    input and produces the filtered color image.
    """
    def image_filter(cimage):
        ww = cimage.width
        hh = cimage.height
        image0 = filt(imgvec.image_make_map(cimage, lambda clr: clr[0]))
        image1 = filt(imgvec.image_make_map(cimage, lambda clr: clr[1]))
        image2 = filt(imgvec.image_make_map(cimage, lambda clr: clr[2]))
        return imgvec.image_make_tuple\
            (hh, ww, \
             tuple(zip(image0.pixlst, image1.pixlst, image2.pixlst)))
    return lambda cimage: image_filter(cimage)

####################################################

def image_blur_bbehav_color(image, ksize, bbehav):
    return \
        color_filter_from_greyscale_filter\
        (lambda image: image_blur_bbehav_grey(image, ksize, bbehav))(image)

####################################################
# save_color_image\
#    (image_blur_bbehav_color(balloons, 5, 'extend'), "OUTPUT/balloons_blurred.png")
####################################################

def image_seam_carving_color(image, ncol):
    """
    Starting from the given image, use the seam carving technique to remove
    ncol (an integer) columns from the image. Returns a new image.
    """
    assert ncol < image.width
    imgres = image
    for i0 in range(ncol):
        print("image_seam_carving_color: i0 =", i0)
        imgres = image_seam_carving_1col_color(imgres)
    return imgres # return of image_seam_carving_color

####################################################

def image_seam_carving_1col_color(image):
    """
    Starting from the given image, use the seam carving technique to remove
    one seam from the image. Returns a new image with one seam being removed.
    """
    ww = image.width
    hh = image.height
    energy = image_edges_color(image)
    ################################################
    def cenergy(i0, j0):
        evalue = imgvec.image_get_pixel(energy, i0, j0)
        if i0 <= 0:
            return evalue
        else:
            if j0 <= 0:
                return evalue + min(cenergy(i0-1, j0), cenergy(i0-1, j0+1))
            elif j0 >= ww-1:
                return evalue + min(cenergy(i0-1, j0-1), cenergy(i0-1, j0))
            else:
                return evalue + min(cenergy(i0-1, j0-1), cenergy(i0-1, j0), cenergy(i0-1, j0+1))
    ################################################
    jmin0 = 0
    cmin0 = cenergy(hh-1, 0)
    for j0 in range(1, ww):
        if cenergy(hh-1, j0) < cmin0:
            jmin0 = j0
            cmin0 = cenergy(hh-1, j0)
    ################################################
    def jminall(i0):
        if i0 >= hh-1:
            return jmin0
        else:
            jmin1 = jminall(i0+1)
            if jmin1 <= 0:
                cmin1 = min(cenergy(i0, jmin1), cenergy(i0, jmin1+1))
            elif jmin1 >= ww-1:
                cmin1 = min(cenergy(i0, jmin1-1), cenergy(i0, jmin1))
            else:
                cmin1 = min(cenergy(i0, jmin1-1), cenergy(i0, jmin1), cenergy(i0, jmin1+1))                
            if jmin1 <= 0:
                if cenergy(i0, jmin1) <= cmin1:
                    return jmin1
                else:
                    return jmin1 + 1
            elif jmin1 >= ww-1:
                if cenergy(i0, jmin1-1) <= cmin1:
                    return jmin1 - 1
                else:
                    return jmin1
            else:
                if cenergy(i0, jmin1-1) <= cmin1:
                    return jmin1 - 1
                elif cenergy(i0, jmin1) <= cmin1:
                    return jmin1
                else:
                    return jmin1 + 1
    ################################################
    return \
        imgvec.image_make_pylist\
        (hh, ww-1, imgvec.image_i2filter_pylist(image, lambda i0, j0, _: jminall(i0) != j0))

####################################################
# save_color_image(imgvec.image_trans_090l(balloons), "OUTPUT/balloons_090l.png")
# save_color_image(imgvec.image_trans_090r(balloons), "OUTPUT/balloons_090r.png")
####################################################
# save_color_image(image_seam_carving_color(balloons,100), "OUTPUT/balloons_seam_carving_100.png")
####################################################
# save_color_image(image_seam_carving_color(balloons,200), "OUTPUT/balloons_seam_carving_200.png")
# save_color_image(image_seam_carving_color(balloons,250), "OUTPUT/balloons_seam_carving_250.png")
# save_color_image(image_seam_carving_color(balloons_090l, 50), "OUTPUT/balloons_090l_seam_carving_50.png")
# save_color_image(image_seam_carving_color(balloons_090r, 50), "OUTPUT/balloons_090r_seam_carving_50.png")
####################################################
