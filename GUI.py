import Prediction as pr
from mttkinter import mtTkinter as tk
import wx
from PIL import ImageTk, Image
from tkinter import messagebox


CANVAS_SIZE = 400


# A function that loads the selected image and gives the prediction result
def load_and_predict():
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', style=style)
    if dialog.ShowModal() == wx.ID_OK:
        filepath = dialog.GetPath()
    else:
        filepath = None
    dialog.Destroy()
    img = Image.open(filepath)
    width, height = img.size
    scale = width / height
    if scale > 0:
        height = CANVAS_SIZE / scale
    else:
        height = CANVAS_SIZE * scale
    img = ImageTk.PhotoImage(img.resize((CANVAS_SIZE, round(height))))
    canv.create_image(CANVAS_SIZE/2, CANVAS_SIZE/2, image=img)
    if round(pr.predict(filepath)) == 1:
        messagebox.showinfo("Prediction", "This is a dog.")
    else:
        messagebox.showinfo("Prediction", "This is a cat.")


# Creating the main window
window = tk.Tk()
window.geometry("600x600")
window.resizable(0, 0)
window.title("Recognizing Dogs And Cats")
window.configure(background='#94fffb')
load_image_button = tk.Button(window, text="Load The Image And See The Prediction!", command=load_and_predict, width=40,
                              background='#33ff3a')
load_image_button.place(relx=0.5, rely=0.075, anchor='center')
canv = tk.Canvas(window, width=CANVAS_SIZE, height=CANVAS_SIZE, bg='white')
canv.place(relx=0.5, rely=0.5, anchor='center')
exit_button = tk.Button(window, text="Exit", command=exit, width=20, background='#fa2d2d')
exit_button.place(relx=0.5, rely=0.925, anchor='center')
tk.mainloop()
