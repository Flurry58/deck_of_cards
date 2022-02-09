import tkinter
from tkinter import *
from PIL import Image, ImageTk
from pil_resize_aspect_ratio import Resizer, FillType

#position is in tuple format
#ex use of addimage func:
#                x  y
#addimage("9S", (10,10))
class mainpage(Frame):
  def __init__(self,master=None):
    self.labellist = []
    Frame.__init__(self, master) 
    self.master = master
    self.pack(fill=BOTH, expand=1)
    
  def setloc(self,index,x,y):
    r = self.labellist[index].grid_location(x,y)
    
   #clear screen
  def clear(self):
    for i in range(len(self.labellist)):
      self.labellist[i].destroy()
    self.labellist = []
      
    #remove specific image by index

  def addimage(self, cardname, position):
  # Create a photoimage object of the image in the path
    cardname += ".png"
    desired_size = 100
    cardname = "cards/" + cardname
    im = Image.open(cardname)
    old_size = im.size  

    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])

    im = im.resize(new_size, Image.ANTIALIAS)

    new_im = Image.new("RGB", (desired_size, desired_size))
    new_im.paste(im, ((desired_size-new_size[0])//2,(desired_size-new_size[1])//2))
    test = ImageTk.PhotoImage(new_im)

    self.label1 = tkinter.Label(win,image=test)
    self.label1.image = test
    self.label1.place(x=position[0],y=position[1])
    self.labellist.append(self.label1)
    new_im = Image.new("RGB", (desired_size, desired_size))
    new_im.paste(im, ((desired_size-new_size[0])//2,(desired_size-new_size[1])//2))
    test = ImageTk.PhotoImage(new_im)

    self.label1 = tkinter.Label(win,image=test)
    self.label1.image = test
    self.label1.place(x=position[0],y=position[1])
    self.labellist.append(self.label1)

#add in code
win = Tk()
frame = Frame(win)
app = mainpage(frame)
#add func here

#create an image
mainpage.addimage(app, "7H", (0,0))
#to remove images you have to identify the index. The indexes are set in order of what order you added the images. They are reset whenever you clear the screen or remove the image
#remove image above
#mainpage.removeimage(app,0)


mainpage.addimage(app, "9H", (0,0))
#clear canvas
mainpage.clear(app)
mainpage.addimage(app, "7H", (0,0))
mainpage.clear(app)
win.wm_title("Tkinter button")
win.geometry("320x200")
win.mainloop()
