from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("1000x600")
root.title("Trabajando en el Canvas usando funciones")
canvas = Canvas(root,width=990,height=490,bg="white",highlightbackground="lightgray")

label = Label(root,text="Selecciona un Color")
fillcolor=["red","green","blue","black"]
color_dropdown = ttk.Combobox(root,state="readonly",values=fillcolor,width=10)

startx = Label(root,text="Inicio X")

coordinates_values=[10,50,100,200,300,400,500,600,700,800,900]
d1 = ttk.Combobox(root,state="readonly",values=coordinates_values,width=10)

starty = Label(root,text="Inicio Y")

d2 = ttk.Combobox(root,state="readonly",values=coordinates_values,width=10)

endx = Label(root,text="Final X")

d3 = ttk.Combobox(root,state="readonly",values=coordinates_values,width=10)

endy = Label(root,text="Final Y")

d4 = ttk.Combobox(root,state="readonly",values=coordinates_values,width=10)

def circle(event):
    oldx = d1.get()
    oldy = d2.get()
    newx = d3.get()
    newy = d4.get()
    keypress='c'
    draw(keypress,oldx,oldy,newx,newy)
    
def rectangle(event):
    oldx = d1.get()
    oldy = d2.get()
    newx = d3.get()
    newy = d4.get()
    keypress='r'
    draw(keypress,oldx,oldy,newx,newy)
    
def line(event):
    oldx = d1.get()
    oldy = d2.get()
    newx = d3.get()
    newy = d4.get()
    keypress='l'
    draw(keypress,oldx,oldy,newx,newy)
    
def draw(keypress,oldx,oldy,newx,newy):
    color = color_dropdown.get()
    if(keypress == "c"):
        draw_circle = canvas.create_oval(oldx,oldy,newx,newy, fill=color)
    
    if(keypress == "r"):
        draw_rectangle = canvas.create_rectangle(oldx,oldy,newx,newy, width = 3, fill=color)
        
    if(keypress == "l"):
        draw_line = canvas.create_line(oldx,oldy,newx,newy, width = 3, fill=color)
    
    
canvas.pack()
root.bind("<c>",circle)
root.bind("<r>",rectangle)
root.bind("<l>",line)

label.place(relx=0.6,rely=0.9,anchor=CENTER)
color_dropdown.place(relx=0.8,rely=0.9,anchor=CENTER)
startx.place(relx=0.1,rely=0.85,anchor=CENTER)
endx.place(relx=0.5,rely=0.85,anchor=CENTER)
starty.place(relx=0.3,rely=0.85,anchor=CENTER)
endy.place(relx=0.7,rely=0.85,anchor=CENTER)
d1.place(relx=0.2,rely=0.85,anchor=CENTER)
d2.place(relx=0.4,rely=0.85,anchor=CENTER)
d3.place(relx=0.6,rely=0.85,anchor=CENTER)
d4.place(relx=0.8,rely=0.85,anchor=CENTER)
canvas.pack()
root.mainloop()