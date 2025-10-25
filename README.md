# Pipeline Results
## 3 - With Hyperparameter Optimisation
Pipeline history: <img src="/images/GraphExecution1.png" alt="Graph" width="1000">

Notice the model is not registered at the last step because the model only achieved a validation accuracy of 57%. Models are only registered if they score 85% or more.

# Evaluation Metrics
In the evaluation step, we evaluate the best model from the tuning step by calculating the confusion matrix, and accuracy on the reserved, test dataset. Here is an example for such evaluation metrics for a model trained on a dataset that is dominated by non-fraudulent transactions (label=0).
<img src="/images/EvaluationMetrics.png" alt="Metrics" width="1000">
These metrics are available in the model registry, so users can quickly gain an understand of how "good" the model is before deployment.


