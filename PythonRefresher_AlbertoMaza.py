
# coding: utf-8

# In[12]:


import numpy as np
import matplotlib.pyplot as plt


# In[13]:


x = np.arange(0,np.pi*2,0.01)
function1 = np.sin(x) #sin function
function2 = np.cos(x)#cos function


# In[14]:


plt.plot(x,function1,x,function2)

plt.xlabel('0 to 2*pi')

plt.ylabel('sin(x) and cos(x)')

plt.title('Sin(x) and Cos(x) Plot')

plt.legend(['sin(x)','cos(x)'])

plt.show()

