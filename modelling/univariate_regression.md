We have multiple learning algorithms/models to solve regression problems. There are 1000s of algorithms developed over the years with a different idea from different people and more such algorithms will continue to come up in the upcoming years but we study only some of the most useful and historically proven most efficient algorithms and these are listed below

# $\color{cyan}{1. Geometric\ Models\ /\ Geometry\ Based\ Regressors\ /\ Geometry\ Based\ Learning}$
---
- [Linear Regression](https://levelup.gitconnected.com/unfolding-maths-for-linear-regression-part-1-simple-linear-regression-561d9e6182f0) (Linear Model) (parametric model cause the no of parameters that needs to be determined is finite, here the parameters are weights)
- NonLinear Regression (Non Linear Model) (parametric model)
    - [Polynomial Regression](https://levelup.gitconnected.com/unfolding-math-for-polynomial-non-linear-regression-7ad8f486d53a)
    - <u> Domain Expert Regression </u> : 
        - Exactly the same as polynomial regression, just that in polynomial regression matured features were just polynomial features but here matured features need not be just polynomial features it could be anything and hence here you need the help of domain experts.
        - Say you have a feature X1 and other feature as X2 but maybe X1+2*X2 is a better feature and this can only be told by domain experts.This is called aggregation(or consolidation) if we combine any two or more features to form new features.We can also divide a feature into two or more features to form new features like full name into first name and last name, this is also called disaggregation(or passing). Such features that we get by aggregating or disaggregating are called non polynomial matured features.
        - Disadvantages : 
            - Domain Expert expenses and many a time domain expert himself does not knows 
            - Time complexity increases
            - Manual process
        - <u>Overfitting</u> : use the same regularization techniques as discussed in polynomial regression.
        - <u>Explainability</u> : Weights can be used to explain which feature is important
    - [Kernel Regression](https://khetansarvesh.medium.com/kernel-regression-fc38027cc3f3)
        - <u>Overfitting</u> : Use same regularization techniques as discussed in polynomial regression
        - <u>Explainability</u> : Weights can be used to explain which feature is important
---
- Linear Support Vector Regression (SVR) : First read linear classification, then read [SVM for classification](https://levelup.gitconnected.com/support-vector-machine-svm-an-optimisation-mammoth-5daf3bc648ad#c5b0) and come back to Linear Regression. Now you will be able to derive SVR automatically on your own from scratch because you have understood the mathematical intuition.
-  Non-Linear Support Vector Regression (SVR)
    - Polynomial SVR
    - Domain Expert SVR
    - Kernel SVR
    - Overfitting in all these methods : Use all regularization techniques discussed in polynomial regression 
    - Explainability in all these methods : Weights can be used to explain which feature is important

---

# $\color{cyan}{2. Deep\ Learning(DL)}$
Use this when you have a huge amount of data because if you use it with less data then it will lead to huge amount of overfitting and since it is huge data use advanced optimization techniques like adam to solve the optimization problem here so that it can converge fast instead of using gradient descent

- [Linear Perceptron](https://khetansarvesh.medium.com/linear-perceptron-regression-10f6f1006afb) (Linear Model)

- NonLinear Perceptron (NonLinear Model)
  - Polynomial Perceptron : 
    - Explainability : Weights can be used to explain which feature is important

  - Domain Expert Perceptron : 
    - Explainability : Weights can be used to explain which feature is important

  - Kernel Perceptron : 
    - Explainability : Weights can be used to explain which feature is important

  - Artificial Neural Network (ANN) :
    - Now the main disadvantage of all the above 3 methods is that in all the 3 methods feature extraction was to be done manually but we somehow wanted a way to do feature extraction (develop matured features) also automatically. Here we will be learning the matured features and hence you don’t need the help of a domain expert 
    - Drawback of this method is that this method can only be used if we have a huge amount of data (rows)? why to use this only when we have a huge amount of data because you will understand that this algorithm leads to too many overfitting problems and we know that if we have lots of data we can curb overfitting and hence this algorithm is only recommended when we have a huge amount of data.
    - Explainability !!



# $\color{cyan}{3. Instance\ Based\ Learning}$

## $\color{yellow}{3.1 Geometric\ Instance\ Based\ Learning}$
- K Nearest Neighbours (Piecewise Linear Model) : Same as what we saw in [KNN for classification](https://pub.towardsai.net/k-nearest-neighbours-knn-for-classification-da05a58d924b) just that here instead of majority voting we will have mean / median 

![Alt text](https://github.com/khetansarvesh/Tabular-Cross-Sectional-Modelling/blob/main/imgs/knn.png)

## $\color{yellow}{3.2 Tree\ Based\ Learning}$
- Decision Tree - Regression / Regression Tree (Piecewise Linear Model / Non Linear Model) 
    - Same as what we saw in [decision tree for classification](https://khetansarvesh.medium.com/decision-tree-classification-explained-909a2fbf5993), just that here
        - Instead of gini / entropy here we use square error loss and we consider that split which gives least squared error value on both the sides of the tree
        - Instead of majority voting we will use mean / median here. 
    - You can see the stat quest lecture on this [here](https://www.youtube.com/watch?v=g9c66TUylZ4).
    - You can find code [here](https://github.com/khetansarvesh/Tabular-Cross-Sectional-Modelling/blob/main/modelling/regression/Decision-Tree-Regression.ipynb).

![Alt text](https://github.com/khetansarvesh/Tabular-Cross-Sectional-Modelling/blob/main/imgs/tree_algo.png)
