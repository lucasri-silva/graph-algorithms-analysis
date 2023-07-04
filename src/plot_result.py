import pandas as pd
import matplotlib.pyplot as plt

def plot():
    file_names = ['dijkstra_sparse.csv', 'bellman_sparse.csv', 'floyd_sparse.csv']
    # file_names = ['dijkstra_sparse.csv', 'bellman_sparse.csv']
    # file_names = ['dijkstra_dense.csv', 'bellman_dense.csv', 'floyd_dense.csv']
    # file_names = ['dijkstra_dense.csv', 'bellman_dense.csv']


    colors = {'dijkstra': 'red', 'bellman': 'green', 'floyd': 'blue'}

    dataframes = []

    path = '../result/positive-weight/'
    # path = '../result/positive-negative-weight/'
    for file in file_names:
        df = pd.read_csv(path+file)
        dataframes.append(df)

    for i, df in enumerate(dataframes):
        algorithm = file_names[i].split('_')[0]
        algorithm_color = colors[algorithm]
        x_column = df.columns[1]
        y_column = df.columns[0]
        plt.scatter(df[x_column], df[y_column], color=algorithm_color, label=algorithm, s=5)

    plt.xlabel('Time (s)')
    plt.ylabel('Number of nodes')
    plt.title('Positive-weight sparse graphs Dijkstra x Bellman-Ford x Floyd-Warshall')
    # plt.title('Positive-weight sparse graphs Dijkstra x Bellman-Ford')
    # plt.title('Positive-weight dense graphs Dijkstra x Bellman-Ford x Floyd-Warshall')
    # plt.title('Positive-weight dense graphs Dijkstra x Bellman-Ford')
    plt.legend()
    plt.show()
