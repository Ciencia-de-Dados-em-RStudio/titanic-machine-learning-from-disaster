
# import modules
import pandas as pd
import numpy as np 
import sklearn.linear_model as skl_lr

# set up variables and response
mtcars_data = pd.read_csv("/Users/jpalbino/OneDrive/Projetos 2021/titanic-machine-learning-from-disaster/data/mtcars.csv")
x <- mtcars_data[, -1]
y <- mtcars_data[, 1]

# convert to python objects
pyx <- r_to_py(x)
pyy <- r_to_py(y)

# create model
#skl_lr$LinearRegression$fit(pyx, pyy)
lr <- skl_lr$LinearRegression()
lr$fit(pyx, pyy)
