We have multiple learning algorithms/models to solve binary classification problems. There are 1000s of algorithms developed over the years with a different idea from different people and more such algorithms will continue to come up in the upcoming years but we study only some of the most useful and historically proven most efficient algorithms and these can be broadly split into these categories
















# $\color{cyan}{1. Discriminant\ Learning\ /\ Discriminant\ Based\ Classifier\ /\ Disriminant\ Models}$

These are called Discriminant based classifier because here we are trying to discriminate between the two classes i.e. find out a hyperplane via which we can separate the two classes



## $\color{yellow}{1.1 Probabilistic\ Discriminative\ Learning}$
- [Linear Logistic Regression](https://khetansarvesh.medium.com/multi-class-linear-logistic-regression-linear-softmax-regression-fac5569387df)
- Non Linear Logistic Regression
  - Polynomial Logistic Regression 
  - Domain Expert Logistic Regression
  - Kernel Logistic Regression
 



## $\color{yellow}{1.2 Geometric\ Discriminative\ Learning}$


---


- [Linear Classification](https://khetansarvesh.medium.com/math-behind-linear-classification-62e2a687b7e5) : convert into multiple binary class classification problem and train multiple models
  - One vs All / One vs Rest
  - One vs One
- Non Linear Classification
  - Polynomial Classification
  - Domain Expert Classification
  - Kernel Classification


---


- [Linear Support Vector Machine (SVM) Classification](https://levelup.gitconnected.com/support-vector-machine-svm-an-optimisation-mammoth-5daf3bc648ad) / Linear Hard SVM-C : 
convert into multiple binary class classification problem and train multiple models
  - One vs All / One vs Rest
  - One vs One
- Non Linear SVM-C / Non Linear Hard SVM-C
  - Polynomial SVM-C
  - Domain Expert SVM-C
  - Kervel SVM-C



--- 


- [Linear Soft SVM-C](https://pub.towardsai.net/decoding-linear-soft-svm-for-classification-over-linear-hard-svm-f84cbc111913)
- Non Linear Soft SVM-C
  - Polynomial
  - Domain Expert
  - Kernel 


---

- [Linear Discriminant Analysis (LDA) / Fisher's LDA (FLDA)](https://pub.towardsai.net/fishers-linear-discriminant-analysis-flda-math-decoded-ac0f632ba884) : convert into multiple binary class classification problem and train multiple models
  - One vs All / One vs Rest
  - One vs One
- Non Linear Discriminant Analysis
  - Polynomial DA
  - Domain Expert DA
  - Kernel DA
   

---

- Linear Conditional Random Fields (CRF)
- Non Linear Conditional Random Fields
  - Polynomial CRF
  - Domain Expert CRF
  - Kernel CRF 































# $\color{cyan}{2. Supervised\ Deep\ Learning}$
You can read more about this in the following blog post.
























# $\color{cyan}{3. Generative\ Learning\ /\ Generative\ Based\ Classifiers\ /\ Generative\ Models}$
These are called generative classifier because here we try to understand how the two classes data was generated using bayes theorem in probability. 

## $\color{yellow}{Probabilistic\ Generative\ Learning}$
- [Gaussian Discriminant Analysis (GDA) or Bayes](https://levelup.gitconnected.com/bayes-algorithm-for-binary-classification-explained-with-equations-df6ccd977631) : convert into multiple binary class classification problem and train multiple models
  - One vs All / One vs Rest
  - One vs One
  - Refer to the following [link](https://khetansarvesh.medium.com/multiclass-bayes-classification-algorithm-decoded-1640e6ed29c4) to understand about decision boundary

- [Naive Bayes (NB)](https://levelup.gitconnected.com/naive-bayes-nb-for-classification-explained-4fe4210d9538) (Same decision boundary as Bayes) : convert into multiple binary class classification problem and train multiple models
  - One vs All / One vs Rest
  - One vs One

















# $\color{cyan}{4. Instance\ Based\ Learning}$

## $\color{yellow}{4.1. Geometric\ Instance\ Based\ Learning}$
- [Linear K-Nearest Neighbors (KNN)](https://pub.towardsai.net/k-nearest-neighbours-knn-for-classification-da05a58d924b) : convert into multiple binary class classification problem and train multiple models
  - One vs All / One vs Rest
  - One vs One

## $\color{yellow}{4.2. Tree\ Based\ Learning\ /\ Tree\ Based\ Classifiers\ /\ Tree\ Models\ /\ Tree\ Algorithms\ /\ Rule\ Based\ Classifier}$
- [Decision Tree Classification](https://khetansarvesh.medium.com/decision-tree-classification-explained-909a2fbf5993) : Piecewise Linear / Non-Linear Model
Here we don't do one vs all / one vs one instead we can make changes to the original algo only to incorporate multi class. This change is
  - In binary classification you saw the tree had 2 branches at each step
  - In case of 3 classes it will have 3 branches at each step
  - In case of 4 classes it will have 4 branches at each step
  - In case of c classes it will have c branches at each step








