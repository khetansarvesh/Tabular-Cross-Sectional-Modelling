# Dimensionality Reduction Techniques

There are many techniques to perform dimensionality reduction : 
1. Lossy Techniques : Techniques in which the reduced dataset shows somewhat less information compared to the original data fall under lossy techniques.
2. Lossless Techniques : Techniques in which the reduced dataset shows exactly the same information as the original data fall under lossless techniques.

Below we will understand many algorithms which can perform Lossy Dimensionality Reduction !! These lossy techniques can be further divided into two broad categories namely : 

## Linear Lossy Techniques
1. [Matrix Decomposition / Matrix Factorization / Principal Component Analysis (PCA)](https://pub.towardsai.net/principle-component-analysis-pca-mathematics-9cfba3c66b45) : In the blog I have only shown PCA using EVD and SVD but we can also use CUR decomposition. You can learn more about CUR decompotion is following videos -- [CUR1](https://www.youtube.com/watch?v=SO1KTzuKTSI) || [CUR2](https://www.youtube.com/watch?v=WgK_D6IyDbM) || [CUR3](https://www.youtube.com/watch?v=qgsuly5nxIw)
2. 
3. Non-Negative Matrix Factorization (NMF)
4. Independent Component Analysis (ICA) 
5. Fourier transformation / Discrete Wavelength Transformation (DWT)

## Non Linear Lossy Techniques (Manifold Learning)


This algorithm is used when your table contains only  independent variables (X1,X2,X3……) and no dependent variable (Y). Here also the task is to learn the function F which shows relation between X1, X2, X3,....

Algorithms discussed here are used mainly for data mining purposes i.e. to explore/analyze the data already present with us and not exactly for predictive analysis i.e. predicting results. People just have put this under ML umbrella but its main use is in data mining. It includes 

### <ins> 1. Dimensionality Reduction </ins>
You can read more about it here

### <ins> 2. Dimensionality Expansion </ins>
- You can use overcomplete autoencoders for this task Sparse Autoencoders / Denoising Autoencoders
- In Fact you can use any deep learning generative model

### <ins> 3. Denoising Data </ins>
Suppose you want to remove noise from your data then how can you do??? Use under complete autoencoders
But first you will have to create noisy data to train your autoencoder on that. You can create noisy data by adding some gaussian noise on the original data 

### <ins> 4. [Clustering](https://khetansarvesh.medium.com/decoding-clustering-algorithms-14375f1aedbd#d5b5) </ins>

### <ins> 5. Recommendation System </ins>
