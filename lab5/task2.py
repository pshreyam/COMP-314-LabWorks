from graph_functions import (
    create_graph,
    print_details,
    degree_distribution,
    plot_degree_distribution
)


filenames = ["inf-power.edges", "ia-reality.edges", "3elt_dual.edges", "bio-dmela.edges", "ca-Erdos992.edges"]


for filename in filenames:
    print("\nFile: ", filename, end="\n\n")
    graph = create_graph(filename)
    print_details(graph)
    print("Degree Distribution: ", dict(zip(*degree_distribution(graph))))
    plot_degree_distribution(filename, graph)
    print("-"*30)
