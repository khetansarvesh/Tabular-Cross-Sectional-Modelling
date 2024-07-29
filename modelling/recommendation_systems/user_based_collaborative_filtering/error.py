import numpy as np
import pandas as pd
import time
import math
import random

class Error:

    def __init__(self):
        self.top_k=500
        
    def rmse(self,rating,xyz):
        """
        This method calculates the Root Mean Square Error from predicted and actual rating of the user
        :param rating: A 2-d numpy array containing the actual and predicted rating
        :param xyz: integer for deciding which model is used for calculations
        :return: void
        """
        b=rating[0]-rating[1]
        c=np.square(b)
        sum=np.sum(c)
        x=rating.shape
        rmse=(sum/x[1])
        #print(rmse)
        rmse=sqrt(rmse)
        #print(rmse)
        #print(x)
        if xyz == 4:
            print("The Root mean Square error in SVD model with 90* retained Energy is " + str(rmse))
        if xyz==1:
            print("The Root mean Square error in collaborative filtering model without baseline approach is "+str(rmse))
        if xyz==2:
            print("The Root mean Square error in collaborative filtering model with baseline approach is "+str(rmse))
        if xyz == 6:
            print("The Root mean Square error in CUR model with 90% retained Energy is " + str(rms(rmse)))
        if xyz == 5:
            print("The Root mean Square error in CUR model with 100% retained Energy is " + str(rmse))
        if xyz == 3:
            print("The Root mean Square error in SVD model with 100% retained Energy is " + str(rmse))

    def precison_at_top_k(self,rating,x):
        """
        This method calculates the Prescison at the top k from predicted and actual rating of the user
        :param rating: A 2-d numpy array containing the actual and predicted rating
        :param xyz: integer for deciding which model is used for calculations
        :return: void
        """

        list1=rating.T.tolist()
        list1.sort(reverse=True)
        rating=np.array(list1)
        rating=rating.T
        occurence_more_than_3= rating[1]>3
        no_of_relevant_items=occurence_more_than_3.sum()
        recommend_array=np.array(list1[:self.top_k])
        recommend_array=recommend_array.T
        recommend_greater_than_3=recommend_array[0]>3
        relevant_greater_than_3=recommend_array[1]>3
        no_of_recomend_items=0
        for i in range(self.top_k):
            if recommend_greater_than_3[i]==True and relevant_greater_than_3[i]==True:
                no_of_recomend_items+=1

        prescison=(no_of_recomend_items/no_of_relevant_items)
        #print("the prescison is "+str(prescison))
        if x==1:
            print("The Prescison at top K in collaborative filtering model without baseline approach is "+str(prescison))
        if x==2:
            print("The Prescison at top K in collaborative filtering model with baseline approach is "+str(prescison))
        if x == 5:
            print("The Prescison at top K in CUR model with 100% retained Energy is " + str(prescison))
        if x == 3:
            print("The Prescison at top K in SVD model with 100% retained Energy is " + str(prescison))
        if x == 6:
            print("The Prescison at top K in CUR model with 90% retained Energy is " + str(prescison))
        if x == 4:
            print("The Prescison at top K in SVD model with 90* retained Energy is " + str(prescison))

    def spearman_rank_corelation(self,rating,x):
        """
        This method calculates the Spearman Rank Correlation from predicted and actual rating of the user
        :param rating: A 2-d numpy array containing the actual and predicted rating
        :param xyz: integer for deciding which model is used for calculations
        :return: void
        """
        xyz = rating.shape
        length = xyz[1]
        ranks = np.zeros((2, length))
        ranks[0] = pd.Series(rating[0]).rank()
        ranks[1] = pd.Series(rating[1]).rank()
        mean_predicted = (np.sum(ranks[0]) / length)
        mean_actual = (np.sum(ranks[1]) / length)
        ranks[0] = ranks[0] - mean_predicted
        ranks[1] = ranks[1] - mean_actual
        temp = ranks.copy()
        temp = np.square(temp)
        sum = np.sum(temp, axis=1)
        numerator = np.dot(ranks[0], ranks[1].T)
        coff = numerator / sqrt((sum[0] * sum[1]))
        # print("the coff is "+str(coff))
        if x == 1:
            print("The Spearman Rank Correlation in collaborative filtering model without baseline approach is " + str(coff))
        if x == 2:
            print("The Spearman Rank Correlation at top K in collaborative filtering model with baseline approach is " + str(coff))
        if x == 5:
            print("The Spearman Rank Correlation at top K in CUR model with 100% retained Energy is " + str(coff))
        if x == 3:
            print("The Spearman Rank Correlation at top K in SVD model with 100% retained Energy is " + str(coff))
        if x == 6:
            print("The Spearman Rank Correlation at top K in CUR model with 90% retained Energy is " + str(coff))
        if x == 4:
            print("The Spearman Rank Correlation at top K in SVD model with 90* retained Energy is " + str(coff))