from tkinter import *

window = Tk()
window.title("Tableau XML parser")
window.geometry('500x400')
lbl = Label(window, text='Choose Tableau workbook XML file:')
lbl.grid(column=100, row=50)
btn = Button(window, text='Open')
btn.grid(column=110, row=50)
window.mainloop()

################################################

# * add file select buttone
# * allow to select multiple files (file queue)
# * position buttons 
# * add select output folder button
# * create an executable
# * change favicon