from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)
drawpad.create_rectangle((300,100,500,460),fill = "darkblue", outline = "black")
drawpad.create_polygon((250,40,300,100,300,460,250,400), fill = "darkblue", outline = "black")
drawpad.create_polygon((250,40,300,100,370,10), fill = "darkblue", outline = "black")
drawpad.create_polygon((370,10,300,100,500,100), fill = "darkblue", outline = "black")
drawpad.create_polygon((450,40,500,100,370,10), fill = "darkblue", outline = "black")
drawpad.create_rectangle((310,120,590,150), fill = "white", outline = "grey")
drawpad.create_polygon(())
root.mainloop()