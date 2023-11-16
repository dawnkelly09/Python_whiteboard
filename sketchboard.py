# Built along with tutorial at freeCodeCamp.org
# https://www.freecodecamp.org/news/build-a-whiteboard-app/
# Thank you, Juan Romano!

import tkinter as tk
from tkinter.colorchooser import askcolor

#############################################
# Functions to handle drawing on the canvas #
#############################################

# function: once assigned to click event, will set is_drawing to True and capture mouse position at beginning of drawing action
def start_drawing(event):
    # these are available anywhere in this file
    global is_drawing, prev_x, prev_y
    # signals start of drawing
    is_drawing = True
    # captures current mouse position (start point of drawing)
    prev_x, prev_y = event.x, event.y
    
# function: if is_drawing is True set these attributes for 
# each vector point of the line that will be drawn
def draw(event):
    global is_drawing, prev_x, prev_y
    # if is_drawing is True, set appearance attributes for 
    # each vector point of the line that will be drawn
    if is_drawing:
        current_x, current_y = event.x, event.y
        canvas.create_line(
            prev_x, prev_y, current_x, current_y,
            fill=drawing_color,
            width=line_width,
            capstyle=tk.ROUND,
            smooth=tk.TRUE,
        )
        prev_x, prev_y = current_x, current_y
        
# function to handle end of drawing action
def stop_drawing(event):
    global is_drawing
    is_drawing = False
    
# function to handle changing the line color
def change_pen_color():
    global drawing_color
    # calls the askcolor module from tkinter
    color = askcolor()[1]
    # if a color is selected, set the drawing_color to that color
    if color:
        drawing_color = color

# function to handle changing the line width
def change_line_width(value):
    global line_width
    line_width = int(value)
    
########################################
# Functions to add text to the canvas #
#######################################



    
##########################
# Build GUI with tkinter #
##########################

# create window with title and white canvas

# creates main application window: serves as container for graphical elements of application
root = tk.Tk()
# sets the title displayed in title bar of the window
root.title("Sketchboard")

# creates drawing canvase in the root app window with white background
canvas = tk.Canvas(root, bg="white")
# drawing canvas will fill the window
canvas.pack(fill="both", expand=True)

# initialize drawing attributes
is_drawing = False
drawing_color = "black"
line_width = 2

# sets initial size of application window in pixels
root.geometry("800x600")

# build navbar and controls

# frame to hold buttons/controls
controls_frame = tk.Frame(root)
controls_frame.pack(side="top", fill="x")
# create 2 buttons to change color and clear canvas
color_button = tk.Button(controls_frame, text="Change Color", command=change_pen_color)
clear_button = tk.Button(controls_frame, text="Clear Canvas", command=lambda: canvas.delete("all"))
# assign buttons to control frame
color_button.pack(side="left", padx=5, pady=5)
clear_button.pack(side="left", padx=5, pady=5)

# create & place label and slider for line width

# create label widget to display text
line_width_label = tk.Label(controls_frame, text="Line Width:")
# placement within the control frame
line_width_label.pack(side="left", padx=5, pady=5)

# create horizontal slider widget to change line width
line_width_slider = tk.Scale(controls_frame, from_=1, to=10, orient="horizontal", command=lambda val: change_line_width(val))
# intial value of slider
line_width_slider.set(line_width)
# assign slider to control frame
line_width_slider.pack(side="left", padx=5, pady=5)

# create bindings to assign functions to UI elements/events

# left mouse button click triggers start_drawing function
canvas.bind("<Button-1>", start_drawing)
# left mouse button drag triggers draw function
canvas.bind("<B1-Motion>", draw)
# left mouse button release triggers stop_drawing function
canvas.bind("<ButtonRelease-1>", stop_drawing)

# instantiate Text class to add text to canvas
text_widget_label = tk.Label(controls_frame, text="Notes:")
text_widget_label.pack(side="top", padx=5, pady=5)
text_widget = tk.Text(controls_frame, height=6, width=120)
text_widget.pack(side="left", padx=5, pady=5)

# starts main loop of application
root.mainloop()





    