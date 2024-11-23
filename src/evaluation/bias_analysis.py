# Bias Analysis using Fairlearn

from fairlearn.metrics import MetricFrame
from sklearn.metrics import accuracy_score
import pandas as pd

# Example data - Replace these with actual predictions and labels
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]
sensitive_features = ['groupA', 'groupB', 'groupA', 'groupB', 'groupA', 'groupB', 'groupA', 'groupB', 'groupA', 'groupB']

# Bias Evaluation with Fairlearn
metric_frame = MetricFrame(
    metrics=accuracy_score,
    y_true=y_true,
    y_pred=y_pred,
    sensitive_features=sensitive_features
)

print("Overall Accuracy:", metric_frame.overall)
print("Group Metrics:", metric_frame.by_group)

# Output results to a CSV for visualization
group_metrics_df = pd.DataFrame(metric_frame.by_group)
group_metrics_df.to_csv('bias_metrics.csv', index=True)
