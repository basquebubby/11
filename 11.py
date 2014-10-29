##########################################
#                                        #
#           100pt - Lab 11               # 
#                                        #
##########################################

# Make the ball "wrap" instead of bouncing - when it hits the right
# edge of the window, it should reappear at the left side and continue moving
# to the right. 

from Tkinter import *
root = Tk()
# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=0)

# Create the oval
circle = drawpad.create_oval(10, 10, 50, 50, fill='green')
square = drawpad.create_rectangle(10,60,50,80, fill='blue')
circledirection = 1
squaredirection = 1
# Create our animation function
def animate():
    global circledirection
    global squaredirection
    # Get the x and y co-ordinates of the circle
    x1, y1, x2, y2 = drawpad.coords(circle)
    a1, b1, a2, b2 = drawpad.coords(square)
    if x2 > drawpad.winfo_width(): 
        drawpad.move(circle,-drawpad.winfo_width(),0)
    elif x1 < 0:
        circledirection = circledirection
    if a2 > drawpad.winfo_width(): 
        drawpad.move(square,-drawpad.winfo_width(),0)
    elif a1 < 0:
        squaredirection = squaredirection
    #Move our oval object by the value of direction
    drawpad.move(circle,circledirection,0)
    drawpad.move(square,squaredirection,0)
    # Wait for 1 millisecond, then recursively call our animate function
    drawpad.after(1, animate)

# Kick off our animation
animate()
root.mainloop()