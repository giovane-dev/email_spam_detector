from tkinter import *
import local_library as lb
import joblib
from PIL import ImageTk, Image

# Model
#--------

model = joblib.load("MultinomialNB_Model_v2.pkl")


# Functions 
#-----------

def show_safe():
    NotSpam = Toplevel(master=root)
    NotSpam.title("Safe")
    lb.center_window(NotSpam, 230,180)
    NotSpam.iconbitmap('right.ico')
    NotSpam.bg_image = ImageTk.PhotoImage(Image.open('right.png'))
    background_label = Label(NotSpam, image=NotSpam.bg_image)
    background_label.pack(pady=10)
    label = Label(NotSpam, text="SAFE",font=("Arial",17),fg="green")
    label.pack(pady=15)
        
def show_spam():
    Spam = Toplevel(master=root)
    Spam.title("Spam")
    lb.center_window(Spam, 230,180)
    Spam.iconbitmap('red.ico')
    Spam.bg_image = ImageTk.PhotoImage(Image.open('red.png'))
    background_label = Label(Spam, image=Spam.bg_image)
    background_label.pack(pady=10)
    label = Label(Spam, text="SPAM",font=("Arial",17),fg="red")
    label.pack(pady=15)
        

def predict_spam():
    input_text = txt_input.get("1.0", "end-1c")
    prediction = model.predict([input_text])
    if prediction == 0:
        show_safe()
    else:
        show_spam()
    txt_input.delete("1.0", "end")
    txt_input.insert("1.0", "")


def exit():
    root.destroy()

#------------------------------------------------------------------------------------------------------------------------    
#Gui initialize

root=Tk()
root.title("Email Spam detector")
lb.center_window(root,400,300)
root.iconbitmap('icon.ico')
root.config(bg="Gray")
textLabel = Label(root, text="Email Spam detector",bg="gray",font=("Arial",16))
txt_input = Text(root,height=5,width=25)
frame = Frame(root,bg="gray",highlightbackground="#eef0ff",highlightthickness=1,height=70,width=300,bd=0)

# Buttons
#---------

check = Button(master= frame,text="Check",width=20,command=predict_spam)
exit=Button(master=frame,text="Exit",width=20, command=exit)

# Pack 
#------
check.grid(column=0,row=0,padx= 10,pady= 8)
exit.grid(column=0, row=1,padx=10,pady=8)
textLabel.pack(pady=30)
txt_input.pack()
frame.pack(pady=10)
#-----------------------------------------------------------
root.mainloop()

