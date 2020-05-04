import tkinter
import main

root = tkinter.Tk()
root.title('Sudoku Config')
diffuculty = tkinter.IntVar()
diffuculty.set(3)
diff = tkinter.Spinbox(root, from_=1, to=10, width=5, textvariable=diffuculty)
diff.grid(column=0,row=0)
dl = tkinter.Label(text='<-- Difficulty (Harder=Longer loading!)')
dl.grid(column=1, row=0)
one = tkinter.Label(root, text='Click- Select A Box')
two = tkinter.Label(root, text='Numbers- Enter A Number Into The Box')
three = tkinter.Label(root, text='Enter- "Lock in" a number, will check if it intercepts anything, counts towards total moves')
four = tkinter.Label(root, text='Backspace- Deletes a number, locked in or not, form a box')
five = tkinter.Label(root, text='Escape- Deselects a box')
six = tkinter.Label(root, text='Space, solves the puzzle for you')

rules = [one, two, three, four, five, six]

for i in range(5):
    rules[i].grid(column=2,row=i)

start = tkinter.Button(text='Start Game', command= lambda: main.run(diffuculty.get()))
start.grid(column=0, row=1)
root.mainloop()