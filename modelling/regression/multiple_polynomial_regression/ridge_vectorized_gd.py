import pandas as pd
import numpy as np
import math
import random

# GD implementation with stop criteria based on :- #no_of_iterations
class GradientDescent_Ridge:

  #constructor
  def _init_(self):
    self.X = 0

  #returns nothing
  def fit(self,X,Y,learning_rate = 0.000001,no_of_iteration = 10000,lambda_ridge=0.01):
    self.X = X
    self.Y = Y

    #adding bias column to X
    df = pd.DataFrame(self.X)
    bias = [1 for i in range(df.shape[0])]
    df.insert(loc = 0 , column = "bias" , value = bias )
    self.X = np.array(df)

    #taking all [c,m1,m2...] as [0,0,0.....] as initial random value and representing this in a matrix named theta
    self.current_theta = np.zeros((self.X.shape[1]))

    # making a list to store error every 50 iterations
    self.error_every_50_iteration_list = list()

    #iterating utill the difference between two errors is <= 0.001 i.e negligible
    for i in range(no_of_iteration +1):

      #calculating (theta)new = (theta)current - (leaning rate)(derivative term)
      #(derivative term) = 2*(X)t.(X.(current_theta)-(Y)t) --usually people divide derivative term with (2)
      self.new_theta = self.current_theta - (learning_rate)*((np.dot(self.X.transpose(),(np.dot(self.X,self.current_theta)-self.Y.transpose()))) + 2*(lambda_ridge)*(self.current_theta))

      #caluclating error using formula ***(error) = (X.(theta)t - (Y)t).(X.(theta)t - (Y)t)t*** -- t means transpose -some people divide this by 2
      self.error = (np.dot(np.dot(self.X,self.new_theta.transpose()) - self.Y.transpose(),(np.dot(self.X,self.new_theta.transpose()) - self.Y.transpose()).transpose()))/2 + ((lambda_ridge)*np.dot((self.new_theta),(self.new_theta.transpose())))

      self.current_theta = self.new_theta

      #storing the error after every 50 iterations
      if(i % 50 == 0):
        self.error_every_50_iteration_list.append(self.error)

  # returns an array of [c m1 m2 m3......mn]
  def coef_(self):
    return self.new_theta

  #returns no of interations taken and also returns an array with error every 50 iteration
  def error_every_50_iteration(self):
    return np.array(self.error_every_50_iteration_list)

  #returns an array of predicted values
  def predict(self,x):
    #adding bias column to x
    df = pd.DataFrame(x)
    bias = [1 for i in range(df.shape[0])]
    df.insert(loc = 0 , column = "bias" , value = bias )
    x = np.array(df)

    return np.dot(x,self.new_theta.transpose())