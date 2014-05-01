from pygraph import DirectedGraph
from pygraph import format_paths

g = DirectedGraph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 5)
g.add_edge(3, 4)
g.add_edge(4, 1)
g.add_edge(2, 4)
g.add_edge(2, 1)

print "Paths from 1:"
print format_paths(g.paths_out(1, 5))
print

print "Paths from 1 (including circular): "
print format_paths(g.paths_out(1, 5, circular=True))
print

print "Paths from 3:"
print format_paths(g.paths_out(3, 5))
print

print "Paths to 3:"
print format_paths(g.paths_in(3, 5))
print

print "Paths from 5:"
print format_paths(g.paths_out(5, 1))
print

print "Paths to 5:"
print format_paths(g.paths_in(5, 5))
print

print "Paths to 5 (including circular):"
print format_paths(g.paths_in(5, 5, circular=True))
print
