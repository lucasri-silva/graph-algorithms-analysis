import json
import time
import random
import os
import shutil

import dijkstra
import bellman_ford
import floyd_warshall
import graph_generator
import plot_result

def clear_terminal():
    print("\033c", end="")

def main():
    answer = 1
    while answer != 4:
        print('1 - Generate new graphs')
        print('2 - Execute Dijkstra, Bellman Ford and Floyd Warshall')
        print('3 - Plot result')
        print('4 - End program')
        answer = input('Enter an option: ')

        if not answer.isdigit():
            print('Invalid option')

        else:
            answer = int(answer)
            if answer == 1:

                shutil.rmtree('./result/')
                os.makedirs('./result/')
                os.makedirs('./result/positive-weight')
                os.makedirs('./result/positive-negative-weight')

                print('Gerando grafos ...')
                shutil.rmtree('./graphs')
                os.makedirs('./graphs/positive-weight')
                os.makedirs('./graphs/positive-negative-weight')

                num_graphs = 1
                pace = 25

                ## generate positive weight graphs
                num_nodes = 10
                num_edges = num_nodes * (num_nodes - 1)
                num_max_nodes = 500
                densities = [1.0, 0.9, 0.6, 0.5]
                weight_range = (1, 100)
                path = 'positive-weight'

                # for density in densities:

                graph_generator.create_graphs(num_nodes, num_max_nodes, num_edges, weight_range, density, num_graphs, pace, path)

                ## generate positive-negative weight graphs
                num_nodes = 5
                num_max_nodes = 50
                densities = [0.5]
                weight_range = (-30, 100)
                path = 'positive-negative-weight'

                for density in densities:

                    graph_generator.create_graphs(num_nodes, num_max_nodes, num_edges, weight_range, density, num_graphs, pace, path)

                input('All good. Press any key to continue')
                clear_terminal()

            elif answer == 2:

                print('Calculando caminho mínimo ...')
                # iterate over all files in directory positive-weight
                for filename in os.listdir('./graphs/positive-weight/'):
                    file_path = os.path.join('./graphs/positive-weight/', filename)
                    graph_qtd_nodes_num = filename.split('_')[0]  
                    graph_density = filename.split('_')[1][:3]

                    if os.path.isfile(file_path):
                        if graph_density == '1.0' or graph_density == '0.9':
                            graph_density = 'dense'
                        elif graph_density == '0.6' or graph_density == '0.5':
                            graph_density = 'sparse'

                        result_file_dijkstra = open('./result/positive-weight/'+'dijkstra_'+graph_density+'.csv', 'a')
                        result_file_bellman = open('./result/positive-weight/'+'bellman_'+graph_density+'.csv', 'a')
                        result_file_floyd = open('./result/positive-weight/'+'floyd_'+graph_density+'.csv', 'a')
                        with open(file_path, 'r') as file:

                            for line in file:

                                graph = json.loads(line)
                                start_vertex = random.randint(1, len(graph))
                                end_vertex = random.randint(1, len(graph))

                                while end_vertex == start_vertex:
                                    start_vertex = random.randint(1, len(graph))
                                    end_vertex = random.randint(1, len(graph))

                                
                                ## DIJKSTRA
                                start_time = time.time()
                                distances, predecessors = dijkstra.dijkstra(graph, start_vertex)
                                # dijkstra.dijkstra_get_path(start_vertex, end_vertex, predecessors)
                                # dijkstra.dijkstra_get_cost(start_vertex, end_vertex, distances)
                                end_time = time.time()
                                elapsed_time = end_time - start_time
                                print(f"Execution time: {elapsed_time} seconds")
                                result_file_dijkstra.write(graph_qtd_nodes_num+','+str(elapsed_time))
                                result_file_dijkstra.write('\n')

                                ## BELLMAN FORD 
                                start_time = time.time()
                                distances, predecessors, counter, negative_cycle = bellman_ford.bellman_ford(graph, start_vertex)
                                # bellman_ford.bellman_ford_get_path(start_vertex, end_vertex, predecessors)
                                # bellman_ford.bellman_ford_get_cost(start_vertex, end_vertex, distances)
                                end_time = time.time()
                                elapsed_time = end_time - start_time
                                print(f"Execution time: {elapsed_time} seconds")
                                result_file_bellman.write(graph_qtd_nodes_num+','+str(elapsed_time))
                                result_file_bellman.write('\n')

                                ## FLOYD WARSHALL
                                start_time = time.time()
                                distances, predecessors = floyd_warshall.floyd_warshall(graph)
                                end_time = time.time()
                                # floyd_warshall.floyd_warshall_get_path(start_vertex, end_vertex, predecessors, distances)
                                elapsed_time = end_time - start_time
                                print(f"Execution time: {elapsed_time} seconds")
                                result_file_floyd.write(graph_qtd_nodes_num+','+str(elapsed_time))
                                result_file_floyd.write('\n')


                            result_file_dijkstra.close()
                            result_file_bellman.close()
                            result_file_floyd.close()
                            file.close()

                # iterate over all files in directory positive-negative-weight
                for filename in os.listdir('./graphs/positive-negative-weight/'):
                    file_path = os.path.join('./graphs/positive-negative-weight/', filename)
                    result_file_bellman = open('./result/positive-negative-weight/'+'bellman'+'.csv', 'a')
                    result_file_floyd = open('./result/positive-negative-weight/'+'floyd'+'.csv', 'a')
                    graph_qtd_nodes_num = filename.split('_')[0]  

                    if os.path.isfile(file_path):

                        with open(file_path, 'r') as file:

                            for line in file:

                                graph = json.loads(line)
                                start_vertex = random.randint(1, len(graph))
                                end_vertex = random.randint(1, len(graph))

                                while end_vertex == start_vertex:
                                    start_vertex = random.randint(1, len(graph))
                                    end_vertex = random.randint(1, len(graph))

                                # print(start_vertex)
                                # print(end_vertex)
                                
                                ## BELLMAN FORD 
                                start_time = time.time()
                                distances, predecessors, counter, negative_cycle = bellman_ford.bellman_ford(graph, start_vertex)
                                if negative_cycle:
                                    print('negative cycle detected')
                                elif str(distances[end_vertex-1]) == 'inf':
                                    print('there is no path between start and end node')
                                else:
                                    # bellman_ford.bellman_ford_get_path(start_vertex, end_vertex, predecessors)
                                    # bellman_ford.bellman_ford_get_cost(start_vertex, end_vertex, distances)
                                    end_time = time.time()
                                    elapsed_time = end_time - start_time
                                    print(f"Execution time: {elapsed_time} seconds")
                                    result_file_bellman.write(graph_qtd_nodes_num+','+str(elapsed_time))
                                    result_file_bellman.write('\n')
                                    # input('press')

                                    ## FLOYD WARSHALL
                                    start_time = time.time()
                                    distances, predecessors = floyd_warshall.floyd_warshall(graph)
                                    end_time = time.time()
                                    # floyd_warshall.floyd_warshall_get_path(start_vertex, end_vertex, predecessors, distances)
                                    elapsed_time = end_time - start_time
                                    print(f"Execution time: {elapsed_time} seconds")
                                    result_file_floyd.write(graph_qtd_nodes_num+','+str(elapsed_time))
                                    result_file_floyd.write('\n')
                                    # input('press')

                            file.close()

                result_file_bellman.close()
                result_file_floyd.close()
                input('All good. Press any key to continue')
                clear_terminal()

            elif answer == 3:

                plot_result.plot()
                input('All good. Press any key to continue')
                clear_terminal()


if __name__ == "__main__":
    main()
