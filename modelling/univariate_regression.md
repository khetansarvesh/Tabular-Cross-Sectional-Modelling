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

- [Linear Perceptron](https://khetansarvesh.medium.com/linear-perceptron-regression-10f6f1006afb) (Linear Model)

- NonLinear Perceptron (NonLinear Model)
  - Polynomial Perceptron : for explainability weights can be used to explain which feature is important
  - Domain Expert Perceptron : for explainability weights can be used to explain which feature is important
  - Kernel Perceptron : for explainability weights can be used to explain which feature is important
  - [Artificial Neural Network (ANN)](https://khetansarvesh.medium.com/artificial-neural-networks-anns-9ec2d198bbd8)
      - For explainability of output, we have following methods :
          - Model Agnostic Methods :
              - [LIME](https://www.youtube.com/watch?v=d6j6bofhj2M) : it has variations like C-Lime and Bayes Lime
              - [SHAP](https://www.youtube.com/watch?v=9haIOplEIGM)
              - Partial Dependence Plot (PDP)
              - Class Activation Mapping (CAM)
              - [Adverserial and Conterfactual Examples Based Methods](https://www.youtube.com/watch?v=UUZxRct8rIk)
              - Perturbation
          - Model (Deep Learning) Specific Methods :
              - Gradient Saliency Maps
              - Integrated Gradients
              - Attention
      - For explainability of intermediate features, we have following methods :
          - [Dataset Examples](https://www.youtube.com/watch?v=y0-ISRhL4Ks&list=PLTx9yCaDlo1UN8ACYqzjq2tj2m2sVr3gB&index=3) :
              - Feature Visualization
              - Activation Maimization
              - TCVA
          - [Probes](https://www.youtube.com/watch?v=HJn-OTNLnoE&list=PLTx9yCaDlo1UN8ACYqzjq2tj2m2sVr3gB&index=4)
          - [Cannonical Correlation Analysis (CCA)](https://www.youtube.com/watch?v=u7Dvb_a1D-0&list=PLTx9yCaDlo1UN8ACYqzjq2tj2m2sVr3gB&index=6) : 
              - SV_CCA
              - PW_CCA




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


# $\color{cyan}{4. Ensemble\ Learning\ /\ Mixture\ Of\ Experts}$
Let’s say you are given a non-linear regression dataset and you applied Polynomial Regression and  Polynomial SVM to it and both gave good results. Now you need a way to somehow combine both the models to get the best of both worlds, then how to do so?? Hence we use Ensemble technique wherein we can combine multiple models. It is said that Ensemble technique works best most of the time over individual models because it prevents overfitting to a great extent (hence also called a regularization technique) and also easily gives 2-3% improvement in training accuracy !!!

Now models can be combined in two ways : 
- [Parallel Ensembles](https://levelup.gitconnected.com/parallel-regression-ensemblers-be8037854336) : Construct all the models parallely independent of each other and then combine them
- Sequential Ensembles : Construct models one after another sequentially and then combine them
  - Stacking Ensemble : no more used and most people don't even know about this anymore
  - [Boosting Ensemble](https://www.youtube.com/watch?v=SEekcR7wdBc) : 
    - [Adaptive Boosting](https://www.youtube.com/watch?v=NLRO1-jp5F8) (or AdaBoost) Ensemble – decision tree : Almost same as bagging just that instead of doing simple sampling here we do weighted sampling
    ![Alt text](https://github.com/khetansarvesh/Tabular-Cross-Sectional-Modelling/blob/main/imgs/adaboost.png)
    - Gradient Boosting (or Gradient Boost) Ensemble – decision tree : [Part1](https://www.youtube.com/watch?v=Nol1hVtLOSg) || [Part2](https://www.youtube.com/watch?v=Oo9q6YtGzvc)
    - [Extreme Gradient Boosting](https://www.youtube.com/watch?v=w-_vmVfpssg&t=116s) (or XGBoost) Ensemble – decision tree
