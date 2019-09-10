
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


###Add tan function

function3 = np.tan(x)
plt.plot(x,function1,x,function2, x, function3)
plt.xlabel('0 to 2*pi')

plt.ylabel('sin(x), cos(x) & tan(x)')

plt.title('Sin(x), Cos(x) and Tan(x) Plot')

plt.legend(['sin(x)','cos(x)','tan(x)'])
plt.show()
