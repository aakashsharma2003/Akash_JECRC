import tkinter as ttk
from unittest import result
from matplotlib.pyplot import box

from numpy import place
app=ttk.Tk()
app.title('My app')
app.geometry('600x400')

msg = ttk.Variable(app)
result=ttk.Variable(app)
print(msg.get())
msg.set('empty')
print(msg.get())




ttk.Label(app,text='A simple text label').place(x=100,y=100)
ttk.Label(app, textvariable=msg).place(x=100,y=70)
ttk.Entry(app, )




def abc(): 
    print('WOw')
    msg.set('jo tera maan kare')

ttk.Button(app,text='Click here', command= abc).place(x=100,y=40)
ttk.Button(app,text='YOu can clik here also', command= lambda:msg.set('pta nhi')).place(x=200,y=200)

f1 = ttk.Variable(app)
f1.set('0')
f2 =ttk.Variable(app)
f2.set('0')

ttk.Entry(app,textvariable=f1, font=('arial,22')).place(x=50,y=200)
ttk.Entry(app,textvariable=f2, font=('arial,22')).place(x=150,y=200)
ttk.Label(app, text='result').place(x=100,y=300)
ttk.Label(app, textvariable=result,font=('arial,22')).place(x=100,y=330)

def calci(op):
    print('i will calculate')
    result.set(eval(f1.get()+op+f2.get()))

ttk.Button(app, text = '+',command=lambda:calci('+'), font = ('arial',22)).\
    place(x=50,y=240)
ttk.Button(app, text = '-',command=lambda:calci('-'), font = ('arial',22)).\
    place(x=100,y=240)
ttk.Button(app, text = '*',command=lambda:calci('*'), font = ('arial',22)).\
    place(x=150,y=240)
ttk.Button(app, text = '/',command=lambda:calci('/'), font = ('arial',22)).\
    place(x=200,y=240)


box = ttk.Listbox(app, height=5, fg='red', activestyle='dotbox')
box.insert(1, 'semplel')
box.insert(2, 'semplel')
box.insert(3, 'semplel')
box.place(x=350 , y=40)


def show ():
    print(box.get(box.curselection()))


ttk.button(app)



app.mainloop()