#!/usr/bin/env python
# coding: utf-8

# # Q.1

# In Python, an empty dictionary can be represented by a pair of curly braces with nothing inside, like this:

# In[1]:


{}


# This is the syntax for creating an empty dictionary literal. Alternatively, you can also use the dict() constructor without any arguments to create an empty dictionary:

# In[2]:


dict()


# # Q.2

# The value of a dictionary with the key 'foo' and the value 42 would be 42. In Python, dictionaries are composed of key-value pairs, where each key is associated with a corresponding value. In this case, the key 'foo' is associated with the value 42. You can access the value by using the key as the index of the dictionary

# In[3]:


my_dict = {'foo': 42}
value = my_dict['foo']
print(value)  # Output: 42


# The variable value will store the value 42, which is the value associated with the key 'foo' in the dictionary my_dict.

# # Q.3

# The most significant distinction between a dictionary and a list in Python is the way they store and access elements:
# 
# 1. Structure:
#    - A list is an ordered collection of elements where each element is identified by its position or index. Lists are defined using square brackets (`[]`) and elements are separated by commas.
#    - A dictionary is an unordered collection of key-value pairs, where each element is identified by a unique key. Dictionaries are defined using curly braces (`{}`), and each key-value pair is separated by a colon (`:`). The keys within a dictionary must be unique.
# 
# 2. Accessing Elements:
#    - List elements are accessed by their index, starting from 0. You can use square bracket notation to access elements, e.g., `my_list[0]`.
#    - Dictionary elements are accessed by their keys. You can use square bracket notation with the key to access the corresponding value, e.g., `my_dict['key']`.
# 
# 3. Order:
#    - Lists maintain the order of elements, which means the position/index of each element is preserved.
#    - Dictionaries do not guarantee any specific order of elements. The key-value pairs are stored in an unordered manner.
# 
# 4. Mutability:
#    - Lists are mutable, meaning you can modify, add, or remove elements after the list is created.
#    - Dictionaries are also mutable, allowing you to modify, add, or remove key-value pairs.
# 
# 5. Use Cases:
#    - Lists are commonly used for sequences of elements where the order matters, such as a collection of numbers, strings, or objects.
#    - Dictionaries are useful when you need to associate values with specific keys, such as storing settings, mapping relationships, or representing real-world entities.
# 
# It's important to choose the appropriate data structure based on the specific requirements of your program and the nature of the data you are working with.

# # Q.4

# If you try to access spam['foo'] where spam is {'bar': 100}, you will encounter a KeyError.
# 
# In Python, when you attempt to access a key in a dictionary that does not exist, such as 'foo' in this case, a KeyError is raised. This error occurs because the key 'foo' is not present in the dictionary spam.
# 
# Here's an example of what happens:

# In[4]:


spam = {'bar': 100}
value = spam['foo']  # Raises KeyError: 'foo'


# When executing this code, it will raise a KeyError with the message 'foo'. To avoid this error, you should ensure that the key you are trying to access actually exists in the dictionary.

# # Q.5

# The expressions 'cat' in spam and 'cat' in spam.keys() essentially check for the presence of the key 'cat' in the dictionary spam, but there is a slight difference in their behavior.
# 
# 'cat' in spam:
# 
# This expression checks whether the key 'cat' exists in the dictionary spam. It returns a boolean value (True or False) indicating whether the key is present as a direct key in the dictionary.
# If 'cat' is a key in spam, it will return True. Otherwise, it will return False.
# Example:

# In[5]:


spam = {'cat': 42}
print('cat' in spam)  


# 'cat' in spam.keys():
# 
# This expression checks whether the key 'cat' exists in the dictionary spam.keys(), which is a view object representing the keys of the dictionary.
# It behaves similarly to 'cat' in spam but explicitly operates on the keys of the dictionary rather than the dictionary itself.
# If 'cat' is a key in spam, it will return True. Otherwise, it will return False.
# Example:

# In[6]:


spam = {'cat': 42}
print('cat' in spam.keys()) 


# In most cases, the results of both expressions will be the same. However, the second expression explicitly checks the keys of the dictionary, which can be useful when you want to specifically focus on the keys without referencing the dictionary as a whole.

# # Q.6

# The expressions 'cat' in spam and 'cat' in spam.values() have different meanings and behavior:
# 
# 'cat' in spam:
# 
# This expression checks whether the key 'cat' exists in the dictionary spam. It returns a boolean value (True or False) indicating whether the key is present in the dictionary as a direct key.
# It checks if 'cat' is a key in spam.
# Example:

# In[8]:


spam = {'cat': 42}
print('cat' in spam)  


# 'cat' in spam.values():
# 
# This expression checks whether the value 'cat' exists in the dictionary spam. It returns a boolean value (True or False) indicating whether the value is present in any of the dictionary's values.
# It checks if 'cat' is a value in spam.
# Example:

# In[9]:


spam = {'key1': 'cat', 'key2': 'dog'}
print('cat' in spam.values())  


# In summary, 'cat' in spam checks if 'cat' is a key in the dictionary spam, while 'cat' in spam.values() checks if 'cat' is a value in the dictionary spam. These expressions operate on different aspects of the dictionary and provide different results based on whether the given key or value is present in the dictionary.

# # Q.7

# A shortcut for the given code can be achieved using the dict.setdefault() method. It allows you to set a default value for a key in a dictionary if the key does not already exist. Here's how it can be used as a shortcut:

# In[11]:


spam.setdefault('color', 'black')


# This code is equivalent to the original code you provided. It checks if the key 'color' is present in the spam dictionary. If the key is not found, it adds the key-value pair 'color': 'black' to the dictionary. If the key already exists, it does not modify the existing value.
# 
# Using setdefault() provides a concise way to achieve the same result as the if statement followed by assignment.

# # Q.8

# To "pretty print" dictionary values in Python, you can use the pprint module, specifically the pprint function. The pprint module provides a way to display data structures in a well-formatted and readable manner. Here's how you can use it to pretty print dictionary values:

# In[12]:


import pprint

my_dict = {'foo': 42, 'bar': [1, 2, 3], 'baz': {'a': 1, 'b': 2}}
pprint.pprint(my_dict)


# The pprint.pprint() function takes a Python object, such as a dictionary, and displays it in a way that is easy to read. It will automatically format the output with indentation and line breaks to make the structure of the dictionary clearer.
# 
# By using pprint instead of the regular print function, you can obtain a more visually appealing representation of complex data structures like dictionaries.

# In[ ]:




