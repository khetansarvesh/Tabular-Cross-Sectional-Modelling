# $\color{cyan}{Data\ Preprocessing\ /\ Descriptive\ Analytics}$
More information available [here](https://khetansarvesh.medium.com/tabular-data-pre-processing-pipeline-af083cab9c52) in my medium blog.


# $\color{cyan}{Data\ Modeling\ /\ Model\ Building\ /\ Machine\ Learning\ /\ Predictive\ Analytics\ /\ Data\ Learning\ /\ Pattern\ Learning\ /\ Pattern\ Recognition}$

## <ins> $\color{yellow}{Supervised\ Learning\ /\ Forecasting}$ </ins>

This algorithm is used when your table contains dependent variable (Y) (also called target variable or labeled variable) which is to be predicted and independent variables (X1,X2,X3……). And your task is the learn the function F which forms the mapping between X and Y
- Regression
    - Univariate Regression : Single Target Variable
        - [Algorithms](https://github.com/khetansarvesh/Tabular-Cross-Sectional-Modelling/blob/main/modelling/univariate_regression.md)
        - [Evaluation](https://github.com/khetansarvesh/Tabular-Cross-Sectional-Modelling/blob/main/modelling/univariate_regression_eval.md) 
    - Multivariate Regression : Multiple Target Variable
        - [Algorithms](https://khetansarvesh.medium.com/multivariate-regression-4b828cf88437)
        - Evaluation 
- Classification
    - Univariate Binary Classification
        - [Algorithms](https://github.com/khetansarvesh/Tabular-Cross-Sectional-Modelling/blob/main/modelling/univariate_binary_classification.md)
        - Evaluation
    - Multivariate Binary Classification or (Univariate / Multivariate) Multiclass Classification
        - Algorithms
        - Evaluation : [Part1](https://www.youtube.com/watch?v=tYZ6cpatw-w) || [Part2](https://www.youtube.com/watch?v=vP06aMoz4v8)
    - (Univariate / Multivariate) Multi Label Classification :
        - Now in Multi Class Classification you saw that one of the k classes can have 1 and rest will have 0 but in multi label classification m out of k classes can have 1 and rest k-m classes will have 0. Hence multi class classification is also called one of k class classification.
        - The primary change here is the usage of Binary cross-entropy with logits (BCEWithLogitsLoss) loss function instead of vanilla cross-entropy loss (CrossEntropyLoss) that is used for multiclass classification. Binary cross-entropy with logits loss allows our model to assign independent probabilities to the labels instead of applying softmax function.


## <ins> $\color{yellow}{Unsupervised\ Learning}$ </ins>
This algorithm is used when your table contains only  independent variables (X1,X2,X3……) and no dependent variable (Y). Here also the task is to learn the function F which shows relation between X1, X2, X3,....

Algorithms discussed here are used mainly for data mining purposes i.e. to explore/analyze the data already present with us and not exactly for predictive analysis i.e. predicting results. People just have put this under ML umbrella but its main use is in data mining. It includes 

1. [Dimensionality Reduction](https://github.com/khetansarvesh/Tabular-Cross-Sectional-Modelling/blob/main/modelling/dim_reduction.md)
2. Dimensionality Expansion
    - You can use overcomplete autoencoders for this task Sparse Autoencoders / Denoising Autoencoders
    - In Fact you can use any deep learning generative model
3. Denoising Data : Suppose you want to remove noise from your data then how can you do??? Use under complete autoencoders. But first you will have to create noisy data to train your autoencoder on that. You can create noisy data by adding some gaussian noise on the original data 
4. [Clustering](https://khetansarvesh.medium.com/decoding-clustering-algorithms-14375f1aedbd#d5b5)
5. Recommendation System



## <ins> $\color{yellow}{Semi\ Supervised\ Learning}$ </ins>
This algorithm is used when your table contains some data without the dependent variable (Y) and some data with the dependent variable (Y) along with the independent variables (X1,X2,X3……).Hence a combo of both supervised and unsupervised kind of data. Usually data without dependent variable (Y) is more compared with dependent variable (Y). It involves techniques like
- Active Learning (most used)
- Transductive Learning 
- Co-training 
- Self training
  
It is useful when extracting relevant features from complex and high volume data, i.e., medical images. 


## <ins> $\color{yellow}{Reinforcement\ Learning\ (RL)}$ </ins>
Analogy of training a dog : 
- if a dog does a good job we pat him and tell him to be a good boy and sometimes reward him with food 
- if he does some bad task then we say him bad boy and punish him. 
- Over time the dog gets trained and understands what is a good task and what is a bad task.

Similarly we need to do this with machines wherein the machine is exposed to an environment where it trains itself continually using trial and error. This machine learns from past experience and tries to capture the best possible knowledge to make accurate business decisions. Desired outcomes provide AI with reward while undesired outcomes result in punishments (Z function).

Hence here the task is to learn both Y (actions) and F (policy) using X (states) and Z (reward functions). Examples of this can be 
- how you learn to drive a bicycle or learn to walk via trial and error
- how to train a helicopter to automatically fly? 



# $\color{cyan}{Model\ Deployment}$

# $\color{cyan}{Model\ Monitoring}$
After model deployment, model monitoring is very crucial to have a continuous check on model performance. Models are created and optimized on training data, so testing environment data is unseen data for them. Model monitoring metrics/tools help us to infer whether the model is good enough for this testing environment. Models decay over time and require retraining or an update. Model performance decays majorly due to:
- <ins> Data Drift </ins>: It occurs when the distribution of the input features for testing/current data is different from the trained data. Due to this, the trained model is no longer relevant for this new data. Data drift can be of two types : 
    - Target drift :
        - When the distribution of target variable in the dataset changes eg during training a classifier, we had 5 datapoints of each class while during testing we observe that class2 has 10 datapoints while class 9 has only 1 datapoint.
        - Population Stability Index (PSI) is a popular metric to capture this.
        - PSI measures how much a variable has shifted in distribution between two samples over a time.
        - For PSI calculation we first split the data into groups and obtain percentage of data in each group for both development data and OOT data. These expected% and actual% are used for calculating PSI for each group. Now, we obtain our final PSI by summing up these group PSIs.
        - To interpret the PSI values, following are the rules –
            - i. If, PSI < 0.1, no change is required in existing model
            - ii. If, 0.1<= PSI < 0.2, slight distribution shift is there, some changes is model is required
            - iii. If, PSI >=0.2, (or greater than 20%) significant distribution shift is present and model should not be used anymore without redeveloping.
    - Var drift :
        - same logic as target drift but now instead of target variable here we look at independent variable(s).
        - Characteristic Stability Index (CSI) is a popular metric to capture this.
        - PSI measures overall population shift whereas CSI focuses on individual model variables used. If PSI values concludes presence of significant distribution shift , then CSI can help us in narrowing down the specific features which are majorly responsible for this.


- <ins> Concept Drift </ins>: In this, distributions remain the same, but the relationships between input features and output changes. The patterns learned through training no longer hold for the current scenario.

To tackle data drift and concept drift, we need a model monitoring system in place so that we can update or retrain the model as and when we get a red flag from this system. [Evidently](https://github.com/evidentlyai/evidently) is an open source tool for model monitoring. It creates dashboard and reports
