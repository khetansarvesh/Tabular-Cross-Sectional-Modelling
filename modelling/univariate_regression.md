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