from tkinter import *

def pressed_button():
    print('I pressed the button!')

app = Tk()
app.title('Button Test')
app.geometry('300x100+200+100')

b = Button(app, text = 'Press me', width = 10, command = pressed_button)
b.pack (side = 'top', padx = 10, pady = 10)

app.mainloop()