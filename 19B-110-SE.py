#!/usr/bin/env python
# coding: utf-8

# # 1

# In[1]:


def Multiple(number):
    count = 0
    for i in range(1,number):
        if i%5==0 or i%3==0:
            count =count+i
    return count
    
print(Multiple(1000))


# # 2

# In[2]:


def InWords(num):
    start_digits = ["Zero", "One", "Two", "Three", "Four","Five", "Six", "Seven", "Eight", "Nine"]
    up = ["", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    mults = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    high = ["hundred", "thousand"]
    
    if num>=10000:
        return "Numbers greater than 10000 is not supported"
    if num<10:
        a= start_digits[num]
        return a
    if num<20:
        a=up[num-9]
        return a
    if num<100:
        st = str(num)
        a = str()
        if int(st[1:2])!=0:
            return (mults[int(st[:1])])+" "+(start_digits[int(st[1:2])])
        else:
            return (mults[int(st[:1])])    
    if num<1000:
        st = str(num)
        if (int(st[1:]))==0:
            return (start_digits[int(st[:1])])+" "+high[0]
        else:
            return start_digits[int(st[:1])]+" "+high[0]+" and "+InWords(int(st[1:]))
    if num<10000:
        st = str(num)
        if (int(st[1:]))==0:
            return (start_digits[int(st[:1])])+" "+high[1]
        else:
            return (start_digits[int(st[:1])])+" "+high[1]+" "+InWords(int(st[1:]))
    
print(InWords(9999))


# # 3

# In[3]:


def SplitAndJoint(abc):
    x = ""
    abc = abc.split()
    l=len(abc)
    for i in range(l):
        x =x+abc[i]
        if i < (len(abc)-1):
            x += "-"
    return x

print(SplitAndJoint("The process in which large food particle breaks down into small food particle is called digestion."))


# # 4

# In[4]:


def LongestWord(abc):
    puncs = "!\"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"
    abc = abc.split()
    x = []
    a = []
    for i in abc:
        for ii in i:  
            if ii in puncs:  
                i = i.replace(ii, "")
        x.append(i)
    for abc in x:
        l=len(abc)
        a.append(l)
        final=x[a.index(max(a))]
    return "Word is: "+final

print(LongestWord("the& nature"))


# # 5

# In[5]:


def RunnerUp(score):
    a = max(score)
    print("Winner score is: ",a)
    score.sort()
    for i in score:
        if i == a:
            score.remove(i)     
            print("Runner up score is: ",max(score))
    
print(RunnerUp([42,33,60,55,97,100]))

