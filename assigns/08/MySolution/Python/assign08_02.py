####################################################
#!/usr/bin/env python3
####################################################
"""
HX-2023-04-07: 20 points
You are required to implement the following function
generator_merge2 WITHOUT using streams. A solution that
uses streams is disqualified.
"""
def generator_merge2(gen1, gen2, lte3):
    c1 = next(gen1,None)
    c2 = next(gen2,None)

    while c1 is not None or c2 is not None:
        if c1 is None:
            yield c2
            c2 = next(gen2,None)
        elif c2 is None:
            yield c1
            c1 = next(gen1,None)
        elif lte3(c1, c2):
            yield c1
            c1 = next(gen1,None)
        else:
            yield c2
            c2 = next(gen2,None)
            
####################################################
