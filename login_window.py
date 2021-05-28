from tkinter import * 
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Login")

u = StringVar()
p = StringVar()

def fun():
    root.destroy()
    
    if u.get() == "khushboo" and p.get() == "123456789":
        import main
    
    elif u.get()=="" and p.get()=="":
        messagebox.showinfo("","all fields are required")
    else :
        messagebox.showinfo("","Incorrect Username or password")
   
same=True
n=1.6


# setting up background image in the window
bg_img = Image.open("login.jpg")
[imageSizeWidth, imageSizeHeight] = bg_img.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = bg_img.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="black",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

title1label = Label(root,text="Admin Login",bg = "black",fg ="white",font=("times of roman",20,"bold"))
title1label.place(x=0,y=0,relwidth=1)

l_frame = Frame(root,bg = "black")
l_frame.place(x=550,y=150)


user_name = Label(l_frame,text= 'Username',font=("times new roman",15,"bold"),bg = "white").grid(row= 1, column=0)
u_entry =  Entry(l_frame,bg="white",bd=3,font=("",15),textvariable=u).grid(row=1,column=1,padx=10,pady=10)

pass_label =  Label(l_frame,text= 'Password',font=("times new roman",15,"bold"),bg = "white").grid(row= 2, column=0)
u_entry =  Entry(l_frame,bg="white",bd=3,font=("",15),textvariable=p ,show="*").grid(row=2,column=1,padx=10,pady=10)

btn = Button(l_frame,text = 'Login', font=("",15),command=lambda:fun(),bg ="white",fg="black")
btn.grid (row=3,column=2,padx=10,pady=10)


root.mainloop()