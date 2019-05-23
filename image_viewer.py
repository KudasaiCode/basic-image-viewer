from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as ms
import PIL
from PIL import Image, ImageTk 

# main class
class application: 
    def __init__(self, master):
        self.master = master
        self.c_size = (700, 500)
        self.setup_gui(self.c_size)
        self.img = None

    def setup_gui(self, s):
        Label(self.master, text = 'Image Viewer', pady = 5, 
              bg = 'white', font = ('', 15)).pack()
        self.canvas = Canvas(self.master, height = s[1], width = s[0], 
                             bd=10, bg = 'black', relief = 'flat')
        self.canvas.pack()
        txt = "No Image"

        self.wt = self.canvas.create_text(s[0]/2, s[1]/2, text = txt, 
                                          font = ('',20), fill = 'white')
        f = Frame(self.master, bg = 'white', padx=5, pady=5)
        Button(f, text = "Open New Image", bd = 2, fg = 'black', bg = 'white', 
               font = ('', 15), command = self.make_image).pack(side = BOTTOM)
        f.pack()

        self.status = Label(self.master, text = 'Current Image: None', bg = 'gray', font = ('', 15), 
                            relief = 'sunken', bd = 2, fg = 'black', anchor = W)
        self.status.pack(side = BOTTOM, fill = X)

    def make_image(self):
        try: 
            File = fd.askopenfilename()
            self.pilImage = Image.open(File)
            re = self.pilImage.resize((700,500), Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(re)
            self.canvas.delete(ALL)
            self.canvas.create_image(self.c_size[0]/2+10, self.c_size[1]/2, 
                                     anchor = CENTER, image=self.img)
            self.status['text'] = 'Current Image: ' + File
        except:
            ms.showerror('Error', 'File type is unsupported.')


root = Tk()
root.title('Image Viewer')
root.resizable(0,0)
application(root)
root.mainloop()





