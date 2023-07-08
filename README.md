<html>
<body>
    <h1>Minimum Path Algorithms Comparison</h1>
      <p>Activities done during the Computer Engineering program's Optimization course at CEFET-MG.</p>
    <h2>Dijkstra's Algorithm</h2>
<p>
    Dijkstra's algorithm is a popular algorithm used to find the shortest path between two nodes in a graph. It works
    by maintaining a set of visited nodes and continually updating the shortest distance from the source node to
    other nodes in the graph. Dijkstra's algorithm guarantees the shortest path when all edge weights are non-negative.
    However, it does not work correctly when negative weights are present in the graph.
</p>

<h2>Bellman-Ford Algorithm</h2>
<p>
    The Bellman-Ford algorithm is another algorithm used for finding the shortest path between two nodes in a graph.
    Unlike Dijkstra's algorithm, Bellman-Ford can handle graphs with negative edge weights. It iteratively relaxes
    the edges of the graph until it finds the shortest path. However, if the graph contains a negative cycle, the
    algorithm detects it and reports the presence of a negative cycle instead of providing the shortest path.
</p>

<h2>Floyd-Warshall Algorithm</h2>
<p>
    The Floyd-Warshall algorithm is a dynamic programming algorithm used to find the shortest paths between all pairs
    of nodes in a graph. It considers all possible intermediate nodes and iteratively updates the shortest path
    distances. The Floyd-Warshall algorithm works correctly even if the graph contains negative edge weights or
    cycles. It provides the shortest path distances between all pairs of nodes in the graph.
</p>

<h2>Comparison Table</h2>
<table>
    <tr>
        <th>Algorithm</th>
        <th>Advantages</th>
        <th>Disadvantages</th>
    </tr>
    <tr>
        <td>Dijkstra</td>
        <td>Handles non-negative edge weights<br>Efficient for finding single-source shortest paths</td>
        <td>Does not handle negative edge weights</td>
    </tr>
    <tr>
        <td>Bellman-Ford</td>
        <td>Handles negative edge weights<br>Detects negative cycles</td>
        <td>Slower than Dijkstra's algorithm<br>May have a higher time complexity</td>
    </tr>
    <tr>
        <td>Floyd-Warshall</td>
        <td>Handles negative edge weights<br>Works for all pairs of nodes</td>
        <td>Slower than both Dijkstra's and Bellman-Ford algorithms<br>Requires more memory</td>
    </tr>
</table>
</body>
</html>
