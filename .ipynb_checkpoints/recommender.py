from numpy import place
import tkinter as ttk
import pandas as pd
import warnings
import os
warnings.filterwarnings('ignore')
print('Location is:',os.getcwd(),'\n\n\n')

app = ttk.Tk()
app.title('Movie Recommendation')
app.geometry('700x700')

cols = ['user_id', 'movie_id', 'rating', 'ts']
df = pd.read_csv('u.data', sep='\t', names=cols).drop('ts', axis=1)
item_cols = ['movie_id', 'title'] + [str(i) for i in range(22)]
df1 = pd.read_csv('u.item', sep='|', names=item_cols,
                  encoding="ISO-8859-1")[['movie_id', 'title']]
movie = pd.merge(df, df1, on='movie_id')

ttk.Label(app, text='Movie Recommendation',
          font=('Algerian', 18)). place(x=300, y=10)
result = ttk.Variable(app)

box = ttk.Listbox(app, height=15 , width = 40)
for row, val  in movie. iterrows():
    box.insert(row+1 , val['title'])

box.place(x=10, y=10)


def get_movie():
    pass


ttk.Button(app, text='Find recommendation', command=get_movie(),
           font=('Arial', 22)).place(x=50, y=260)
ttk.Label(app, textvariable=result, font=('arial', 22)).place(x=200, y=200)


app.mainloop()