
# coding: utf-8

# In[3]:

import random

x = []
#test case: 
def random_test():
        l = random.sample(range(0, 100000), 1)   
        return l

def sorted_test():
        l = random.sample(range(0, 100000), 1)
        return sorted(l)

def reverse_sorted_test():
        l = random.sample(range(0, 100000),1)  
        return list(reversed(l))


def test_case():
    l = random.sample(range(0, 100000), 200)   
    return sorted(l)

def test_case2():
    l = random.sample(range(0, 100000), 200)   
    return list(reversed(l))


# In[4]:


def test_set_best_case():
    #First test case: len = 50
    w1 = []
    i = 1
    while ( i <= 10):
        w1.append(i);
        i += 1;
        
     #First test case: len = 50
    w2 = []
    i = 1
    while ( i <= 20):
        w2.append(i);
        i += 1;
    
    
    #First test case: len = 50
    w3 = []
    i = 1
    while ( i <= 50):
        w3.append(i);
        i += 1;
    
    
    #First test case: len = 50
    w4 = []
    i = 1
    while ( i <= 100):
        w4.append(i);
        i += 1;
    
    #First test case: len = 50
    w5 = []
    i = 0
    while ( i <= 150):
        w5.append(i);
        i += 1;
    
    #First test case: len = 50
    w6 = []
    i = 1
    while ( i <= 200):
        w6.append(i);
        i += 1;
    
    #First test case: len = 50
    w7 = []
    i = 1
    while ( i <= 250):
        w7.append(i);
        i += 1;
    
    #First test case: len = 50
    w8 = []
    i = 1
    while ( i <= 300):
        w8.append(i);
        i += 1;
        
    array = [w1,w2,w3,w4,w5,w6,w7,w8]
    return array


# In[5]:


def test_set_worst_case():
    #First test case: len = 50
    w1 = []
    i = 10
    while ( i > 0):
        w1.append(i);
        i -= 1;
        
     #First test case: len = 50
    w2 = []
    i = 20
    while ( i > 0):
        w2.append(i);
        i -= 1;
    
    
    #First test case: len = 50
    w3 = []
    i = 50
    while ( i > 0):
        w3.append(i);
        i -= 1;
    
    
    #First test case: len = 50
    w4 = []
    i = 100
    while ( i > 0):
        w4.append(i);
        i -= 1;
    
    #First test case: len = 50
    w5 = []
    i = 150
    while ( i > 0):
        w5.append(i);
        i -= 1;
    
    #First test case: len = 50
    w6 = []
    i = 200
    while ( i > 0):
        w6.append(i);
        i -= 1;
    
    #First test case: len = 50
    w7 = []
    i = 250
    while ( i > 0):
        w7.append(i);
        i -= 1;
    
    #First test case: len = 50
    w8 = []
    i = 300
    while ( i > 0):
        w8.append(i);
        i -= 1;
        
    array = [w1,w2,w3,w4,w5,w6,w7,w8]
    return array

def test_cases_init():
    ranges = [10,20,50,100,150,200,250,300]
    presorted = []
    reversedsorted = []
    random_ = []

    for r in ranges:
        i = 1
        arr = []
        while (i <= r):
            arr.append(i)
            i +=1
        presorted.append(arr)
        reversedsorted.append(arr[::-1])
        random_.append(list(random.sample(range(0, r), r) ))

    return presorted, reversedsorted, random_

def bestcase_bucket():
    w1 = []
    i = 1
    while ( i <= 10):
        w1.append(i);
        i += 1;
    w2 = []
    i = 1
    while ( i <= 20):
        w2.append(i);
        i += 1;
    w3 = []
    i = 1
    while ( i <= 30):
        w3.append(i);
        i += 1;
    w4 = []
    i = 1
    while ( i <= 40):
        w4.append(i);
        i += 1;
    w5 = []
    i = 1
    while ( i <= 50):
        w5.append(i);
        i += 1;
    w6 = []
    i = 1
    while ( i <= 60):
        w6.append(i);
        i += 1;
    w7 = []
    i = 1
    while ( i <= 70):
        w7.append(i);
        i += 1;
    w8 = []
    i = 1
    while ( i <= 80):
        w8.append(i);
        i += 1;
    w9 = []
    i = 1
    while ( i <= 90):
        w9.append(i);
        i += 1;
    w10 = []
    i = 1
    while ( i <= 100):
        w10.append(i);
        i += 1;
    w_final = [w1,w3,w4,w5,w6,w7,w8,w9,w10]    
    return w_final

def consecutive_test():
    w1 = []
    i = 1
    while ( i <= 5000):
        w1.append(i);
        j = 0
        while (j <= 100):
            w1.append(random.randint(0, 1000));
            j += 1
        i += 1;
    return w1;
