# Advanced Statistical Visualization Module for Plotly

This module extends Plotly's capabilities with advanced statistical visualization functions. It provides enhanced tools for data analysis and visualization, making it easier to create publication-quality statistical plots.

## Features

1. **Enhanced Distribution Plots**
   - Histogram with Kernel Density Estimation (KDE)
   - Rug plot for individual data points
   - Customizable bins and styling

2. **Interactive Correlation Matrix**
   - Multiple correlation methods (Pearson, Spearman, Kendall)
   - Interactive heatmap with value display
   - Customizable color scales

3. **Advanced Box Plots**
   - Individual data points display
   - Mean value markers
   - Outlier visualization
   - Group comparison capabilities

4. **Statistical Test Visualization**
   - T-test visualization
   - Mann-Whitney U test visualization
   - P-value display
   - Interactive comparison plots

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Import the module in your Python code:
```python
from statistical_plots import (
    create_distribution_plot,
    create_correlation_matrix,
    create_advanced_boxplot,
    create_statistical_test_plot
)
```

## Usage Examples

### Distribution Plot
```python
import numpy as np
from statistical_plots import create_distribution_plot

# Generate sample data
data = np.random.normal(0, 1, 1000)

# Create distribution plot
fig = create_distribution_plot(
    data,
    title="Normal Distribution",
    show_kde=True,
    show_rug=True
)
fig.show()
```

### Correlation Matrix
```python
import pandas as pd
from statistical_plots import create_correlation_matrix

# Create sample dataframe
df = pd.DataFrame(np.random.randn(100, 4), columns=['A', 'B', 'C', 'D'])

# Create correlation matrix
fig = create_correlation_matrix(
    df,
    method="pearson",
    show_values=True
)
fig.show()
```

### Advanced Box Plot
```python
import pandas as pd
from statistical_plots import create_advanced_boxplot

# Create sample data
df = pd.DataFrame({
    'group': ['A'] * 50 + ['B'] * 50,
    'value': np.concatenate([np.random.normal(0, 1, 50), np.random.normal(1, 1, 50)])
})

# Create advanced box plot
fig = create_advanced_boxplot(
    df,
    x='group',
    y='value',
    show_points=True,
    show_mean=True
)
fig.show()
```

### Statistical Test Plot
```python
import numpy as np
from statistical_plots import create_statistical_test_plot

# Generate sample data
data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(1, 1, 100)

# Create statistical test plot
fig = create_statistical_test_plot(
    data1,
    data2,
    test_type="t-test",
    show_p_value=True
)
fig.show()
```

## HTML Dashboard Version

The module also includes an HTML dashboard version (`statistical_dashboard.html`) that provides an interactive web interface for all statistical visualizations. This version offers several advantages:

### Features of the HTML Dashboard

1. **Browser-Based Interface**
   - No Python installation required
   - Works directly in any modern web browser
   - Responsive design that adapts to different screen sizes

2. **Interactive Visualizations**
   - All plots are fully interactive
   - Support for zooming, panning, and hovering
   - Ability to download plots as images
   - Real-time data exploration

3. **Modern UI Design**
   - Clean and professional layout
   - Card-based plot containers
   - Consistent styling and typography
   - Smooth animations and transitions

4. **Implementation Details**
   - Built with pure HTML, CSS, and JavaScript
   - Uses Plotly.js for visualization
   - Client-side data generation
   - No server-side dependencies

### Using the HTML Dashboard

1. Simply open `statistical_dashboard.html` in a web browser
2. All visualizations will load automatically
3. Interact with the plots using:
   - Mouse wheel for zooming
   - Click and drag for panning
   - Hover for detailed data points
   - Download button for saving plots

### Advantages Over Python Version

- **Accessibility**: No programming knowledge required
- **Portability**: Works on any device with a web browser
- **Sharing**: Easy to share with others via web hosting
- **Performance**: Client-side rendering for smooth interactions
- **Maintenance**: No need to manage Python dependencies

## Contributing

Feel free to contribute to this module by:
1. Reporting bugs
2. Suggesting new features
3. Improving documentation
4. Adding new statistical visualization functions

## License

This project is licensed under the MIT License - see the LICENSE file for details. 