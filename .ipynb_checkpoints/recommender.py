import tkinter as ttk



app = ttk.Tk()
app.title('recommendation system')
app.geometry('400x400')


result = ttk.Variable(app)
box = ttk. Listbox(app, height=10)
box.place(x=10,y=10)
 

def get_movies():
    pass

ttk.Button(app, text='find recommendation', font=('Arial',22) ,command=get_movies).\
    place(x=200,y=50)

ttk.Label(app, textvariable=result,font=('Arial',22)).\
    place(x=200,y=100)


app.mainloop()