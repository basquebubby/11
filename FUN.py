##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!
drawpad.create_rectangle((0,0,850,450),fill = "lightblue", outline = "black")
drawpad.create_rectangle((0,450,800,600), fill = "darkgreen")#Grass
drawpad.create_polygon((460,60,580,60,620,100,490,100), fill = "orange", outline = "black")
drawpad.create_polygon((490,100,620,100,620,250,490,250), fill = "orange", outline = "black")
drawpad.create_polygon((490,250,460,150,460,60,490,100), fill = "orange", outline = "black")
drawpad.create_rectangle((100,600,700,300), fill = "red") #Creates house body
drawpad.create_polygon((490,70,510,90,580,90,560,70), fill = "darkgrey", outline = "black")
drawpad.create_line(560,70,560,90)
drawpad.create_polygon((50,200,100,300,100,600,50,500), fill = "red")#House side
drawpad.create_polygon((100, 300, 400, 100, 700, 300), fill = "blue", outline = "black") #Creates roof
drawpad.create_polygon((400,100,50,200,100,300), fill = "blue", outline = "black")
drawpad.create_rectangle((300,600,500,400), fill = "yellow") #Makes door
drawpad.create_oval((440,500,470,530), fill = "black") #Makes door knob
drawpad.create_rectangle((150,450,250,550), fill = "lightgray", outline = "black")
drawpad.create_rectangle((550,450,650,550), fill = "lightgray", outline = "black")
root.mainloop()