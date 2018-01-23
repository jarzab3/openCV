import tkinter as tk
import cv2
from PIL import Image, ImageTk


width, height = 600, 400
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = tk.Tk()
root.bind('<Escape>', lambda e: root.quit())
lmain = tk.Label(root)
lmain.pack()



# root = tk.Tk()
# frame = tk.Frame(root)
# frame.pack()


def write_slogan():
    print("Tkinter is easy to use!")


button = tk.Button(root,
                   text="QUIT",
                   fg="red",
                   command=quit)

button.pack(side=tk.LEFT)

slogan = tk.Button(root,
                   text="Hello",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

# root.mainloop()



def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)



show_frame()
root.mainloop()