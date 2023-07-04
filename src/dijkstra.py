def dijkstra(graph, start):
    num_vertices = len(graph)
    distances = [float('inf')] * num_vertices
    predecessors = [None] * num_vertices
    distances[start-1] = 0
    Q = list(range(num_vertices))

    while Q:
        disconnectedNode = False
        current_vertex = Q[0]
        vertex_distance = distances[current_vertex]

        for vertex in Q:
            if distances[vertex] < vertex_distance:
                vertex_distance = distances[vertex]
                current_vertex = vertex

        Q.remove(current_vertex)

        for neighbor in range(num_vertices):
            if vertex_distance != 'inf' and graph[current_vertex][neighbor] != 'inf':
                if distances[neighbor] == 'inf':
                    distances[neighbor] = vertex_distance + graph[current_vertex][neighbor]
                    predecessors[neighbor] = current_vertex + 1
                elif (vertex_distance + graph[current_vertex][neighbor] < distances[neighbor]):
                    distances[neighbor] = vertex_distance + graph[current_vertex][neighbor]
                    predecessors[neighbor] = current_vertex + 1

        for vertex in Q:
            if distances[vertex] != 'inf':
                disconnectedNode = False
        if disconnectedNode: break


    return distances, predecessors

def dijkstra_get_path(start, destination, predecessors):
    C = list()
    r = destination
    while r != start:
        pair = (predecessors[r-1], r)
        C.append(pair)
        r = pair[0] 

    print(f'Minimum Path ({start}->{destination}): {C[::-1]}')


def dijkstra_get_cost(start, destination, distances):
    print(f'Cost ({start}->{destination}): {distances[destination-1]}')
