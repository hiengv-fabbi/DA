from tkinter import *
from tkinter import filedialog
import os
import cv2
from matplotlib import pyplot as plt

root = Tk()

# root.withdraw()

def featurequery():
    os.system('Run.py')

label = Label(root, text="Chọn ảnh cần tìm kiếm:")
label.grid(row=5,column=0)

# query = filedialog.askopenfilename()
# query.grid(row=1,column=0)
button = Button(root, text="Find",command=featurequery)
button.grid(row=6,column=0) 


# print (imagelist)


root.mainloop()