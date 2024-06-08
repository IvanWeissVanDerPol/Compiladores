import matplotlib.pyplot as plt
import logging

class ChartGenerationError(Exception):
    """Custom exception for errors during chart generation."""
    pass

def generate_bar_chart(data, title='Bar Chart', xlabel='X-axis', ylabel='Y-axis'):
    """
    Generates a bar chart from the provided data.

    :param data: A dictionary with keys as labels and values as corresponding values.
    :param title: The title of the chart.
    :param xlabel: The label for the X-axis.
    :param ylabel: The label for the Y-axis.
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Generating bar chart with title: {title}")

    try:
        labels = list(data.keys())
        values = list(data.values())
        
        plt.figure(figsize=(10, 6))
        plt.bar(labels, values, color='skyblue')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()
    except Exception as e:
        logger.error(f"Error generating bar chart '{title}': {e}")
        raise ChartGenerationError(f"Error generating bar chart '{title}': {e}")

if __name__ == "__main__":
    sample_data = {'A': 10, 'B': 20, 'C': 30, 'D': 40}
    generate_bar_chart(sample_data, title='Sample Bar Chart', xlabel='Category', ylabel='Value')
