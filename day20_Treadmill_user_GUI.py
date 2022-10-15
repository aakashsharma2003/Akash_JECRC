import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as ttk
from PIL import ImageTk, Image

data = pd.read_csv(r'treadmil-users.csv')

app = ttk.Tk()
app.geometry('600x300')
app.title("Treadmil User Analysis")
# Radio Button

graphs = ttk.Variable(app)
values = {'Pair plot': 'sns.pairplot(data = data)', 'Joint plot': "sns.jointplot(data = data, x='{col1}', y='{col2}')",
          'Bar plot': "sns.barplot(data = data, x='{col1}', y='{col2}')",
          'Box plot': "sns.boxplot(data = data, x='{col1}', y='{col2}')"}
graphs.set(values['Pair plot'])
y = 10
for key, value in values.items():
    ttk.Radiobutton(app, text=key, variable=graphs,
                    value=value).place(x=10, y=y)
    y += 20
# Option Value 1
col1 = ttk.Variable(app)
values = ['Select']+list(data.columns)

col1.set(values[0])
ttk.Label(app, text='Column 1').place(x=150, y=40)
ttk.OptionMenu(app, col1, *values).place(x=150, y=10)


# Option Value 2
col2 = ttk.Variable(app)
values = ['Select']+list(data.columns)

col2.set(values[0])
ttk.Label(app, text='Column 2').place(x=150, y=110)
ttk.OptionMenu(app, col2, *values).place(x=150, y=80)


# Option Value 3
col3 = ttk.Variable(app)
values = ['Select']+list(data.columns)

col3.set(values[0])
ttk.Label(app, text='Column 3').place(x=150, y=180)
ttk.OptionMenu(app, col3, *values).place(x=150, y=150)


# canvas

cnv = ttk.Canvas(app, width=250, height=200)
cnv.place(x=300, y=60)

# result
result = ttk.Variable(app)
ttk.Label(app, textvariable=result).place(x=300, y=300)


def show():
    global img
    global cnv
    column1 = col1.get()
    column2 = col2.get()
    column3 = col3.get()

    # print(graphs.get())
    # print(col1.get())
    # print(col2.get())
    # print(col3.get())
    g = graphs.get()
    if 'col1' in g:
        if column1 == 'Select':
            result.set('column1 must be selected')
            return
    if 'col2' in g:
        if column2 == 'Select':
            result.set('column 2 must be selected')
            return
    if 'col3' in g:
        if column3 == 'Select':
            result.set('column 3 ,must be selecetd')
            return

    fig = plt.figure(figsize=(5, 2))
    eval(g.format(col1=column1, col2=column2, col3=column3))
    # plt.show()
    fig, plt.savefig('graph.png')
    img = ImageTk.PhotoImage(Image.open('graph.png').resize((250, 200)))

    cnv.create_image(0, 0, anchor=ttk.NW, image=img)
    result.set('success')


ttk.Button(app, text='show', command=show).place(x=400, y=20)

app.mainloop()