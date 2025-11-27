# Model Registry Pipeline for a Classification Model
## Executive Summary
Using the Sagemaker SDK, I developed a Sagemaker Pipeline to preprocess data, train & tune a Decision Tree Classifier model and then evaluate its performance on test data. Upon evaluation, the Pipeline decides whether the model should be registered. From there, a model deployment pipeline (not shown here) can take the registered model and deploy to a Sagemaker endpoint or self-managed endpoint.

## Business Benefits
The advantages of using a Pipeline are reproducibility and speed. Since all the data processing, model tuning & evaluation steps are wrapped up in one abstraction, users need only interact with the high-level pipeline. This enables quicker model development. Also, different end users can execute a pipeline with different parameter values, based on their use case. For example, some users may require a simplistic model so they can more easily explain the model to their consumers. Parameters such as max_depth can be set prior to pipeline execution.

## Methodology
1. Preprocessing script that does the ETL (Extract Transform Load). Transform steps include dropping unnecssary columns, imputing NaN values, converting categorical features into numerical ones, and resampling so there are equal numbers of fraudulent and genuine cases.
2. Training script that loads the datasets, trains a Decision Tree Classifier model, and stores model artifacts. This custom training script uses the built-in docker image with Scikit-learn & pandas pre-installed; scikit-learn is a necessary library to import the DecisionTreeClassifier class.
3. Evaluation script to evaluate model performance: model accuracy on test dataset and confusion matrix
4. All scripts come together in the final pipeline. A successful execution relies on a model achieving at least 85% accuracy on the test dataset. The following exection failed to register the model because the test accuracy < 85%
<img src="/images/GraphExecution1.png" alt="Graph" width="1000">

## Skills
Cloud: AWS Sagemaker 
Python: Pandas, Scikit-learn, Logging
Data Science: Resampling, Decision Tree, Confusion matrix 

# Results
Example for such evaluation metrics for a model trained on a dataset that is dominated by non-fraudulent transactions (label=0).
<img src="/images/EvaluationMetrics.png" alt="Metrics" width="1000">
These metrics are available in the model registry, so users can quickly gain an understand of how "good" the model is before deployment.


