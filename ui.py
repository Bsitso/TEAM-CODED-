from tkinter import *
root = Tk()
app = Frame(root)
app.grid()
root.geometry("500x250")
root.title("ELECTRONIC VOTING SYSTEM")
Result1 = 50
Result2 = 100
l1 = Label(app, text="\t GHANA ELECTROL COMMISSION", font = 50)
l2 = Label(app, text="\t     ELECTION FINAL RESULTS", font = 50)
l3 = Label(app,text="VINCENT TETTEH", font = 40)
l4 = Label(app,text="EDEM KPEGAH", font = 40)
l5 = Label(app, text="\t \n \n     VINCENT TETTEH : {}".format(Result1), font = 40)
l6 = Label(app,text="\t \n        EDEM KPEGAH : {}".format(Result2), font = 40)
l1.grid(row = 0, column = 1, columnspan = 1, sticky = W)
l2.grid(row = 1, column = 1, columnspan = 1, sticky = W)
#l3.grid(row = 3, column = 0)
l5.grid(row = 3, column = 1)
#l4.grid(row = 5, column = 0)
l6.grid(row = 4, column = 1)
root.mainloop() 