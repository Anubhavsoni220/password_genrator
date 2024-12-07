#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import string   
import random
import pyperclip  #to use cop and paste(file attachment managment) method

def generator():
    
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_characters
    password_length=int(length_Box.get())

    
    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))
    
    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))  
    
    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))


     # password=random.sample(all,password_length)
    # passwordField,insert(0,password)

def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)
    

root=Tk()
root.config(bg='#D3D3D3')
root.geometry("310x420")
choice=IntVar()
Font=('arial',13,'bold')

passwordLabel=Label(root,text= 'Password Generator ',font=('times new roman',25,'bold'),bg='#FF6F61',fg='white')
passwordLabel.grid(pady=15) # grid method helps in adding the value on window.
strongradioButton=Radiobutton(root,text='Hard',value=3,variable=choice,font=Font)
strongradioButton.grid(pady=8)
mediumradioButton=Radiobutton(root,text='Medium',value=2,variable=choice,font=Font) 
mediumradioButton.grid(pady=8)
weakradioButton=Radiobutton(root,text='Easy',value=1,variable=choice,font=Font)
weakradioButton.grid(pady=8)



lengthLabel=Label(root,text='Password Length',font=Font,fg='violet')
lengthLabel.grid(pady=8)

length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_Box.grid(pady=8)

generateButton=Button(root,text='Generate',font=Font,command=generator)
generateButton.grid(pady=8)

passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.grid(pady=8)

copyButton=Button(root,text='Copy',font=Font,command=copy)
copyButton.grid(pady=8)

root.mainloop()


# In[ ]:





# In[ ]:




