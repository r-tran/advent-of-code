import sys
from collections import defaultdict

def get_original_sources(graph):
    sources = set(graph.keys())
    for neighbors in graph.values():
        for n in neighbors:
            if n in sources:
                sources.remove(n)
    return list(sources)

def is_source_node(graph, visited, curr_node):
    for node in graph:
        if curr_node in graph[node]:
            if node not in visited:
                return False
    return True

instructions = open(sys.argv[1],'r').readlines()
graph = defaultdict(list)
for instruction in instructions:
    graph[instruction.split()[1]].append(instruction.split()[-3])

def part1():
    sources = get_original_sources(graph)
    nodes_visited = set()
    path = []

    while len(sources) > 0:
        front = 0
        sources.sort()
        while not is_source_node(graph, nodes_visited, sources[front]):
            front += 1
        curr = sources.pop(front)
        if curr not in nodes_visited:
            nodes_visited.add(curr)
            path.append(curr)
            for neighbor in graph[curr]:
                if neighbor not in nodes_visited:
                    sources.append(neighbor)

    return ''.join(path)

def part2(n_workers):
    sources = get_original_sources(graph)
    workers = [''] * n_workers
    worker_count = [0] * n_workers
    nodes_visited = set()
    in_progress = set()
    time = 0
    order = []

    while len(sources) > 0:
        sources.sort()
        for node in sources:
            if node not in nodes_visited and node not in in_progress and is_source_node(graph, nodes_visited, node):
                for i in range(len(workers)):
                    if workers[i] == '':
                        workers[i] = node
                        in_progress.add(node)
                        break
        for i in range(len(workers)):
            if workers[i] != '':
                worker_count[i] += 1
                if worker_count[i] == ord(workers[i]) - ord('A') + 61:
                    sources = [x for x in sources if x != workers[i]]
                    order.append(workers[i])
                    if workers[i] not in nodes_visited:
                        nodes_visited.add(workers[i])
                        for neighbor in graph[workers[i]]:
                            if neighbor not in nodes_visited:
                                sources.append(neighbor)
                    
                    in_progress.remove(workers[i])
                    worker_count[i] = 0
                    workers[i] = ''
        time += 1
    return time

print(part2(5))
