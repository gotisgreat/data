import numpy as np

input_x=[]
input_y=[]
n=input("enter number of elements:")
for i in range(0,n):
    input_x.append(input("enter x:"))
    input_y.append(input("enter y:"))
x=np.array(input_x, dtype ="float")
y=np.array(input_y, dtype ="float")
xy=[]
x_square=[]
x_mean=np.mean(x)
y_mean=np.mean(y)
xy_mean=np.mean(x*y)
x_square_mean=np.mean(x**2)
best_m=(x_mean*y_mean - xy_mean)/(x_mean**2-x_square_mean)
best_c=y_mean-x_mean*best_m
predict_x=input("enter x for prediction:");
predict_y=best_m*predict_x+best_c
print predict_y
