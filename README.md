# Pipeline Results
## 3 - With Hyperparameter Optimisation
Pipeline history: <img src="/images/GraphExecution1.png" alt="Graph" width="1000">

Notice the model is not registered at the last step because the model only achieved a validation accuracy of 57%. Models are only registered if they score 85% or more.

In the evaluation step, there are model metrics calculated and shown in the event the model is registered. Here is an example of such model metrics for a model trained on a fraud transactions dataset that has not been resampled.

