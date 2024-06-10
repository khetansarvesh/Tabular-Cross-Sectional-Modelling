import pandas as pd
import numpy as np
import math
import random

# MGD implementation with stop criteria based on :- #no_of_iterations
class MiniBatchGradientDescent:

  #constructor
  def _init_(self):
    self.X = 0

  #returns nothing
  def fit(self, X, Y, learning_rate = 0.000001, no_of_iteration = 10000, points_to_consider = 1):

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
      indices = random.sample(range(0, len(self.X)), points_to_consider)
      self.Xps = list()
      self.Yps = list()
      for i in indices:
        self.Xps.append(self.X[i,:])
        self.Yps.append(self.Y[i])

      #converting list into numpy array cause numpy is very fast
      self.Xps = np.array(self.Xps)
      self.Yps = np.array(self.Yps)

      #calculating (theta)new = (theta)current - (leaning rate)(derivative term)
      #(derivative term) = 2*(Xp)t.(Xp.(current_weights)-(Yp)t) --usually people divide derivative term with (2)*(no of datapoints) --some people divide it by 2
      self.new_weights = self.current_weights - (learning_rate)*(np.dot(self.Xps.transpose(),(np.dot(self.Xps,self.current_weights)-self.Yps.transpose())))

      #caluclating error using formula ***(error due to all points) = (X.(theta)t - (Y)t).(X.(theta)t - (Y)t)t*** -- t means transpose --some people divide it by 2
      self.error = (np.dot(np.dot(self.Xps,self.new_weights.transpose()) - self.Yps.transpose(),(np.dot(self.Xps,self.new_weights.transpose()) - self.Yps.transpose()).transpose()))/2

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



# MGD implementation with stop criterai based on :- utill the difference between two errors is <= 0.001 i.e negligible
class MiniBatchGradientDescent_ErrorDiff_Stop:

  #constructor
  def _init_(self):
    self.X = 0

  #returns nothing
  def fit(self,X,Y,learning_rate = 0.000001,no_of_iterations = 10000, points_to_consider = 1):
    self.X = X
    self.Y = Y

    #adding bias column to X
    df = pd.DataFrame(self.X)
    bias = [1 for i in range(df.shape[0])]
    df.insert(loc = 0 , column = "bias" , value = bias )
    self.X = np.array(df)

    #taking all [c,m1,m2...] as [0,0,0.....] as initial random value can be anything and representing this in a matrix named weights
    self.current_weights = np.zeros((self.X.shape[1]))

    #calculating intial error using the formula ***(error) = (X.(theta)t - (Y)t).(X.(theta)t - (Y)t)t*** -- t means transpose -some people divide this by 2
    self.current_error = (np.dot(np.dot(self.X,self.current_weights.transpose()) - self.Y.transpose(),(np.dot(self.X,self.current_weights.transpose()) - self.Y.transpose()).transpose()))/2
    self.error_diff = self.current_error

    # to keep a count of iterations that has occured
    self.no_of_iteration = 0;

    # making a list to store error every 50 iterations
    self.error_every_50_iteration_list = list()
    self.error_every_50_iteration_list.append(self.current_error)

    #iterating utill the difference between two errors is <= 0.001 i.e negligible
    while(self.error_diff > 0.00000001):

      #generation Xps i.e. random points matrix
      indices = random.sample(range(0, len(self.X)), points_to_consider)
      self.Xps = list()
      self.Yps = list()
      for i in indices:
        self.Xps.append(self.X[i,:])
        self.Yps.append(self.Y[i])
      self.Xps = np.array(self.Xps)
      self.Yps = np.array(self.Yps)

      #calculating (theta)new = (theta)current - (leaning rate)(derivative term)
      #(derivative term) = 2*(X)t.(X.(current_weights)-(Y)t) --usually people divide derivative term with (2)
      self.new_weights = self.current_weights - (learning_rate)*(np.dot(self.Xps.transpose(),(np.dot(self.Xps,self.current_weights)-self.Yps.transpose())))

      #caluclating error using formula ***(error) = (X.(theta)t - (Y)t).(X.(theta)t - (Y)t)t*** -- t means transpose -some people divide this by 2
      self.new_error = (np.dot(np.dot(self.Xps,self.new_weights.transpose()) - self.Yps.transpose(),(np.dot(self.Xps,self.new_weights.transpose()) - self.Yps.transpose()).transpose()))/2

      #updating the error difference
      self.error_diff = abs(self.current_error - self.new_error)
      self.current_error = self.new_error
      self.current_weights = self.new_weights

      #counting the no of interation taken to run the algorithm
      self.no_of_iteration = self.no_of_iteration + 1

      #storing the error after every 50 iterations
      if(self.no_of_iteration % 50 == 0):
        self.error_every_50_iteration_list.append(self.new_error)

      #breaking if no_of_iteration for achieving error_diff = 0.00000001 exceeds the no_of_iterations specified by user
      if(self.no_of_iteration > no_of_iterations):
        break;

  # returns an array of [c m1 m2 m3......mn]
  def coef_(self):
    return self.new_weights

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

    return np.dot(x,self.new_weights.transpose())
