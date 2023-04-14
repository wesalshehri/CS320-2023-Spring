####################################################
#!/usr/bin/env python3
####################################################
"""
HX-2023-04-07: 20 points
The following implementation is stream-based:
# def graph_bfs(nxs, fnexts):
#     visited = set()
#     def helper(qnxs):
#         if qnxs.empty():
#             return strcon_nil()
#         else:
#             nx1 = qnxs.get()
#             # print("gtree_bfs: helper: nx1 = ", nx1)
#             for nx2 in fnexts(nx1):
#                 if not nx2 in visited:
#                     qnxs.put(nx2)
#                     visited.add(nx2)
#             return strcon_cons(nx1, lambda: helper(qnxs))
#         # end-of-(if(qnxs.empty())-then-else)
#     qnxs = queue.Queue()
#     for nx0 in nxs:
#         qnxs.put(nx0)
#         visited.add(nx1)
#     return lambda: helper(qnxs)
Please give a generator-based implementation of graph_bfs!!!
"""
import queue

def generator_graph_bfs(nxs, fnexts):
    nq = queue.Queue()
    visited = set()
    for nx0 in nxs:
        nq.put(nx0)
        visited.add(nx0)
        
    while not(nq.empty()):
            nx1 = nq.get()
            for nx2 in fnexts(nx1):
                if not nx2 in visited:
                    nq.put(nx2)
                    visited.add(nx2)
            yield nx1
            
            
        
####################################################
