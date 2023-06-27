# import matplotlib.pyplot as plt
#
# x = []
# y = []
#
# def plot():
#     with open("./result/positive-weight/dijkstra_big_dense", "r") as file:
#         for line in file:
#             values = line.strip().split(",")
#             print(values)
#             x.append(float(values[1]))
#             y.append(float(values[0]))
#
#     plt.plot(x, y)
#     plt.xlabel('Time (s)')
#     plt.ylabel('Number of nodes')
#     plt.show()
