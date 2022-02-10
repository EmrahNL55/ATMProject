from tkinter import*
from tkinter.font import Font
from newAtm import  Transaction  as tr
from guiMenu import guimenu_

mn=guimenu_()
class login_screen():
    def __init__(self) :
        self.x='500x600'
        
    def log_menu(self):        
        self.root = Tk()
        self.root.config(background='#e0f5d0')
        self.root.title('ATM_Login')   
        self.root.resizable(width=False, height=False)   
        self.root.geometry(self.x)
        self.font_1 = Font(family='Times New Roman',size=24,weight='normal',slant='italic',underline=0,overstrike=0)        
        self.photo = PhotoImage(file ="login-button-orange-clipart.png").subsample(2,2)
        self.framess()
        self.labelss()     
        self.entryss()
        self.root.mainloop()   
        
# FRAMES
    def framess(self):
       self.frame_1 = Frame(self.root, bg='#e0f5d0', width=300, height=50)
       self.frame_1.place(x=125,y=95)
       self.frame_1.pack_propagate(0)
       self.frame_2 = Frame(self.root, bg='#e0f5d0', width=300, height=50)
       self.frame_2.place(x=125,y=35)
       self.frame_2.pack_propagate(0)          
        #on frame 
    def labelss(self):
        labelid=Label(self.frame_1,text='ID NUMBER', font='Arial 12', bg='#e0f5d0')
        labelid.place(x=1, y=1)
        labelpas=Label(self.frame_2,text='PASSWORD', font='Arial 12',bg='#e0f5d0')
        labelpas.place(x=1,y=0)
    def entryss(self):    
        #LOGIN ENTRY      
        self.entrypaswid = Entry(self.frame_2)
        self.entryidwid=Entry(self.frame_1)
        self.entryidwid.place(x=120,y=1)
        self.entrypaswid.place(x=120,y=0)
        #LOGIN BUTTON
        self.button = Button(self.root, image=self.photo, borderwidth=0, bg='#e0f5d0',command=lambda:self.log())
        self.button.place(x=185,y=315)   
    #LOGIN BUTTON COMMAND
    def log(self): 
         self.id,self.password=self.entryidwid.get(), self.entrypaswid.get() 
         self.control()
    #PASWOORD AND USERNAME CONTROL
    def control(self):  
        atm=tr(self.id,self.password)
        set_information=atm.customer_log_in()     
        if set_information!="username or password is incorrect":  
            if set_information['idnumber']==self.id and set_information['password']==self.password:
                self.root.destroy()    
                mn.launcher(self.id,self.password,set_information)    #if login true idnumber and password sending guimenu             
        else:
            self.messages=Message(self.root,text=set_information,)
            self.messages.config( width=500, font=('Arial Hebrew', 14, 'italic'),  bg='#e0f5d0', )
            self.messages.place_configure( x=100, y=200)        

            
login=login_screen()  
login.log_menu()

