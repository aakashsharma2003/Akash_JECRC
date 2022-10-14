import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as ttk

data=pd.read_csv(r'treadmil-users.csv')

app = ttk.Tk()
app.geometry('600x300')
app.title("Treadmil User Analysis")
#Radio Button

graphs = ttk.Variable(app)
values = {'Pair plot': 'sns.pairplot(data = data)', 'Joint plot': "sns.jointplot(data = data, x='{col1}', y='{col2}')",
          'Bar plot': "sns.barplot(data = data, x='{col1}', y='{col2}')"}
graphs.set(values['Pair plot'])
y = 10
for key, value in values.items():
    ttk.Radiobutton(app, text=key, variable=graphs,
                    value=value).place(x=10, y=y)
    y += 20
#Option Value 1
col1=ttk.Variable(app)
values=['Select']+list(data.columns)

col1.set(values[0])
ttk.OptionMenu(app, col1,*values).place(x=150,y=10)
ttk.Label(app,text='Column 1').place(x=150,y=40)

#Option Value 2
col2=ttk.Variable(app)
values=['Select']+list(data.columns)

col2.set(values[0])
ttk.OptionMenu(app, col2,*values).place(x=150,y=80)
ttk.Label(app,text='Column 2').place(x=150,y=110)

#Option Value 3
col3=ttk.Variable(app)
values=['Select']+list(data.columns)

col3.set(values[0])
ttk.OptionMenu(app, col3,*values).place(x=150,y=150)
ttk.Label(app,text='Column 3').place(x=150,y=180)
def show():
    #print(graphs.get())
    print(col1.get())
    print(col2.get())
    print(col3.get())


ttk.Button(app, text='show', command=show).place(x=400, y=20)

app.mainloop()
