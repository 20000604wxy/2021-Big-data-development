from ui import workspace,display,show_result
from tkinter import *

root1 = Tk()
root2 = Tk()
input=workspace(root1)
display(root2)
root1.mainloop()
root2.mainloop()
root3=Tk()
show_result(root3,input)
root3.mainloop()