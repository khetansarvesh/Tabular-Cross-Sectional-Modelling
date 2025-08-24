Now it is very difficult to decide which model to use when hence we use all the models on the same dataset via trial and error and at the end finally choose that hypothesis which is best. How to decide which model is the best? 

Obviously, the one which gives the best predictions and to check how good predictions a model gives we have several ways and these are called evaluation metrics / performance parameter / goodness of fit. Some of the most famous evaluation metrics are as follows. You can use any of these, all are proportional to each other.

- Error (lower the better) : one of the famous error is Root Mean Squared Error (RMSE) and Sum of Squared Error
- Accuray (higher the better) : one of the famous accuracy is R2

![Alt text](https://github.com/khetansarvesh/Tabular-Cross-Sectional-Modelling/blob/main/imgs/eval_metrics.png)

Another heuristic way to decide which model will work best for your data is via data visualization. If only one independent and one dependent variable you can use a scatter plot but if more than one independent variable and one dependent variable you use some dimensionality reduction technique like PCA to convert all independent variables into 1 independent variable and then plot that one independent variable with the dependent variable.

![Alt text](https://github.com/khetansarvesh/Tabular-Cross-Sectional-Modelling/blob/main/imgs/data_vis.png)
