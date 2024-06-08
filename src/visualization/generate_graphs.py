import matplotlib.pyplot as plt
import networkx as nx
import logging

class GraphGenerationError(Exception):
    """Custom exception for errors during graph generation."""
    pass

def generate_network_graph(graph_data, title='Network Graph'):
    """
    Generates a network graph from the provided graph data.

    :param graph_data: A dictionary with keys as nodes and values as lists of connected nodes.
    :param title: The title of the graph.
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Generating network graph with title: {title}")

    try:
        G = nx.Graph()
        
        for node, edges in graph_data.items():
            for edge in edges:
                G.add_edge(node, edge)
        
        plt.figure(figsize=(10, 6))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', linewidths=1, font_size=15)
        plt.title(title)
        plt.show()
    except Exception as e:
        logger.error(f"Error generating network graph '{title}': {e}")
        raise GraphGenerationError(f"Error generating network graph '{title}': {e}")

if __name__ == "__main__":
    sample_graph_data = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C']}
    generate_network_graph(sample_graph_data, title='Sample Network Graph')
