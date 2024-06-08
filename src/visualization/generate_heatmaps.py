import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import logging

class HeatmapGenerationError(Exception):
    """Custom exception for errors during heatmap generation."""
    pass

def generate_heatmap(data, title='Heatmap', xlabel='X-axis', ylabel='Y-axis'):
    """
    Generates a heatmap from the provided data.

    :param data: A 2D list or numpy array representing the heatmap data.
    :param title: The title of the heatmap.
    :param xlabel: The label for the X-axis.
    :param ylabel: The label for the Y-axis.
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Generating heatmap with title: {title}")

    try:
        plt.figure(figsize=(10, 8))
        sns.heatmap(data, annot=True, fmt="d", cmap='YlGnBu')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()
    except Exception as e:
        logger.error(f"Error generating heatmap '{title}': {e}")
        raise HeatmapGenerationError(f"Error generating heatmap '{title}': {e}")

if __name__ == "__main__":
    sample_data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    generate_heatmap(sample_data, title='Sample Heatmap', xlabel='Category', ylabel='Value')
