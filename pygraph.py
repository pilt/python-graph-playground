from collections import defaultdict


class DirectedGraph(object):

    def __init__(self):
        self._out = defaultdict(set)
        self._in = defaultdict(set)

    def add_edge(self, from_node, to_node):
        self._out[from_node].add(to_node)
        self._in[to_node].add(from_node)

    def remove_edge(self, from_node, to_node):
        self._out[from_node].remove(to_node)
        self._in[to_node].remove(from_node)

    def paths_out(self, node, max_distance, circular=False):
        return get_paths(self._out, node, max_distance, circular)

    def paths_in(self, node, max_distance, circular=False):
        return [[reversed(p) for p in pp] for pp
                in get_paths(self._in, node, max_distance, circular)]


def get_paths(inner_graph, node, max_distance, circular):
    paths = defaultdict(list)
    _paths(inner_graph, node, [], max_distance, paths, set(), circular)

    inverted_paths = []
    for d in range(max_distance - 1, -1, -1):
        inverted_paths.append(list(paths[d]))

    return inverted_paths


def _paths(inner_graph, node, path, distance, dist_paths, seen, circular):
    dist_paths[distance].append(path + [node])
    seen.add(node)

    if distance == 0:  # max distance reached
        return
    for n in inner_graph[node]:
        if not circular and n in seen:  # prevent circular paths
            continue
        _paths(inner_graph, n, path[::] + [node], distance - 1,
               dist_paths, seen.copy(), circular)


def format_paths(paths):
    fmt = []
    for i, distance_paths in enumerate(paths):
        fmt.append("{}: {}".format(i + 1,
                                   "\n   ".join(["->".join(map(str, dp))
                                                 for dp in distance_paths])))
    return "\n".join(fmt)
