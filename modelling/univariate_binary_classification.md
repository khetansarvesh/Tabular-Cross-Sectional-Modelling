We have multiple learning algorithms/models to solve binary classification problems. There are 1000s of algorithms developed over the years with a different idea from different people and more such algorithms will continue to come up in the upcoming years but we study only some of the most useful and historically proven most efficient algorithms and these can be broadly split into these categories

# $\color{cyan}{1.Discriminant\ Learning\ /\ Discriminant\ Based\ Classifier\ /\ Disriminant\ Models}$

These are called Discriminant based classifier because here we are trying to discriminate between the two classes i.e. find out a hyperplane via which we can separate the two classes

## $\color{yellow}{1.1 Geometric\ Discriminative\ Learning}$


---


### [Linear Classification](https://khetansarvesh.medium.com/math-behind-linear-classification-62e2a687b7e5) (Linear Model) : people wrongly call this as Linear Perceptron also
### Non Linear Classification (Non Linear Model)
  - [Polynomial Classification](https://www.youtube.com/watch?v=3liCbRZPrZA)
  - Domain Expert Classification
  - Kernel Classification
    - Prefer not to use kernel classification because the computation time complexity increases exponentially without much change in model performance.   



---


- [Linear Support Vector Machine (SVM) Classification](https://levelup.gitconnected.com/support-vector-machine-svm-an-optimisation-mammoth-5daf3bc648ad) (Linear Model) (also called Hard SVM)
- Non Linear SVM-C (Non Linear Model)
  - Polynomial SVM-C
    - Exactly same as what we saw in polynomial Regression i.e. first we map to higher dimension by generating polynomial features and then we learn a linear SVM in this higher dimension which leads to learning a non linear SVM on original smaller dimension
  - Domain Expert SVM-C
  - [Kervel SVM-C](https://github.com/khetansarvesh/Tabular-Cross-Sectional-Modelling/blob/main/modelling/classification/Kernel-SVM.ipynb)
    - Prefer to use kernel SVM because the computation time complexity increases exponentially but the model performance also increases too much.



--- 




## $\color{yellow}{1.2 Probabilistic\ Discriminative\ Learning}$
