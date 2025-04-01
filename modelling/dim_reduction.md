# Dimensionality Reduction Techniques

There are many techniques to perform dimensionality reduction : 
1. <ins> Lossy Techniques </ins> : Techniques in which the reduced dataset shows somewhat less information compared to the original data fall under lossy techniques.
2. <ins> Lossless Techniques </ins> : Techniques in which the reduced dataset shows exactly the same information as the original data fall under lossless techniques.

Below we will understand many algorithms which can perform Lossy Dimensionality Reduction !! These lossy techniques can be further divided into two broad categories namely : 


# <ins> $\color{yellow}{Linear\ Lossy\ Techniques}$ </ins>
1. [Matrix Decomposition / Matrix Factorization / Principal Component Analysis (PCA)](https://pub.towardsai.net/principle-component-analysis-pca-mathematics-9cfba3c66b45) : In the blog I have only shown PCA using EVD and SVD but we can also use CUR decomposition. You can learn more about CUR decompotion is following videos -- [CUR1](https://www.youtube.com/watch?v=SO1KTzuKTSI) || [CUR2](https://www.youtube.com/watch?v=WgK_D6IyDbM) || [CUR3](https://www.youtube.com/watch?v=qgsuly5nxIw)
2. Metric Multidimensional Scaling (MDS) / Classical MDS / Principal Coordinate Analysis (PCoA)
3. Non-Negative Matrix Factorization (NMF)
4. Independent Component Analysis (ICA) 
5. Fourier transformation / Discrete Wavelength Transformation (DWT)


# <ins> $\color{yellow}{Non\ Linear\ Lossy\ Techniques\ (Manifold  Learning)}$ </ins>

## 1. Local (looks at neighbors to reduce dimensions)
## 2. Global (looks at entire dataset to reduce dimensions)

2.1. Non Linear PCA : these can be of different types like Polynomial PCA / Domain Expert PCA / Kernel PCA
    
2.2. Non Metric MDS : 

2.3. [IsoMap](https://www.youtube.com/watch?v=RPjPLlGefzw&list=PLehuLRPyt1HzQoXEhtNuYTmd0aNQvtyAK&index=4) :

2.4. Deep Unsupervised Learning :
- Self Organizing Maps (SOMs)
- You can use any generative model discussed [here](https://levelup.gitconnected.com/data-augmentation-for-regression-ffnn-8b2ca20aba7c) , I will explain with the help of UnderComplete Autoencoder (AEs). We already know we use UnderComplete AE to generate new data points but in the process we also reduce the dimensions of the inputs and this is where dimensionality reduction happens automatically and we will use those reduced dimensions. Infact, undercomplete AE behaves like PCA if 1 input layer, 1 hidden layer with identity activation function and 1 output layer with identity activation function


## 3. Transitional (can be both local / global)
3.1. UMAP : [Video](https://www.youtube.com/watch?v=iPV7mLaFWyE) || [Code](https://github.com/khetansarvesh/Tabular-Cross-Sectional-Modelling/blob/main/modelling/dimensionality-reduction/UMAP.ipynb)
