#x = input("bde:").split()
#if a[0]==a[-1]:
#    print('yes')
#else:
#    print('no')
#############
#x = input("bde:").split()
#print (x[::-1])
#############
#x = input("bde:").split()
#x.append('5')
#print(x)
#############
#x = input("bde:").split()
#x.remove("5")
#print(x)
#############
#x = input("bde:").split()
#x.pop(1)
#print(x)
#############
#x = input("bde:").split()
#del x[1]
#print(x)
#############
#x = input("bde:").split()
#del x[1]
#x.insert(1,'5')
#print(x)
#############
#x = input("bde:").split()
#b=x.count('5')
#print(b)
#############
#x = input("bde:").split()
#W=x.index("5")
#print(W)
#############
#x = input("bde:").split()
#x.sort()
#print (x[::-1])
#############
#x = input("bde:").split()
#s = input("bde:").split()
#s.extend(x)
#print(s)
#############
#x = input("bde:").split()
#for i in x:
#    print(i)
#############
#x = input("bde:").split()
#print(x)
#d=[]
#for i in x:
#    d.append(int(i))
#print(d)
#############
#x = input("bde:").split()
#print(x)
#d=0
#for i in x:
#    d=d+int(i)
#print (d)
#############
#x = input("bde:").split(',')
#r1 = m1 = t1 = 0
#r = m = t = 0
#apple = 5000
#moz=10000
#tot=7000
#for i in x:
#    a = i.split()
#    if len(a) != 2:
#        continue
#    item = a[0]
#    count = int(a[1])
#    if item == 'apple':
#        r1 = count * apple
#        r = count
#    elif item == 'moz':
#        m1 = count * moz
#        m = count
#    elif item == 'tot':
#        t1 = count * tot
#        t = count
#print(r1, r * '*')
#print(m1, m * '*')
#print(t1, t * '*')
############################################ttk################################################
#from tkinter import *
#import qrcode
#from PIL import Image, ImageTk
#######################
#root = Tk()
#root.title('ebi')
#root.geometry("400x400")
#root.config(bg='gray25')
##########################
#t = Text(root, width=20, height=3)
#t.place(x=110, y=220)
######################
#label = Label(root)
#label.place(x=120, y=50)
#####################
#def generate_qr():
#    global qr_image
#    text1 = t.get('1.0', END).strip()
    ##################
#    if text1:
        
#        qr = qrcode.make(text1)
#        qr.save("qr.png")  
#        #####################
#        img = Image.open("qr.png")
#        img = img.resize((150, 150))  
#        qr_image = ImageTk.PhotoImage(img)
#        label.config(image=qr_image)  
#########################################
#kk = Button(root, text='dorost kon', font=('arial', 15), bg='black', fg='snow', command=generate_qr)
#kk.place(x=140, y=300)
###########################
#root.mainloop()
