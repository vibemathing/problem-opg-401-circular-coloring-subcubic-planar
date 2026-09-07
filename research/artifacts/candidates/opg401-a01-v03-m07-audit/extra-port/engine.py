"""Exact graph-edge counter. No imports of any earlier candidate or boundary table."""
from functools import lru_cache
from itertools import combinations

PALETTE = range(20)
ADJ = tuple(tuple(y for y in PALETTE if 7 <= abs(x-y) <= 13) for x in PALETTE)
MATRIX = tuple(tuple(int(y in ADJ[x]) for y in PALETTE) for x in PALETTE)


def edges(paths):
    return sorted({tuple(sorted((a, b))) for path in paths for a, b in zip(path, path[1:])})


@lru_cache(maxsize=2048)
def transfer(internal_constraints):
    """Sum over every internal path color; endpoints have no unary restrictions here."""
    m = MATRIX
    for boundary_color in internal_constraints:
        colors = PALETTE if boundary_color is None else ADJ[boundary_color]
        out = [[0]*20 for _ in PALETTE]
        for start in PALETTE:
            for x in colors:
                value = m[start][x]
                if value:
                    for end in ADJ[x]:
                        out[start][end] += value
        m = tuple(tuple(row) for row in out)
    return m


def theta_count(graph, boundary):
    """Exact sum-product enumeration for two/three internally disjoint paths."""
    paths, ports = graph['paths'], graph['ports']
    start, end = paths[0][0], paths[0][-1]
    assert start != end and all(p[0] == start and p[-1] == end for p in paths)
    middle = [v for p in paths for v in p[1:-1]]
    assert len(middle) == len(set(middle)) and start not in middle and end not in middle
    assert edges(paths) == sorted(tuple(e) for e in graph['edges'])
    assert all(0 <= c < 20 for c in boundary.values())
    matrices = [transfer(tuple(boundary[ports[v]] if v in ports else None for v in p[1:-1])) for p in paths]
    starts = ADJ[boundary[ports[start]]] if start in ports else PALETTE
    ends = ADJ[boundary[ports[end]]] if end in ports else PALETTE
    total = 0
    for a in starts:
        for b in ends:
            n = 1
            for matrix in matrices:
                n *= matrix[a][b]
            total += n
    return total


def witness(graph, boundary, remove_edge=None, omit_color=None):
    """Separate direct-edge DFS. Returns a full internal witness or None."""
    ee = [tuple(e) for e in graph['edges'] if tuple(e) != remove_edge]
    vs = sorted({v for e in graph['edges'] for v in e})
    neighbors = {v: set() for v in vs}
    for a,b in ee:
        neighbors[a].add(b); neighbors[b].add(a)
    colors = tuple(c for c in PALETTE if c != omit_color)
    domains = {v: set(ADJ[boundary[graph['ports'][v]]]) & set(colors)
               if v in graph['ports'] else set(colors) for v in vs}
    chosen = {}
    nodes = 0
    def search(todo, dd):
        nonlocal nodes
        nodes += 1
        if nodes > 100000:
            raise RuntimeError('bounded DFS node limit')
        if not todo:
            return dict(chosen)
        v = min(todo, key=lambda z: (len(dd[z]), -len(neighbors[z]), z))
        rest = todo - {v}
        for c in sorted(dd[v]):
            nd = dict(dd)
            for w in neighbors[v] & rest:
                nd[w] = dd[w] & set(ADJ[c])
                if not nd[w]:
                    break
            else:
                chosen[v] = c
                result = search(rest, nd)
                if result is not None:
                    return result
        chosen.pop(v, None)
        return None
    return search(set(vs), domains)


def valid(graph, boundary, coloring, aliases=()):
    if any(not 0 <= c < 20 for c in list(boundary.values())+list(coloring.values())):
        return False
    if any(boundary[a] != boundary[b] for a,b in aliases):
        return False
    vs = {v for e in graph['edges'] for v in e}
    return (set(coloring) == vs
            and all(coloring[b] in ADJ[coloring[a]] for a,b in graph['edges'])
            and all(boundary[t] in ADJ[coloring[v]] for v,t in graph['ports'].items()))


def small_replacements():
    """A specified 71-element screen, NOT an exhaustive list of all plane patches."""
    for n in range(4,8):
        cyc = [str(i) for i in range(n)]
        for pos in combinations(range(1,n),3):
            indices = (0,)+pos
            ports = {str(i):c for i,c in zip(indices,('p','s','r','q'))}
            paths = [cyc+[cyc[0]]]
            yield {'name': 'cycle-'+str(n)+'-'+str(indices), 'paths':paths, 'ports':ports, 'edges':edges(paths)}
    for lengths in ((1,3,3),(1,3,4),(2,2,4),(2,3,3)):
        next_vertex = 2; paths = []
        for length in lengths:
            paths.append(['0']+[str(i) for i in range(next_vertex,next_vertex+length-1)]+['1'])
            next_vertex += length-1
        for inner in range(3):
            outer = [p for i,p in enumerate(paths) if i != inner]
            order = outer[0]+outer[1][-2:0:-1]
            available = [v for v in order if v not in ('0','1')]
            for selected in combinations(available,4):
                cyclic = [v for v in order if v in selected]
                for shift in range(4):
                    ports = {cyclic[(shift+i)%4]:c for i,c in enumerate(('p','s','r','q'))}
                    yield {'name':'theta-'+str(lengths)+'-'+str(inner)+'-'+str(ports),
                           'paths':paths, 'ports':ports, 'edges':edges(paths)}
