
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt


# In[11]:


x = np.arange(0,np.pi*2,0.01)
function1 = np.sin(x)
function2 = np.cos(x)


# In[17]:


plt.plot(x,function1,x,function2)
plt.xlabel('0 to 2*pi')
plt.ylabel('sin(x) and cos(x)')
plt.title('Sin(x) and Cos(x) Plot')
plt.legend(['sin(x)','cos(x)'])
plt.show()

