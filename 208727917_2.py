from math import sqrt

import pandas as pd

#df = pd.read_csv('Iris.csv')
#print(df.describe())

df = pd.read_csv('Iris.csv', index_col = ['SepalLengthCm'])
summed = 0
std = 0
amount = len(df)
for index, row in df.iterrows():
    summed = summed + index
mean = summed / amount
print("The Mean of the Sepal Length Cm is: " + str(mean))
for index, row in df.iterrows():
        new = index - mean
        new2 = new*new
        std = std + new2
std = sqrt(std / amount)
print("The Standard Deviation is: " + str(std))
print()


df = pd.read_csv('Iris.csv', index_col = ['SepalWidthCm'])
summed = 0
amount = len(df)
for index, row in df.iterrows():
    summed = summed + index
mean = summed / amount
print("The Mean of the Sepal Width Cm is: " + str(mean))
for index, row in df.iterrows():
        new = index - mean
        new2 = new*new
        std = std + new2
std = sqrt(std / amount)
print("The Standard Deviation is: " + str(std))
print()

df = pd.read_csv('Iris.csv', index_col = ['PetalLengthCm'])
summed = 0
amount = len(df)
for index, row in df.iterrows():
    summed = summed + index
mean = summed / amount
print("The Mean of the Petal Length Cm is: " + str(mean))
for index, row in df.iterrows():
        new = index - mean
        new2 = new*new
        std = std + new2
std = sqrt(std / amount)
print("The Standard Deviation is: " + str(std))
print()

df = pd.read_csv('Iris.csv', index_col = ['PetalWidthCm'])
summed = 0
amount = len(df)
for index, row in df.iterrows():
    summed = summed + index
mean = summed / amount
print("The Mean of the Petal Width Cm is: " + str(mean))
for index, row in df.iterrows():
        new = index - mean
        new2 = new*new
        std = std + new2
std = sqrt(std / amount)
print("The Standard Deviation is: " + str(std))