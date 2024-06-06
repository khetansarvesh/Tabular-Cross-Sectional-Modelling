import numpy as np
import math

#pass y_actual and y_pred as numpy row array
class evaluation_metric:
  #constructor
  def _init_(self):
    self.y_pred = 0
    self.y_actual = 0

  #to caluculate *******root mean squared error = root(mean(sum(square(y_actual - y_pred))))*******
  def rmse(self , y_actual , y_pred):
    self.RMSE = 0;
    self.RMSE = math.sqrt((np.sum(((y_actual - y_pred)*(y_actual - y_pred))))/len(y_actual))
    return self.RMSE

  #to calculate ******* mean squared error = mean(sum(square(y_actual - y_pred))) **********
  def mse(self , y_actual , y_pred):
    self.MSE = 0;
    self.MSE = np.sum(((y_actual - y_pred)*(y_actual - y_pred)))/len(y_actual)
    return self.MSE

  #to calculate *******total sum of square of residue = 0.5*sum(square(y_actual - y_pred))*********
  def ssres(self , y_actual , y_pred):
    self.SSRES = 0
    self.SSRES = (np.sum((y_actual - y_pred)*(y_actual - y_pred)))/2
    return self.SSRES