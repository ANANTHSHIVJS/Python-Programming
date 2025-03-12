from tkinter import *

class myschool:
    def __init__(self,rootone):
        frame=Frame(rootone)
        frame.pack()
        self.clbutton = Button(frame,text='Clicked',command=self.cl)
        self.clbutton.pack()

        self.cabutton = Button(frame, text='Cancel', command=self.ca)
        self.cabutton.pack()

        self.qubutton = Button(frame, text='Exit', command=frame.quit)
        self.qubutton.pack(side=LEFT)

    def cl(self):
        print("Clicked")
    def ca(self):
        print("Cancel")

root=Tk()
obj=myschool(root)
root.mainloop()



