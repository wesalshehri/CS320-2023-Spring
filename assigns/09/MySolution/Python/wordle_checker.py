########################
# HX-2023-04-15: 10 points
########################
"""
Given two words w1 and w2 of the same length,
please implement a function wordle_hint(w1, w2)
that return a sequence of pairs (i, c) for each
character c in w2 where i indicates the color
of c according to the rule of the wordle game:
0: c does not appear in w1
1: c appears in w1 at the same position as it does in w2
2: c appears in w1 at a different position as it does in w2
Please note that the number of times (1, c) or (2, c) appearing
in the returned sequence must be less than or equal to the number
of times c appearing in w1.
For instance,
w1 = water and w2 = water
wordle_hint(w1, w2) =
(1, w), (1, a), (1, t), (1, e), (1, r)
For instance,
w1 = water and w2 = waste
wordle_hint(w1, w2) =
(1, w), (1, a), (0, s), (2, t), (2, e)
For instance,
w1 = abbcc and w2 = bbccd
wordle_hint(w1, w2) =
(2, b), (1, b), (2, c), (1, c), (0, d)
"""
########################################################################
def wordle_hint(w1, w2):
  x0 = []
  x1 = []
  x2 = []
  for w in zip(w1, w2):
    x3, x4 = w
    if not x4 in x1:
      x1.append(x4)
      x2.append(w1.count(x4))
      
    x5 = x1.index(x4)
    if(x3 == x4):
        x0.append((1, x4))
        x2[x5] -= 1
    else:
        if(x2[x5] == 0):
          x0.append((0, x4))
        else:
          x0.append((2, x4))
          
  return x0
########################################################################
