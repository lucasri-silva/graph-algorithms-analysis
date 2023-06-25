import json
import time
import random
import os
import shutil

import dijkstra
import bellman_ford
import floyd_warshall
import graph_generator

def main():
    shutil.rmtree('./result/')
    os.makedirs('./result/')
    os.makedirs('./result/positive-weight')
    os.makedirs('./result/positive-negative-weight')
    answer = input('Do you want to generate new graphs? (y/n) ')

    if answer == 'y':
        print('Gerando grafos ...')
        shutil.rmtree('./graphs')
        os.makedirs('./graphs/positive-weight')
        os.makedirs('./graphs/positive-negative-weight')

        num_nodes = 10
        num_max_nodes = 10
        num_edges = num_nodes * (num_nodes - 1)
        num_graphs = 1
        pace = 25
        densities = [1.0, 0.9, 0.6, 0.5]

        weight_range = (1, 100)
        path = 'positive-weight'
        ## generate positive weight graphs
        for density in densities:

            graph_generator.create_graphs(num_nodes, num_max_nodes, num_edges, weight_range, density, num_graphs, pace, path)

        weight_range = (-100, 100)
        path = 'positive-negative-weight'
        ## generate positive-negative weight graphs
        for density in densities:

            graph_generator.create_graphs(num_nodes, num_max_nodes, num_edges, weight_range, density, num_graphs, pace, path)


    print('Calculando caminho mínimo ...')
    # iterate over all files in directory positive-weight
    for filename in os.listdir('./graphs/positive-weight/'):
        file_path = os.path.join('./graphs/positive-weight/', filename)
        
        if os.path.isfile(file_path):
            result_file = open('./result/positive-weight/'+filename, 'w')
            with open(file_path, 'r') as file:

                for line in file:


                    graph = json.loads(line)
                    start_vertex = random.randint(0, len(graph)-1)
                    end_vertex = random.randint(0, len(graph)-1)

                    while end_vertex == start_vertex:
                        start_vertex = random.randint(0, len(graph)-1)
                        end_vertex = random.randint(0, len(graph)-1)

                    print(filename)
                    print(start_vertex)
                    print(end_vertex)
                    print(graph)
                    
                    ## DIJKSTRA
                    start_time = time.time()
                    distances, predecessors = dijkstra.dijkstra(graph, start_vertex)
                    dijkstra.dijkstra_get_path(start_vertex, end_vertex, predecessors)
                    dijkstra.dijkstra_get_cost(start_vertex, end_vertex, distances)
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    print(f"Execution time: {elapsed_time} seconds")

                    ## BELLMAN FORD 
                    start_time = time.time()
                    distances, predecessors, counter = bellman_ford.bellman_ford(graph, start_vertex)
                    bellman_ford.bellman_ford_get_path(start_vertex, end_vertex, predecessors)
                    bellman_ford.bellman_ford_get_cost(start_vertex, end_vertex, distances)
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    print(f"Execution time: {elapsed_time} seconds")

                    ## FLOYD WARSHALL
                    start_time = time.time()
                    distances, predecessors = floyd_warshall.floyd_warshall(graph)
                    end_time = time.time()
                    floyd_warshall.floyd_warshall_get_path(predecessors, distances)
                    elapsed_time = end_time - start_time
                    print(f"Execution time: {elapsed_time} seconds")

                    # result_file.write(str(elapsed_time))
                    # result_file.write('\n')
                    input('press')

                result_file.close()
                file.close()

if __name__ == "__main__":
    main()
