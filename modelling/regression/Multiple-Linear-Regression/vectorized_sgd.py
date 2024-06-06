import pandas as pd
import numpy as np
import math
import random

class StochasticGradientDescent:

  #constructor
  def _init_(self):
    self.X = 0

  #returns nothing
  def fit(self,X,Y,learning_rate = 0.000001,no_of_iteration = 10000):

    self.X = X
    self.Y = Y

    #adding bias column to X
    df = pd.DataFrame(self.X)
    bias = [1 for i in range(df.shape[0])]
    df.insert(loc = 0 , column = "bias" , value = bias )
    self.X = np.array(df)

    #taking all [c,m1,m2...] as [0,0,0.....] and representing this in a matrix named theta
    self.current_weights = np.zeros((self.X.shape[1]))

    # making a list to store error every 50 iterations
    self.error_every_50_iteration_list = list()

    for i in range(no_of_iteration + 1):
      #generating a random point
      self.Xp = list()
      self.Yp = list()
      random_no = random.randint(0,len(self.Y)-1)
      self.Xp.append(self.X[random_no])
      self.Yp.append(self.Y[random_no])

      #converting list into numpy array cause numpy is very fast
      self.Xp = np.array(self.Xp)
      self.Yp = np.array(self.Yp)

      #calculating (theta)new = (theta)current - (leaning rate)(derivative term)
      #(derivative term) = 2*(Xp)t.(Xp.(current_weights)-(Yp)t) --usually people divide derivative term with (2)*(no of datapoints) --some people divide it by 2
      self.new_weights = self.current_weights - (learning_rate)*(np.dot(self.Xp.transpose(),(np.dot(self.Xp,self.current_weights)-self.Yp.transpose())))

      #caluclating error using formula ***(error due to all points) = (X.(theta)t - (Y)t).(X.(theta)t - (Y)t)t*** -- t means transpose --some people divide it by 2
      self.error = (np.dot(np.dot(self.X,self.new_weights.transpose()) - self.Y.transpose(),(np.dot(self.X,self.new_weights.transpose()) - self.Y.transpose()).transpose()))/2

      self.current_weights = self.new_weights

      #storing the error after every 50 iterations
      if(i % 50 == 0):
        self.error_every_50_iteration_list.append(self.error)

  #returns an array of estimated parameters [c,m1,m2.....,mn]
  def coef_(self):
    return self.new_weights

  #returns an array with error every 50 iteration
  def error_every_50_iteration(self):
    return np.array(self.error_every_50_iteration_list)

  #returns an array of predicted values
  def predict(self,x):
    #adding bias column to x
    df = pd.DataFrame(x)
    bias = [1 for i in range(df.shape[0])]
    df.insert(loc = 0 , column = "bias" , value = bias )
    x = np.array(df)

    return np.dot(x,self.new_weights.transpose())