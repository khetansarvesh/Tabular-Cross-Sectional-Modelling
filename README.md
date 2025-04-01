# $\color{cyan}{Data\ Preprocessing\ /\ Descriptive\ Analytics}$
More information available [here](https://khetansarvesh.medium.com/tabular-data-pre-processing-pipeline-af083cab9c52) in my medium blog.


# $\color{cyan}{Data\ Modeling\ /\ Model\ Building\ /\ Machine\ Learning\ /\ Predictive\ Analytics\ /\ Data\ Learning\ /\ Pattern\ Learning\ /\ Pattern\ Recognition}$

## <ins> $\color{yellow}{Supervised\ Learning\ /\ Forecasting}$ </ins>

This algorithm is used when your table contains dependent variable (Y) (also called target variable or labeled variable) which is to be predicted and independent variables (X1,X2,X3……). And your task is the learn the function F which forms the mapping between X and Y
- Regression
- Classification

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

[Evidently](https://github.com/evidentlyai/evidently) is an open source tool for model monitoring. It creates dashboard and presents a report on –

## <ins> $\color{yellow}{Data\ Drift}$ </ins>
DATA DRIFT CAN BE OF TWO TYPES : 
- Target drift : dataset has become skewed eg 20 ventile mein atleast 5% sabka hona chahiye na
- Var drift : same logic as target but now for dependent variable


## <ins> $\color{yellow}{Concept\ Drift}$ </ins>
Underlying relation b/w dependent and independent features has itself changed
