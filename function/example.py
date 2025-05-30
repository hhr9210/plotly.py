import numpy as np
import pandas as pd
from statistical_plots import (
    create_distribution_plot,
    create_correlation_matrix,
    create_advanced_boxplot,
    create_statistical_test_plot
)

# 1. Distribution Plot Example
print("\n1. Creating distribution plot...")
data = np.random.normal(0, 1, 1000)
fig_dist = create_distribution_plot(
    data,
    title="Normal Distribution Example",
    show_kde=True,
    show_rug=True,
    html_filename="distribution_example.html"
)

# 2. Correlation Matrix Example
print("\n2. Creating correlation matrix...")
df = pd.DataFrame(np.random.randn(100, 4), columns=['A', 'B', 'C', 'D'])
fig_corr = create_correlation_matrix(
    df,
    method="pearson",
    show_values=True,
    html_filename="correlation_example.html"
)

# 3. Advanced Box Plot Example (with confidence intervals)
print("\n3. Creating advanced box plot (with confidence intervals)...")
df_box = pd.DataFrame({
    'group': ['A'] * 50 + ['B'] * 50,
    'value': np.concatenate([np.random.normal(0, 1, 50), np.random.normal(1, 1, 50)])
})
fig_box = create_advanced_boxplot(
    df_box,
    x='group',
    y='value',
    show_points=True,
    show_mean=True,
    show_ci=True,  # Show confidence intervals
    ci_level=0.95,  # 95% confidence interval
    html_filename="boxplot_example.html"
)

# 4. Statistical Test Plot Example
print("\n4. Creating statistical test plot...")
data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(1, 1, 100)
fig_test = create_statistical_test_plot(
    data1,
    data2,
    test_type="t-test",
    show_p_value=True,
    html_filename="statistical_test_example.html"
)

print("\nAll plots have been saved to the output directory.") 