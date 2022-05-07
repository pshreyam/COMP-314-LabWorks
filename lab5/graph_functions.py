import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


def create_graph(edge_list_filename):
    header_list = ["a", "b", "w"]
    df = pd.read_csv("data/"+edge_list_filename, sep=" ", header=None, names=header_list)
    graph = nx.from_pandas_edgelist(df, "a", "b", ["w"])
    return graph


def draw_graph(graph):
    nx.draw(graph)
    plt.show()


def number_of_nodes(graph):
    return nx.number_of_nodes(graph)


def number_of_edges(graph):
    return nx.number_of_edges(graph)


def average_degree(graph):
    return 2 * number_of_edges(graph) / number_of_nodes(graph)


def density(graph):
    if number_of_nodes(graph) > 1:
        return (2 * number_of_edges(graph)) / (number_of_nodes(graph)*(number_of_nodes(graph)-1))
    return 0


def diameter(graph):
    try:
        return nx.diameter(graph)
    except Exception:
        print("Diameter could not be calculated!")


def clustering_coefficient(graph):
    e = [0 for vertex in graph.nodes()]
    neighbours = [[x for x in nx.neighbors(graph, node)] for node in graph.nodes()]
    k = [len(x) for x in neighbours]
    for i, neighbour in enumerate(neighbours):
        for u in neighbour:
            for v in neighbour:
                if graph.has_edge(u, v):
                    e[i] += 1
    e = list(map(lambda x: x/2, e))
    clustering_coeff = [(2*x) / (y*(y-1)) if y > 1 else 0 for x, y in zip(e, k)]
    return sum(clustering_coeff) / len(clustering_coeff)


def print_details(graph):
    print("No. of nodes: {}, No. of edges: {}".format(number_of_nodes(graph), number_of_edges(graph)))
    print("Average Degree: {}".format(average_degree(graph)))
    print("Density: {}".format(density(graph)))
    print("Diameter: {}".format(diameter(graph)))
    print("Clustering Coefficient: {}".format(clustering_coefficient(graph)))


def degree_distribution(graph):
    degrees_of_vertices = {}
    for vertex in graph.nodes():
        degree = len([x for x in nx.neighbors(graph, vertex)])
        if degree not in degrees_of_vertices.keys():
            degrees_of_vertices[degree] = 1
        else:
            degrees_of_vertices[degree] += 1
    degrees_of_vertices = dict(sorted(degrees_of_vertices.items()))
    degrees = list(degrees_of_vertices.keys())
    degrees_count = list(map(lambda x: x/number_of_nodes(graph), degrees_of_vertices.values()))
    return degrees, degrees_count


def plot_degree_distribution(filename, graph):
    x, y = degree_distribution(graph)
    plt.plot(x, y)
    plt.title("Dataset: " + filename + " (Degree Probability Distribution)")
    plt.xlabel("Degree (k)")
    plt.ylabel("Degree Distribution (P(k))")
    plt.show()
