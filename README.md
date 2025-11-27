# Model Registry Pipeline for a Classification Model

## Executive Summary

Using the Sagemaker SDK, I developed a Sagemaker Pipeline for data processing, model training/tuning and evaluation. Upon evaluation, the Pipeline decides whether the model should be registered. In the real world, a model deployment pipeline (not shown here) could follow by taking the registered model and deploying it to a Sagemaker endpoint or self-managed endpoint for realtime inference for customers.

## Business Benefits

The advantages of using a pipeline are reproducibility and speed. Since all the data processing, model tuning & evaluation steps are wrapped up in one abstraction, users need only interact with the high-level pipeline. This enables quicker model development. Also, different end users can execute a pipeline with different parameter values, based on their use case. For example, some users may require a simplistic model so they can more easily explain the model to their consumers. Parameters such as max_depth can be set prior to pipeline execution.

## Methodology

1. Preprocessing script that does the ETL (Extract Transform Load). Transform steps include dropping unnecessary columns, imputing NaN values, converting categorical features into numerical ones, and resampling so there are equal numbers of fraudulent and genuine cases.
2. Training script that loads the datasets, trains a Decision Tree Classifier model, and stores model artifacts. This custom training script uses the built-in docker image with Scikit-learn & pandas pre-installed; scikit-learn is a necessary library to import the DecisionTreeClassifier class.
3. Evaluation script to evaluate model performance: model accuracy on test dataset and confusion matrix.
4. All scripts come together in the final pipeline. A successful execution relies on a model achieving at least 85% accuracy on the test dataset. The following execution failed to register the model because the test accuracy < 85%.

<img src="/images/GraphExecution1.png" alt="Graph" width="1000">

## Skills

Cloud: AWS Sagemaker <br>
Python: Pandas, Scikit-learn, Logging <br>
Data Science: Resampling for Imbalanced Datasets, Decision Tree, Confusion Matrix 

## Results

Below is an example of the model evaluation view for a succesfully registered model. On the right, you can see the confusion matrix and below the accuracy on the test dataset.

<img src="/images/EvaluationMetrics.png" alt="Metrics" width="1000">

Teams responsible for model deployment can use these results to decide whether a model should be approved for deployment or not. These results are not usually available in the Sagemaker Model Registry. By explicitly defining model_metrics inside the RegisterModel step, the evaluation report (accuracy, confusion matrix, etc.) becomes visible in the Model Registry—enabling deployment teams to make faster, evidence-based decisions.

## Next Steps

1. Run training job for longer to produce a model that yields more accurate results
2. Add cost optimisation considerations (e.g. spot instances for training)
3. Extend this pipeline with a "Model Deployment Pipeline" that takes the most successful model, and then deploys it to a Sagemaker Endpoint for realtime inference
