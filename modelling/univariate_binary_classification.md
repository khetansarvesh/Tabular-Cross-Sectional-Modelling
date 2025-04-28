We have multiple learning algorithms/models to solve binary classification problems. There are 1000s of algorithms developed over the years with a different idea from different people and more such algorithms will continue to come up in the upcoming years but we study only some of the most useful and historically proven most efficient algorithms and these can be broadly split into these categories

# $\color{cyan}{1. Discriminant\ Learning\ /\ Discriminant\ Based\ Classifier\ /\ Disriminant\ Models}$

These are called Discriminant based classifier because here we are trying to discriminate between the two classes i.e. find out a hyperplane via which we can separate the two classes

## $\color{yellow}{1.1 Geometric\ Discriminative\ Learning}$


---


- [Linear Classification](https://khetansarvesh.medium.com/math-behind-linear-classification-62e2a687b7e5) -- people wrongly call this as Linear Perceptron also
- Non Linear Classification
  - [Polynomial Classification](https://www.youtube.com/watch?v=3liCbRZPrZA)
  - Domain Expert Classification
  - Kernel Classification
    - Prefer not to use kernel classification because the computation time complexity increases exponentially without much change in model performance.   



---


- [Linear Support Vector Machine (SVM) Classification](https://levelup.gitconnected.com/support-vector-machine-svm-an-optimisation-mammoth-5daf3bc648ad) / Linear Hard SVM-C
- Non Linear SVM-C / Non Linear Hard SVM-C
  - [Polynomial SVM-C](https://media.springernature.com/lw685/springer-static/image/chp%3A10.1007%2F978-981-15-0214-9_87/MediaObjects/468797_1_En_87_Fig2_HTML.png)
    - Exactly same as what we saw in polynomial Regression i.e. first we map to higher dimension by generating polynomial features and then we learn a linear SVM in this higher dimension which leads to learning a non linear SVM on original smaller dimension
  - Domain Expert SVM-C
  - [Kervel SVM-C](https://github.com/khetansarvesh/Tabular-Cross-Sectional-Modelling/blob/main/modelling/classification/Kernel-SVM.ipynb)
    - Prefer to use kernel SVM because the computation time complexity increases exponentially but the model performance also increases too much.



--- 


- [Linear Soft SVM-C](https://pub.towardsai.net/decoding-linear-soft-svm-for-classification-over-linear-hard-svm-f84cbc111913)
- Non Linear Soft SVM-C
  - Polynomial
  - Domain Expert
  - Kernel 


---

- [Linear Discriminant Analysis (LDA) / Fisher's LDA (FLDA)](https://pub.towardsai.net/fishers-linear-discriminant-analysis-flda-math-decoded-ac0f632ba884)
- Non Linear Discriminant Analysis
  - Polynomial DA
    - Same as what we discussed in polynomial regression . Here we have great matured polynomial features like x1x2 x1^2 x2^2 ...and the apply LDA.Hence this results in a non linear decision boundary. If the matured features are all 2 degree polynomials then it is called quadratic discriminant analysis (QDA). Here also same problem of overfitting will arise and we can use all the regularization techniques to solve this overfitting problem
  - Domain Expert DA
  - Kernel DA
    - Prefer not to use because the computation time complexity increases exponentially without much change in model performance.
   

---

- Linear Conditional Random Fields (CRF)
- Non Linear Conditional Random Fields
  - Polynomial CRF
  - Domain Expert CRF
  - Kernel CRF 



---


## $\color{yellow}{1.2 Probabilistic\ Discriminative\ Learning}$
- [Linear Logistic Regression](https://khetansarvesh.medium.com/mathematical-orgasm-for-logistic-regression-40b404266e54)
- Non Linear Logistic Regression
  - Polynomial Logistic Regression
    - Same as what we discussed in polynomial regression . Here we great matured polynomial features like x1x2 x1^2 x2^2 ...and the apply logistics regression.Hence this results in a non linear decision boundary
    - Now the main disadvantage of this technique is that if initially we have 100 features then the no of 2 degree matured features that you generate will be 5000 which is too many and if you want to go with 3 degree matured features then you generate 170000 feature which is way too too much  and hence training time increases exponentially and hence we have other non linear models which performs better wrt training time compared to this algo.
    - Moreover here we also have to solve the problem of deciding the degree of polynomial till which you want to go (you need to take the advice of domain expert) because if you go to too high degree polynomial then you might end up overfitting the data.Hence this deciding the no of degree of polynomial is a very very difficult task and hence algo such as kernel SVM and ANN comes to our rescue wherein we can fit non linear decision boundary without the headache of deciding the no of higher degree polynomial.
    - Here also you will find overfitting and you can use the same old techniques discussed earlier to handle overfitting.  
  - Domain Expert Logistic Regression
  - Kernel Logistic Regression
    - It is advised not to use kernel classification because the computation time complexity increases exponentially without much change in model performance.
 






# $\color{cyan}{2. Supervised\ Deep\ Learning}$
- Linear Perceptron (linear model) (another representation of linear logistic regression)
  - Exactly the same as linear perceptron for regression problem just that here the output activation function used is logistic function because as we know this is just another way of representing logistic regression.Or you can use any function which ranges from 0 to 1 as the output layer activation function because we say in linear logistic regression also that we can use any other function instead of logistic function which ranges from 0 to 1. (you actually can't use any output layer activation function lying b/w 0 and 1 you need to take care that the chosen activation function does not leads to such a loss function which is saturating or lead to vanishing gradient problem (zero gradients) )
  - Cost function also used here is the same as the one used in logistic regression (we have discussed two types of cost function in logistic regression you can use any but prefer using the one which does not have the saturation issue)  
- Non Linear Perceptron (non linear model)
  - Polynomial Perceptron
  - Domain Expert Perceptron
  - Kernel Perceptron
  - ANN
    - Exactly the same as non linear perceptron for the regression problem just that here also we can take any random non linear activation function to be the hidden activation function but the output activation function has to be a logistic function instead of identity function.
    - Code Implementation available [here](https://github.com/khetansarvesh/Tabular-Cross-Sectional-Modelling/blob/main/modelling/classification/ANN.ipynb).
    - Regularization Techniques :
      - [Data Augmentation](https://levelup.gitconnected.com/data-augmentation-for-classification-ffnn-fa53c233e42e)
      - Early Stopping
      - Penalty Regularization 


