#!/usr/bin/env python
# coding: utf-8

# In[33]:


a = " Everything is Everything "
b = " People who know more do more "
c = " Everything happens for a reason "
d = " Being embarrassed doesn't exist "

print("Want to know principles from 4 different situations?")

answer = input("Do you want to know? (yes/no): ").strip().lower()

if answer == "yes":
    print("Which situation?")
    print("1. Being embarrassed?")
    print("2. Bad things happening?")
    print("3. Bad decisions in life?")
    print("4. Being impatient with an ignorant person?")

    situation = input("Please enter the number corresponding to the situation: ").strip()

    if situation == "1":
        print(d)
        why_answer = input("Want to know why? (yes/no): ").strip().lower()
        if why_answer == "yes":
            print("You cannot be embarrassed by anything that you know already happened to someone else.")
    
    elif situation == "2":
        print(c)
        why_answer = input("Want to know why? (yes/no): ").strip().lower()
        if why_answer == "yes":
            print("Don't stress over situations we cannot control. In times of negativity is where we show our true colors.")
    
    elif situation == "3":
        print(a)
        why_answer = input("Want to know why? (yes/no): ").strip().lower()
        if why_answer == "yes":
            print("Our decisions reflect on our everyday life. A messy room means a messy life, Easy desisions Hard Life, Hard Decisions, easy life.")
    
    elif situation == "4":
        print(b)
        why_answer = input("Want to know why? (yes/no): ").strip().lower()
        if why_answer == "yes":
            print("Never get frustrated over someone who's ignorant to anything. It's your job to do more to help them learn from the situation. Then they will pass it on to the next individual.")
else:
    print("Oh well, just so you know, wisdom doesn't come with age.")


# In[ ]:




