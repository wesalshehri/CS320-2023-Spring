####################################################
#!/usr/bin/env python3
####################################################
import sys
sys.path.append('./../../../../mypylib')
from mypylib_cls import *
import queue
import nltk
nltk.download('words')
from nltk.corpus import words
################################################
setofwords = set(words.words())
################################################
def word_is_legal(word):
    return word in setofwords

####################################################
"""
HX-2023-03-24: 30 points
Solving the doublet puzzle
"""
####################################################
# assign05_02

def string_length(word):
    return len(word)

def strsub(word, i):
    return word[i]


def AB():
    return "abcdefghijklmnopqrstuvwxyz"

def string_implode(s):
    return fnlist_foldleft(s, "", lambda acc, x: acc + x)


def fnlist_tabulate(n, fopr):
    if n <= 0:
        return fnlist_nil()
    else:
        return fnlist_cons(fopr(0), fnlist_tabulate(n - 1, lambda i: fopr(i + 1)))

def string_tabulate(l, fopr):
   return string_implode(fnlist_tabulate(l, fopr))


def word_neighbors(word):
    """                                                                                                                                                       
    Note that this function should returns a fnlist                                                                                                           
    (not a pylist)                                                                                                                                            
    Your implementation should be combinator-based very                                                                                                       
    much like the posted solution.                                                                                                                            
    """
    wlen = string_length(word)
    return \
        fnlist_concat(string_imap_fnlist\
                      (word, lambda i, c: fnlist_concat\
                       (string_imap_fnlist(AB(), lambda _, c1: fnlist_sing\
                                           (string_tabulate(wlen, lambda j: strsub(word, j) if i != j else c1)) if (c != c1) else fnlist_nil()))))
            

def word_neighbors_legal(word):
    return fnlist_filter_pylist(word_neighbors(word), word_is_legal)

def wpath_neighbors_legal(wpath):
    word1 = wpath[-1]
    words = word_neighbors_legal(word1)
    return [wpath + (word2,) for word2 in words]

def gtree_bfs(nxs, fchildren):
    def helper(nxs):
        if nxs.empty():
            return strcon_nil()
        else:
            nx1 = nxs.get()
            for nx2 in fchildren(nx1):
                nxs.put(nx2)
            return strcon_cons(nx1, gtree_bfs(nxs, fchildren))
    return lambda: helper(nxs)

def doublet_stream_from(word):
    nxs = queue.Queue() 
    nxs.put((word,))
    return gtree_bfs(nxs, wpath_neighbors_legal)


####################################################
