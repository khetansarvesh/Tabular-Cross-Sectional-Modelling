import numpy as np
import math
import pandas as pd

class NormalEquation:

  #constructor
  def _init_(self):
    self.X = 0

  #returns nothing
  def fit(self,X,Y):
    self.X = X
    self.Y = Y

    #adding bias column to X
    df = pd.DataFrame(self.X)
    bias = [1 for i in range(df.shape[0])]
    df.insert(loc = 0 , column = "bias" , value = bias )
    self.X = np.array(df)

    # calculating weights using the formula ***(weights) = ((x)t.(x))-1.((x)t.(y)t)**** -- t means transpose --(-1) means inverse
    self.weights = np.dot(np.linalg.inv(np.dot(self.X.transpose(), self.X)), np.dot(self.X.transpose(), self.Y.transpose()))

  # returns an array of learnt weights [W0 W1 W2 W3......Wn]
  def coef_(self):
    return self.weights

  #returns an array of predicted values
  def predict(self,x):
    #adding bias column to x
    df = pd.DataFrame(x)
    bias = [1 for i in range(df.shape[0])]
    df.insert(loc = 0 , column = "bias" , value = bias )
    x = np.array(df)

    return np.dot(x,self.weights.transpose())