def floyd_warshall(graph):
    distances = graph
    predecessors = []

    for i in range(len(graph)):
        row = []
        for j in range(len(graph)):
            if graph[i][j] == 'inf' or j == i: 
                row.append(None)
            else:
                row.append(i+1)
        predecessors.append(row)
    
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if distances[i][k] != 'inf' and distances[k][j] != 'inf':
                    if distances[i][j] == 'inf':
                        distances[i][j] = distances[i][k] + distances[k][j]
                        predecessors[i][j] = predecessors[k][j]
                    elif distances[i][k] + distances[k][j] < distances[i][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]
                        predecessors[i][j] = predecessors[k][j]

    return distances, predecessors

def floyd_warshall_get_cost(start, destination, distances):
    return distances[start][destination]

def floyd_warshall_get_path(predecessors, distances):
    num_nodes = len(predecessors)
    
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j:
                path = list()
                if predecessors[i][j] == None:
                    pair = (i+1, j+1)
                else:
                    pair = (predecessors[i][j], j+1)
                path.append(pair)
                # print(pair)
                # input('press')
                while pair[0] != i+1 and pair[0] != None:
                    pair = (predecessors[i][pair[0]-1], pair[0])
                    path.append(pair)
                path.reverse()
                print(f"Path from {i+1} to {j+1}: {path} , Cost: {floyd_warshall_get_cost(i, j, distances)}")
