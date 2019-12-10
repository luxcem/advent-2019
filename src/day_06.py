def read_source(source):
    graph = {}
    rgraph = {}
    for line in source:
        src, dst = line.split(")")
        rgraph[dst] = src
        if src in graph:
            graph[src].append(dst)
        else:
            graph[src] = [dst]
    return graph, rgraph


def count_orbits(rgraph, identifier):
    if identifier not in rgraph:
        return 0
    else:
        return 1 + count_orbits(rgraph, rgraph[identifier])


def path_len(a, b, rgraph):
    def path(src, rgraph):
        if src == "COM":
            return ["COM"]
        return [src] + path(rgraph[src], rgraph)

    frst_path = path(a, rgraph)
    secd_path = path(b, rgraph)
    # first common ancestor
    ancestor = None
    for obj in frst_path:
        if obj in secd_path:
            ancestor = obj
            break
    return frst_path.index(ancestor) + secd_path.index(ancestor) - 2


def part1(source):
    _, rgraph = read_source(source)
    return sum([count_orbits(rgraph, obj) for obj in rgraph.keys()])


def part2(source):
    _, rgraph = read_source(source)
    return path_len("YOU", "SAN", rgraph)
