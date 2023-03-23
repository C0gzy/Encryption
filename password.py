import tkinter as tk
from cryptography.fernet import Fernet
import tkinter.messagebox

def enc():
    global key ; global f ; global output1
    message = entry1.get()
    key.encode()
    encoded = message.encode()
    
    f = Fernet(key)
    encrypt = f.encrypt(encoded)
    #with open('ec.txt.encrypted', 'wb') as f:
        #f.write(encrypt)
    print("Your encrypted password is")
    print(encrypt)
    print("--------------------------")
    try:
        output.destroy()
    except:
        print()
    var1=tk.StringVar()
    output1= tk.Entry(top , state="readonly",)
    var1.set(str(encrypt, 'utf-8'))
    output1.config(text=var1, relief='flat', font=("Courier", 10))
    output1.grid(row=1,column=1, ipady = 1, ipadx = 105)    
    
def de():
    global key ; global message ; global decrypt ; global output
    data = entry1.get()
    #with open('ec.txt.encrypted', 'rb') as f:
        #data = f.read()7
    data = data.encode("utf-8")
    fernet = Fernet(key)
    decrypt = fernet.decrypt(data)
    print("Your decrypted password is")
    print(decrypt)
    try:
        output1.destroy()
    except:
        print()
    var=tk.StringVar()
    var.set(str(decrypt, 'utf-8'))
    output= tk.Entry(top , state="readonly")
    output.config(text=var, relief='flat', font=("Courier", 10))
    output.grid(row=1,column=1,ipady = 1, ipadx = 105)
    
def cont():
    global entry1 ; global button1 ; global key ; global button2 ; global purpose ; global ecrypt ; 
    key = entry.get()
    print(key)
    
    label1.destroy() ; entry.destroy() ; button.destroy()
    #p = tk.Label(top, text="Purpose")
    i = tk.Label(top, text="Input")
    #purpose= tk.Entry(top)
    ecrypt = b""
    print(ecrypt)
    entry1= tk.Entry(top)
    
    button1=tk.Button(top,text="Encrypt",command=enc)  
    button2=tk.Button(top,text="Decrypt",command=de)  
    #p.grid(row=0,column=0)
    i.grid(row=0,column=0)
    #purpose.grid(row=0,column=1)
    entry1.grid(row=0,column=1, ipady = 1, ipadx =120)
    
    button1.grid(row=3,column=1, ipady = 1, ipadx = 40)
    button2.grid(row=4,column=1, ipady = 1, ipadx = 40)

def start():
    global entry ; global top ; global label1 ; global button ; global positionRight ; global positionDown
    top = tk.Tk()
    windowWidth = top.winfo_reqwidth()
    windowHeight = top.winfo_reqheight()
    positionRight = int(top.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(top.winfo_screenheight()/2 - windowHeight/2)
    top.winfo_toplevel().title("Encryption")



    label1=tk.Label(top,text="Enter Key")
    entry= tk.Entry(top)
    button=tk.Button(top,text="Enter",command=cont)

    
    #config
    button.config(height = 1, width = 20)
    #entry.config(height = 1, width = 20)
    #layout
    label1.grid(row=0,column=0)
    entry.grid(row=0,column=1,ipady=1, ipadx = 45)
    
    button.grid(row=1,column=1)
start()
top.geometry("+{}+{}".format(positionRight, positionDown))
top.mainloop()