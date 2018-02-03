
# coding: utf-8

# In[1]:


import pandas
movies = pandas.read_csv("fandango_score_comparison.csv")


# In[2]:


import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

plt.hist(movies["Fandango_Stars"])


# In[4]:


import numpy

fandango_mean = movies["Fandango_Stars"].mean()
metacritic_mean = movies["Metacritic_norm_round"].mean()
fandango_std = movies["Fandango_Stars"].std()
metacritic_std = movies["Metacritic_norm_round"].std()
fandango_median = movies["Fandango_Stars"].median()
metacritic_median = movies["Metacritic_norm_round"].median()

print(fandango_mean)
print(metacritic_mean)
print(fandango_std)
print(metacritic_std)
print(fandango_median)
print(metacritic_median)


# In[5]:


movies["diff"] = numpy.abs(movies["Metacritic_norm_round"] - movies["Fandango_Stars"]) 


# In[7]:


movies.sort_values(by = "diff").head(5)


# In[9]:


from scipy.stats import linregress 

slope, intercept, r_value, p_value, stderr_slope = linregress(movies["Metacritic_norm_round"], movies["Fandango_Stars"])
r_value


# In[10]:


predicted = 3 * slope + intercept
predicted


# In[11]:


pred_1 = 1 * slope + intercept
pred_5 = 5 * slope + intercept
plt.scatter(movies["Metacritic_norm_round"], movies["Fandango_Stars"])
plt.plot([1,5],[pred_1,pred_5])
plt.xlim(1,5)
plt.show()

