#!/usr/bin/env python
# coding: utf-8

# # Дана функция f(x) = -8x^2+3x+17

# ## 1. Определяем корни 

# In[22]:


from sympy import *

x = Symbol('x')
func = -8*(x**2)+3*x+17
y = solve(func)
x1 = float(y[0])
x2 = float(y[1])

print(x1, x2)


# ## 2. Найти интервалы, на которых функция возрастает

# In[23]:


fd = diff(func)
print(solve(0<fd))


# ## 3. Найти интервалы, на которых функция убывает

# In[24]:


print(solve(0>fd))


# ## 4. Построить график

# In[25]:


import matplotlib.pyplot as plt
list_y = []
for i in range(-5, 6, ):
    x = i
    y = -8*(x**2)+3*x+17
    list_y.append(y)
    
plt.plot(range(-5, 6, ), list_y)

plt.plot(range(-5,6),[0,0,0,0,0,0,0,0,0,0,0])


# ## 5. Вычислить вершину

# In[26]:


corni = solve(fd)
top = corni[0]
x = top
y = -8*(x**2)+3*x+17
print(top, y)


# ## 6. Определить промежутки, на котором f > 0

# In[27]:


solve(0<func)


# ## 7. Определить промежутки, на котором f < 0

# In[28]:


solve(0>func)


# In[ ]:




