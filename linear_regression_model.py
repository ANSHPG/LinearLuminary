# -*- coding: utf-8 -*-
"""LINEAR-REGRESSION-MODEL.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1P9KEEfDggR-0XEi5HJOF2tuW0fjG1VSL
"""

import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import seaborn as sns

"""# DATA PROCESSING"""

data = pd.read_csv('BHP.csv')

data.head()

feature = 'location'

data[feature].value_counts()

location = data[feature].value_counts().index[0]

data_location = data[(data[feature]==location) & (data['area_type']=='Super built-up  Area')]

data_location.dropna(inplace=True)

data_location.shape

row = data_location.shape[0]

data_location = data_location[['total_sqft','price']]
data_location['total_sqft'] = pd.to_numeric(data_location['total_sqft'], errors='coerce')
data_location['price'] = pd.to_numeric(data_location['price'], errors='coerce')
data_location['total_sqft'] = data_location['total_sqft']/1000

train = data_location.head(int(row*0.7))
test  = data_location.tail(int(row*0.3))

train.head()

plt.xlabel('sqft [* 1000]')
plt.ylabel('price [in Lakhs]')
plt.title(f'{location},Bangalore')
plt.scatter(test['total_sqft'],test['price'],marker = 'x',color = 'red')

x2 = train['total_sqft'].values
y2 = train['price'].values
x3 = test['total_sqft'].values
y3 = test['price'].values

x = []
y = []
print(f'x-len:{len(x)}')
print(f'y-len:{len(y)}')
for i in range (0,len(x2)):
  if(isinstance(x2[i], (int, float)) and not np.isnan(x2[i])):
    x.append(x2[i])
    y.append(y2[i])
  else:
    print(x2[i])

x_test = []
y_test = []
for i in range (0,len(x3)):
  if(isinstance(x3[i], (int, float)) and not np.isnan(x3[i])):
    x_test.append(x3[i])
    y_test.append(y3[i])
  else:
    print(x3[i])

len(x)

"""# ALGORITHM FORMATION

**SIMPLE LINEAR REGRESSION MODEL** $$Y^{(i)}= wx^{(i)}+b$$

**computing output function**: $$f_{w,b} = wx^{(i)}+b$$ which will provide linear agression model to predict price wrt sqft.
"""

f_wb = []
def compute_output(w,b,x,y) :
  m = len(x)
  for i in range(0,m):
    f_wb.append((w*x[i])+b)

"""**COST FUNCTION:** $$J_{w,b} = \frac{1}{2m}\sum\limits_{i=0}^{m} (wx^{(i)}+b-y^{(i)})^2$$ which help us in determining the parameters $$(w,b)$$ where **j_wb** will be mininmum according to the parameters"""

def compute_cost(w,b,x,y):
  j_wb = 0
  m = len(x)
  for i in range(0,m):
    j_wb += ((w*x[i])+ b - y[i])**2
    # print(train['total_sqft'].values[i])
  j_wb = (1/(2*m))*j_wb
  return j_wb

"""**GRADIENT DESCENT**
$$\frac{dj_{(w,b)}}{dw} = \frac{1}{m}\sum\limits_{i=0}^{m}[wx^{(i)}+b-y{(i)}].wx^{(i)}$$
$$\frac{dj_{(w,b)}}{db} = \frac{1}{m}\sum\limits_{i=0}^{m}wx^{(i)}+b-y{(i)}$$
Here we finding the value of parameters $$(w,b)$$ for which cost_function would be minimum , by finding where the slope of cost _function would be minimum.
"""

def compute_gradient(w,b,x,y):
  m = len(x)
  dj_dw = 0
  dj_db = 0
  for i in range(0,m):
   dj_dw += ((w*x[i])+b-y[i])*x[i]
   dj_db += (w*x[i])+b-y[i]
  dj_dw *= (1/m)
  dj_db *= (1/m)
  return(dj_dw,dj_db)

"""**IMPROVENT OF GRADIENT DESCENT ON EACH ITERATION**
$$w = w - \alpha\frac{dj_{(w,b)}}{dw}$$
$$b = b - \alpha\frac{dj_{(w,b)}}{db}$$
The cases on how w & b will change:<br>
$$ \frac{dj_{(w,b)}}{dw} > 0$$
Here, the slope will be positive and 'w' will move towards left to achive minimum.
$$ \frac{dj_{(w,b)}}{dw} < 0$$
Here, the slope will be negative and 'w' will move towards right to achive minimum.
$$ \frac{dj_{(w,b)}}{dw} = 0$$
Very rarely we will get it '0' at early, after many iterations and changing of parametrical values, we will come to a point where it will reach minimum at that time we will be getting our 'w' and 'b' <br><br>
$$Note: \alpha - controls-speed-always-positive $$  
"""

def gradient_descent(w,b,x,y,alpha,repeat,compute_gradient,compute_cost):
  j_hist = []
  w_hist = []
  b_hist = []
  dj_wb  = []
  plot_hist = []
  for i in range(0,repeat):
    dj_dw,dj_db = compute_gradient(w,b,x,y)
    w = w - (alpha*dj_dw)
    b = b - (alpha*dj_db)
    if(i<=repeat):
      j_hist.append(compute_cost(w,b,x,y))
      w_hist.append(w)
      b_hist.append(b)
      dj_wb.append((dj_dw+dj_db)/2)
      plot_hist.append([w,b])
    if((i%100)==0):
      print(f'iteration[{i+1}]: w:{w}, b:{b}, j:{j_hist[i]} dj_db:{dj_db} dj_dw:{dj_dw}')
  return(w,b,j_hist,w_hist,b_hist,dj_wb,plot_hist)

w_temp = 0
b_temp = 0
alpha_temp = 0.01 #1.0e-2
repeat = 10000
w,b,j_hist,w_hist,b_hist,dj_wb,plot_hist = gradient_descent(w_temp,b_temp,x,y,alpha_temp,repeat,compute_gradient,compute_cost)

"""# **PLOTING DATA**"""

compute_output(w,b,x,y)

plt.xlabel('sqft [* 1000]')
plt.ylabel('price [in Lakhs]')
plt.title(f'After {repeat} iterations,On Trained data')

plt.plot(x,f_wb)
plt.scatter(x,y,marker='x',color='red')
plt.legend(["Calculated Value","Trained data"], loc="lower right")

plt.scatter(x_test,y_test)

check_y = []
def check(w,b,x):
  m = len(x)
  for i in range (0,m):
    check_y.append((w*x[i]+b))
  return check_y

predict_y = check(w,b,x_test)

plt.xlabel('sqft [* 1000]')
plt.ylabel('price [in Lakhs]')

plt.title(f'After {repeat} iterations')
plt.scatter(x_test,y_test,marker='x')
plt.plot(x_test,predict_y,color='red')
plt.legend(["Actual Value", "Predicted Value"], loc="lower right")

x_plot,y_plot = np.meshgrid(w_hist,b_hist)

z_plot = []
for i in range(0,len(x_plot)):
  z_plot.append(compute_cost(x_plot[i],y_plot[i],x,y))

z_plot = np.array(z_plot)

ax = plt.axes(projection="3d")
ax.set_title('Cost Function,Linear Regression Model ANSHP')
ax.set_xlabel('parameter - w')
ax.set_ylabel('parameter - b')
ax.set_zlabel('j(w,b)')

ax.plot_surface(x_plot,y_plot,z_plot,cmap='plasma')

itern = np.arange(0,10000)

plt.xlabel('iteration')
plt.ylabel('ERROR - costFunction')
plt.title('Cost functions decreases with each iteration')
plt.plot(itern,j_hist)

data.head()

