import numpy as np
import pandas as pd
from statistical_plots import (
    create_distribution_plot,
    create_correlation_matrix,
    create_advanced_boxplot,
    create_statistical_test_plot
)

# 1. 创建分布图示例
print("\n1. 创建分布图...")
data = np.random.normal(0, 1, 1000)
fig_dist = create_distribution_plot(
    data,
    title="正态分布示例",
    show_kde=True,
    show_rug=True,
    html_filename="distribution_example.html"
)

# 2. 创建相关性矩阵示例
print("\n2. 创建相关性矩阵...")
df = pd.DataFrame(np.random.randn(100, 4), columns=['A', 'B', 'C', 'D'])
fig_corr = create_correlation_matrix(
    df,
    method="pearson",
    show_values=True,
    html_filename="correlation_example.html"
)

# 3. 创建高级箱线图示例（带置信区间）
print("\n3. 创建高级箱线图（带置信区间）...")
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
    show_ci=True,  # 显示置信区间
    ci_level=0.95,  # 95% 置信区间
    html_filename="boxplot_example.html"
)

# 4. 创建统计检验图示例
print("\n4. 创建统计检验图...")
data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(1, 1, 100)
fig_test = create_statistical_test_plot(
    data1,
    data2,
    test_type="t-test",
    show_p_value=True,
    html_filename="statistical_test_example.html"
)

print("\n所有图表已保存到 output 目录中。") 