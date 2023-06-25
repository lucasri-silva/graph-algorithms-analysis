import random
import networkx as nx
import numpy as np
import json

def create_graphs(num_nodes, num_max_nodes, num_edges, weight_range, density, num_graphs, pace, path):

    while num_nodes <= num_max_nodes:

        num_graphs_per_num_nodes = num_graphs

        while num_graphs_per_num_nodes:
            graph = generate_random_graph(num_nodes, num_edges, weight_range, density)
            write_graph_to_file(graph, num_nodes, density, path)
            num_graphs_per_num_nodes -= 1

        num_nodes += pace
        num_edges = num_nodes * (num_nodes - 1)

def generate_random_graph(num_nodes, num_edges, weight_range, density):
    graph = nx.DiGraph()
    graph.add_nodes_from(range(num_nodes))
    max_edges = num_nodes * (num_nodes - 1)
    num_edges = min(num_edges, int(max_edges * density))
    
    for _ in range(num_edges):
        source = random.randint(0, num_nodes - 1)
        target = random.randint(0, num_nodes - 1)
        while target == source or graph.has_edge(source, target):
            source = random.randint(0, num_nodes - 1)
            target = random.randint(0, num_nodes - 1)
        weight = random.randint(weight_range[0], weight_range[1])
        graph.add_edge(source, target, weight=weight)

    return graph

def write_graph_to_file(graph, num_nodes, density, path):
    file_path = "./graphs/"+path+"/"+str(num_nodes)+"_"+str(density)+".json"
    file = open(file_path, 'a')

    adj_matrix = nx.adjacency_matrix(graph).todense()
    adj_matrix = np.array(adj_matrix)
    adj_list = adj_matrix.tolist()

    for i in range(len(adj_list)):
        for j in range(len(adj_list)):
            if i != j and adj_list[i][j] == 0:
                adj_list[i][j] = 'inf'

    json.dump(adj_list, file)
    file.write('\n')
    file.close()
