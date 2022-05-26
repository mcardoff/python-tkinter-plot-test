import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

def main():
    global root,canvas,toolbar,sel
    root = tkinter.Tk()
    root.wm_title("Embedding in Tk")

    fig = Figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)
    y1 = 2 * np.sin(2 * np.pi * t)
    y2 = 2 * np.cos(2 * np.pi * t)
    sel = 0
    
    plt = fig.add_subplot(111)

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    canvas.mpl_connect("key_press_event", on_key_press)
    button = tkinter.Button(master=root, text="Quit", command=lambda: _quit())
    button.pack(side=tkinter.BOTTOM)

    plot_button = tkinter.Button(master=root, text="Next Plot", command=(lambda: plots(plt,t,[y1,y2])))
    plot_button.pack(side=tkinter.BOTTOM)
    
    tkinter.mainloop()

def plots(plt,x,plots):
    global sel,canvas
    plt.clear() # clear what is there
    print("plotting {}".format(sel))
    plt.plot(x,plots[sel])
    if sel < len(plots)-1:
        sel += 1
    else:
        sel = 0
    canvas.draw()

def on_key_press(event):
    global canvas,toolbar
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)

def _quit():
    global root
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.

if __name__ == '__main__':
    main()
