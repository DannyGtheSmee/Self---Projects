#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
from sklearn.linear_model import LinearRegression
get_ipython().run_line_magic('matplotlib', 'inline')


# In[38]:


file_path = '/Users/throwgoods/Downloads/kc_house_data.csv'
df = pd.read_csv(file_path)
print(df.head())


# In[39]:


df.dtypes


# In[40]:


df.describe()


# In[42]:


columns_to_drop = ['id', 'Unnamed: 0']

for col in columns_to_drop:
    if col in df.columns:
        df.drop(col, axis=1, inplace=True)

print(df)


# In[43]:


df['floors'].value_counts().to_frame()


# In[44]:


wf = df['waterfront']
price = df['price']

sns.boxplot(x = wf, y = price)


# In[45]:


sns.regplot(x = "sqft_above", 
            y = "price", 
            data = df)
plt.show()


# In[46]:


df.corr()['price'].sort_values()


# In[47]:


X = df[['long']]
Y = df['price']
lm = LinearRegression()
lm.fit(X,Y)
lm.score(X, Y)


# In[48]:


sqft_living = df[['sqft_living']]
price = df['price']

lm = LinearRegression()
lm.fit(sqft_living,price)
lm.score(sqft_living, price)


# In[49]:


features =["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]     


# In[50]:


price = df['price']
x = df[features]
lm = LinearRegression()
lm.fit(x,price)
lm.score(x, price)


# In[51]:


Input=[('scale',StandardScaler()),('polynomial', PolynomialFeatures(include_bias=False)),('model',LinearRegression())]


# In[52]:


pipe=Pipeline(Input)
pipe
pipe.fit(df[features],df['price'])
pipe.score(df[features],df['price'])


# In[53]:


from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
print("done")


# In[54]:


X = df[features]
Y = df['price']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, random_state=1)

print("number of test samples:", x_test.shape[0])
print("number of training samples:",x_train.shape[0])


# In[55]:


from sklearn.linear_model import Ridge


# In[56]:


RidgeModel = Ridge(alpha = 0.1)
RidgeModel.fit(x_train, y_train)
RidgeModel.score(x_test, y_test)


# In[57]:


polylm = PolynomialFeatures(degree=2)

x_train_polylm=polylm.fit_transform(x_train[['floors', 'waterfront','lat' ,'bedrooms' ,'sqft_basement' ,'view' ,'bathrooms','sqft_living15','sqft_above','grade','sqft_living']])

RidgeModel=Ridge(alpha=0.1)
RidgeModel.fit(x_train_polylm, y_train)

print('R^2 for second order polynomial transform the Training data by fitting a Ridge regression')
score = RidgeModel.score(x_train_polylm, y_train)
print(score)


# In[58]:


x_test_polylm=polylm.fit_transform(x_test[['floors', 'waterfront','lat' ,'bedrooms' ,'sqft_basement' ,'view' ,'bathrooms','sqft_living15','sqft_above','grade','sqft_living']])

RidgeModel=Ridge(alpha=0.1)
RidgeModel.fit(x_test_polylm, y_test)
RidgeModel.score(x_test_polylm, y_test)

print('R^2 for second order polynomial transform the Testing data by fitting a Ridge regression')
score = RidgeModel.score(x_train_polylm, y_train)
print(score)


# In[59]:


import pandas as pd
import matplotlib.pyplot as plt

# Assuming 'data' is your DataFrame and 'column_name' is the column you want to plot
data['column_name'].plot.hist(bins=10)  # Adjust the number of bins as needed
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of Column')
plt.show()


# In[ ]:




