####################################################
#!/usr/bin/env python3
####################################################
import sys
####################################################
sys.path.append('../../../07')
sys.path.append('./../../../../mypylib')
####################################################
from dictwords import *
from mypylib_cls import *
from assign05_02 import *
####################################################
"""
HX-2023-03-24: 10 points
Solving the doublet puzzle
"""
####################################################
"""
Please revisit assign06_04.py.
######
Given a word w1 and another word w2, w1 and w2 are a
1-step doublet if w1 and w2 differ at exactly one position.
For instance, 'water' and 'later' are a 1-step doublet.
The doublet relation is the reflexive and transitive closure
of the 1-step doublet relation. In other words, w1 and w2 are
a doublet if w1 and w2 are the first and last of a sequence of
words where every two consecutive words form a 1-step doublet.
<Here is a little website where you can use to check if two words
for a doublet or not:
http://ats-lang.github.io/EXAMPLE/BUCS320/Doublets/Doublets.html
######
"""
####################################################
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
            
            
            
def helper(x):
    return foreach_to_filter_fnlist(fnlist_foreach)(word_neighbors(x), lambda word: word_is_legal(word))

def doublet_bfs_test(w1, w2):
    """
    Given two words w1 and w2, this function should
    return None if w1 and w2 do not for a doublet. Otherwise
    it returns a path connecting w1 and w2 that attests to the
    two words forming a doublet.
    """
    temp = stream_make_filter(gpath_bfs([w1], helper), lambda path: path[-1] == w2)()
    if temp.get_ctag() == 0:
        return None
    else:
        return temp.get_cons1()
    
####################################################
