# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
tr = search.GPSProblem('T', 'R'
                       , search.romania)
gd = search.GPSProblem('G', 'D'
                       , search.romania)
ae = search.GPSProblem('A', 'E'
                       , search.romania)



#print(search.breadth_first_graph_search(ab).path())
#print(search.depth_first_graph_search(ab).path())
print(search.branch_and_bound_graph_search(ab).path())
print("****")
print(search.branch_and_bound_with_heuristic_graph_search(ab).path())
print("-------------------------------------------------------")
print(search.branch_and_bound_graph_search(tr).path())
print("****")
print(search.branch_and_bound_with_heuristic_graph_search(tr).path())
print("-------------------------------------------------------")
print(search.branch_and_bound_graph_search(gd).path())
print("****")
print(search.branch_and_bound_with_heuristic_graph_search(gd).path())
print("-------------------------------------------------------")
print(search.branch_and_bound_graph_search(ae).path())
print("****")
print(search.branch_and_bound_with_heuristic_graph_search(ae).path())


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
