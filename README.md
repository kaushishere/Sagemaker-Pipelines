# Model Registry Pipeline for a Classification Model
## Executive Summary
Using the Sagemaker SDK, I developed a Sagemaker Pipeline to preprocess data, train & tune a Decision Tree Classifier model and then evaluate its performance on test data. Upon evaluation, the Pipeline decides whether the model should be registered. From there, a model deployment pipeline (not shown here) can take the registered model and deploy to a Sagemaker endpoint or self-managed endpoint.

## Business Benefits of Pipelines
The advantages of using a Pipeline are reproducibility and speed. Since all the data processing, model tuning & evaluation steps are wrapped up in one abstraction, users need only interact with the high-level pipeline. This enables quicker model development. Also, different end users can execute a pipeline with different parameter values, based on their use case. For example, some users may require a simplistic model so they can more easily explain the model to their consumers. Parameters such as max_depth can be set prior to pipeline execution.

## Methodology

## Skills
Cloud: AWS Sagemaker
Python: Pandas, Scikit-learn

## before...
Pipeline history: <img src="/images/GraphExecution1.png" alt="Graph" width="1000">

Notice the model is not registered at the last step because the model only achieved a validation accuracy of 57% (only 4 training jobs were run). Models are only registered if they score 85% or more.

# Evaluation Metrics
In the evaluation step, we evaluate the best model from the tuning step by calculating the confusion matrix, and accuracy on the reserved, test dataset. Here is an example for such evaluation metrics for a model trained on a dataset that is dominated by non-fraudulent transactions (label=0).
<img src="/images/EvaluationMetrics.png" alt="Metrics" width="1000">
These metrics are available in the model registry, so users can quickly gain an understand of how "good" the model is before deployment.


