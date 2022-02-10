from os import stat
import tkinter as tk
from tkinter import Frame, Listbox, Scrollbar, StringVar, ttk,messagebox
from tkinter.font import Font
from newAtm import Transaction as td
from newAtm import Customer as cs
from datetime import date
class guimenu_():  
    tick=0  
    def __init__(self) :
        self.x='900x750'    
    def launcher(self,id,pas,set_information):#set_information
        self.id=id
        self.pas=pas
        self.transactions=set_information # type is dict
        self.nl='\n'
        self.menu()
        self.message_s()
        self.menu_buttons()
       
    def menu(self):
        self.menu=tk.Tk()
        self.menu.config(background='#79e7c9')
        #self.menu.title('Transaction Menu')
        self.menu.geometry(self.x)  
        self.menu.resizable(0,0)
        self.font_1 = Font(family='Times New Roman',size=12,weight='bold',slant='italic') 
        self.font_2 = Font(family='Bookman Old Style ',size=10,weight='normal') 
        self.font_3= Font(family='Bookman Old Style ',size=20,weight='normal')          
        date_info=date.today().strftime("%m/%d/%Y")
        customer_info=tk.Message(self.menu,text=f"""Welcome {self.transactions['name']}  {self.transactions['surname']} {5*"  "} {date_info}""")
        customer_info.config( width=500, font=('Arial Black', 14, 'italic'), background='#79e7c9')
        customer_info.place(x=10,y=5, width=500)
        
    def entry_(self):            
        self.entry = tk.Entry(self.menu,  background="#ffffff",font=self.font_3 , fg='black', width=8)
        self.entry.place(x=350, y=100 ,width=260, height=100)  
        self.entry.bind("<BackSpace>", lambda e: "break")  
        self.entry.bind("<Delete>", lambda e: "break")
        self.allbuttons()
    def allbuttons(self):
        self.framebuttons=tk.Frame(self.menu, bg='#79e7c9', width=250, height=320)
        self.framebuttons.place_configure(x=7,y=100)  
        frame=self.framebuttons        
        self.button1=tk.Button(frame,text='1',command=lambda: self.entry.insert(100,'1'), font=self.font_1, width=5,height=2, background='#1eb886')
        self.button1.place_configure(x=10, y=7)
        self.button2=tk.Button(frame,text='2',command=lambda:self.entry.insert(100,'2'), font=self.font_1, width=5,height=2, background='#1eb886')
        self.button2.place_configure(x= 90 , y=7)
        self.button3=tk.Button(frame, text='3', command=lambda:self.entry.insert(100,'3'),font=self.font_1, width=5,height=2, background='#1eb886')
        self.button3.place_configure(x=170,y=7)
        self.button4=tk.Button(frame,text='4',command=lambda: self.entry.insert(100,'4'), font=self.font_1, width=5,height=2, background='#1eb886')
        self.button4.place_configure(x=10, y=87)
        self.button5=tk.Button(frame,text='5',command=lambda:self.entry.insert(100,'5'), font=self.font_1, width=5,height=2, background='#1eb886')
        self.button5.place_configure(x=90 , y=87)
        self.button6=tk.Button(frame, text='6', command=lambda:self.entry.insert(100,'6'),font=self.font_1, width=5,height=2, background='#1eb886')
        self.button6.place_configure(x=170,y=87)
        self.button7=tk.Button(frame,text='7',command=lambda:self.entry.insert(100,'7'), font=self.font_1, width=5,height=2, background='#1eb886')
        self.button7.place_configure(x= 10 , y=167)
        self.button8=tk.Button(frame, text='8', command=lambda:self.entry.insert(100,'8'), font=self.font_1, width=5,height=2, background='#1eb886')
        self.button8.place_configure(x=90,y=167)
        self.button9=tk.Button(frame,text='9',command=lambda: self.entry.insert(100,'9'), font=self.font_1, width=5,height=2, background='#1eb886')
        self.button9.place_configure(x=170, y=167)
        self.button0=tk.Button(frame,text='0',command=lambda:self.entry.insert(100,'0'), font=self.font_1, width=5,height=2, background='#1eb886')
        self.button0.place_configure(x=8 , y=250)        
        self.buttonDelete=tk.Button(frame, text='DELETE', command=lambda:self.Delbutton(self.entry.get()), font=self.font_1, width=10,height=2, background='#1eb886')
        self.buttonDelete.place_configure(x=125 , y=250)  
        self.backB()             
        
    def backB(self):
        self.buttonBack=tk.Button(self.menu,text='BACK',command=lambda:self.backButton(), font=self.font_1, width=10,height=2, background='#cccc00')
        self.buttonBack.place_configure(x=450 , y=550)         

    def backButton(self):        
        if self.x=='c':
            try:
                self.buttonBack.destroy()  
                self.messages.destroy()
                self.menu_buttons()               
            except AttributeError:
                 print('fout')     
       
        if self.x=='s':            
            self.messages.destroy()  
            self.framebuttons.destroy()   
            self.buttonBack.destroy()
            self.entry.destroy()
            self.buttonOk.destroy()      
            self.menu_buttons()       
        elif self.x=='r':
            self.destroyscrolbar()            
            self.menu_buttons()       
        elif self.x=='v':            
            self.buttonOk.destroy()
            self.messages.destroy() 
            self.buttonBack.destroy()    
            self.infframe.destroy()
            self.menu_buttons()  
        else:            
            self.buttonBack.destroy()
            self.entry.destroy()
            self.buttonOk.destroy()            
            self.messages.destroy()
            self.framebuttons.destroy()
            self.menu_buttons()     
    def destroyscrolbar(self):                  
        destroy_list=[self.yearchoosen,self.monthchoosen,self.dayschoosen,self.yearchoosenLaast,self.monthchoosenLaast,self.dayschoosenLaast,
                      self.label_act,self.label_act2,self.buttonOk,self.buttonBack]
        for j in destroy_list:
                j.destroy()              
        self.framescrol_list.destroy()         
    def menu_buttons(self):         
        self.menu.title('Main Menu')
        bg_color='#1eb886'
        self.buttoninsert=tk.Button(self.menu, text='INSERT', bg=bg_color, command=lambda:self.numeretic_menu('i'),font=self.font_1, width=20,height=2)
        self.buttoninsert.place_configure(x=150,y=100)        
        self.buttonwithdraw=tk.Button(self.menu, text='WITHDRAW',bg=bg_color, command=lambda:self.numeretic_menu('w'),font=self.font_1, width=20,height=2)
        self.buttonwithdraw.place_configure(x=150,y=200)
        self.buttoncheckbalance=tk.Button(self.menu, text='CHECKBALANCE',bg=bg_color, command=lambda:self.numeretic_menu('c'),font=self.font_1, width=20,height=2)
        self.buttoncheckbalance.place_configure(x=500,y=100)
        self.buttonsendmoney=tk.Button(self.menu, text='SENDMONEY',bg=bg_color, command=lambda:self.numeretic_menu('s'),font=self.font_1, width=20,height=2)
        self.buttonsendmoney.place_configure(x=150,y=300)
        self.buttonChangeinfo=tk.Button(self.menu, text='USER INFORMATION',bg=bg_color, command=lambda:self.numeretic_menu('v'),font=self.font_1, width=20,height=2)
        self.buttonChangeinfo.place_configure(x=500,y=300)
        self.buttonExitatam=tk.Button(self.menu, text='EXIT',bg=bg_color, command=lambda:self.exitatm(),font=self.font_1, width=20,height=2)
        self.buttonExitatam.place_configure(x=500,y=450)
        self.buttonProcess=tk.Button(self.menu, text='TRANSACTIONS\nHISTORY',bg=bg_color, command=lambda:self.numeretic_menu('r'),font=self.font_1, width=20,height=2)
        self.buttonProcess.place_configure(x=500, y=200)        
        
        self.menu.mainloop()
    
    def numeretic_menu(self,x):
        self.x=x
        if self.x=='s':
            self.destroy_methods()
            self.send_moneygui()
        elif self.x=='c':
            self.destroy_methods()
            self.backB()
            self.message_s()
            self.transaction_func()
        elif self.x=='r':
            self.destroy_methods()
            self.activity()
            self.backB()
        elif self.x=='v':
            self.destroy_methods()
            self.get_information_user()
            self.backB()
            self.okButton()            
        else:
            self.destroy_methods()
            self.entry_()
            self.okButton()
            self.message_s()
    def destroy_methods(self):
        self.buttoninsert.destroy()
        self.buttoncheckbalance.destroy()
        self.buttonwithdraw.destroy()
        self.buttonsendmoney.destroy()
        self.buttonExitatam.destroy()
        self.buttonProcess.destroy()
        self.buttonChangeinfo.destroy()
    def get_information_user(self):#information menu 
        self.menu.title('Information User')
        self.infframe=Frame(self.menu, width=200, height=200, background='#79e7c9')
        self.infframe.place(x=100, y=200)
        for i,z in enumerate(['name','surname','telephone','mail','balance']):            
            self.label_creatief=tk.Label(self.infframe,text=z, justify='left',  width=10, anchor='w', font=('ariel',18), background='#79e7c9')
            self.label_creatief.grid(row=i, column=0)
        
        self.var_name,self.var_surname,self.var_tel,self.var_mail,self.var_balance=tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar(),tk.StringVar()
        self.entry_name=tk.Entry(self.infframe, textvariable=self.var_name,justify='center', font=('ariel', 15,"italic") )
        self.entry_name.grid(row=0, column=1)
        self.entry_surname=tk.Entry(self.infframe,textvariable=self.var_surname,justify='center', font=('ariel', 15,"italic") )
        self.entry_surname.grid(row=1, column=1)        
        self.entry_telephone=tk.Entry(self.infframe,textvariable=self.var_tel, justify='center', font=('ariel', 15,"italic") )
        self.entry_telephone.grid(row=2, column=1)
        self.entry_mail=tk.Entry(self.infframe,textvariable=self.var_mail, justify='center',font=('ariel', 15,"italic"))
        self.entry_mail.grid(row=3, column=1)
        self.entry_balance=tk.Entry(self.infframe,textvariable=self.var_balance,justify='center', font=('ariel', 15,"italic") )
        self.entry_balance.grid(row=4, column=1)
        self.get_informacie_var()
        self.message_s()
    def get_informacie_var(self):
        self.var_name.set(self.transactions['name'])
        self.var_surname.set(self.transactions['surname'])
        self.var_tel.set(self.transactions['telephone'])
        self.var_mail.set(self.transactions['mail'])
        self.var_balance.set(self.transactions['balance'])
        self.entry_name.config(state='disabled')
        self.entry_surname.config(state='disabled')
        self.entry_telephone.config(state='disabled')
        self.entry_mail.config(state='disabled')
        self.entry_balance.config(state='disabled')
    

    def scrool_bar(self):
        self.framescrol_list=Frame(self.menu, background='black')
        self.framescrol_list.place(x=20, y=300, width=250, height=300)

        self.list_my=Listbox(self.framescrol_list,  borderwidth=5, width=38)                 
        self.list_my.pack(side='left', fill="y")

        self.scrollbar = Scrollbar(self.framescrol_list, orient='vertical', width=15)               
        self.scrollbar.pack(side='right', fill='y')          
        self.scrollbar.config(command=self.list_my.yview)     
    def transaction_hist(self, text):                 
        self.list_my.delete(0,'end')        
        for i, j in enumerate(text,1):   
            trs_his=f"{i}. {j}"         
            self.list_my.insert('end', trs_his)     
    #Messages
    def message_s(self):   
        self.var=StringVar()        
        if self.x=='s' :                            
            self.messages=tk.Message(self.menu,textvariable=self.var)
            self.messages.config( width=500, font=('Arial Black', 14, 'italic'), background='#79e7c9')
            self.messages.place_configure( x=300, y=300)               
        elif self.x=='v':           
            self.messages=tk.Message(self.menu,textvariable=self.var)
            self.messages.config( width=500, font=('Arial Hebrew', 14, 'italic'), aspect=400, background='#79e7c9', )
            self.messages.place_configure( x=300, y=450)
        else:            
            self.messages=tk.Message(self.menu,textvariable=self.var)
            self.messages.config( width=500, font=('Bookman Old Style', 14, 'italic'), aspect=400, background='#79e7c9', )
            self.messages.place_configure( x=350, y=300)
                
    def Delbutton(self,inputlen):#Delete button function        
        if inputlen=='amount:':                       
            self.entry.delete(len(inputlen))
        elif inputlen=='idnumber:':            
            self. entry.delete(len(inputlen))
        else:           
            self.entry.delete(len(inputlen)-1)

    def okButton(self):
        if self.x=='r':
            self.buttonOk=tk.Button(self.menu,text="OK", command=lambda:self.Okbutton(),font=self.font_1, width=10,height=2,background='#cccc00')
            self.buttonOk.place_configure(x=475, y=215)           
        elif self.x =='v':
            self.buttonOk=tk.Button(self.menu,text="UPDATE", command=lambda:self.Okbutton(),font=self.font_1, width=10,height=2,background='#cccc00')
            self.buttonOk.place_configure(x=400, y=375)   
        else:
            self.buttonOk=tk.Button(self.menu,text="OK", command=lambda:self.Okbutton(), font=self.font_1, width=10,height=2,background='#cccc00')
            self.buttonOk.place_configure(x=475, y=215)        
                

    def Okbutton(self):
        if self.x=='s':# 
            tick=self.entry.get()
            if len(tick)!=0:    
                if tick[0]=='a':                 
                    self.amount=self.entry.get()[7:]
                    self.entry.delete(0, 'end')
                    self.entry.insert(0,'idnumber:')           
                elif tick[0]=='i':                
                    self.send_id=self.entry.get()[9:]
                    self.transaction_func()
        elif self.x=='r':
            self.comboget()
        elif self.x=='v':
            if self.tick==0:
                self.entry_telephone.config(state='normal')
                self.entry_mail.config(state='normal')
                self.tick+=1
            else:
                self.telephone=self.entry_telephone.get()
                self.mail=self.entry_mail.get()
                self.tick=0
                self.transaction_func()
        else:                
            self.amount=self.entry.get()
            self.transaction_func()         
    def send_moneygui(self):       
        self.enterinsert='amount:'
        self.entry_()
        self.message_s()
        self.entry.insert(0,self.enterinsert)        
        self.okButton()
    def activity(self):
        self.datum_kies()  
        self.datuminserts()      
        self.scrool_bar()       
        self.okButton()
    def datum_kies(self):
       self.label_act=ttk .Label(self.menu, text = "Select First Date :",font = ("Times New Roman", 12),background='#79e7c9')
       self.label_act.place_configure(x=100, y= 125, width= 125, height= 30)    
       self.label_act2=ttk .Label(self.menu, text = "Select Last Date :",font = ("Times New Roman", 12),background='#79e7c9')
       self.label_act2.place_configure(x=100, y= 175, width= 125, height= 30)            
    def datuminserts(self):           
        months=([str(i).zfill(2) for i in range(1,13)])
        years=[i for i in range(2021,2121)]
        days=[str(i).zfill(2) for i in range(1,32)]
        self.yearchoosen = ttk.Combobox(self.menu,values=years, width = 10)
        self.yearchoosen.place_configure(x=250,y=125)
        self.monthchoosen = ttk.Combobox(self.menu, values=months ,width = 10)
        self.monthchoosen.place_configure(x=335,y=125)        
        self.dayschoosen=ttk.Combobox(self.menu, values=days, width=10)
        self.dayschoosen.place_configure(x=420,y=125)       
             
        self.yearchoosenLaast= ttk.Combobox(self.menu,values=years, width = 10)
        self.yearchoosenLaast.place_configure(x=250,y=175)       
        self.monthchoosenLaast= ttk.Combobox(self.menu, values=months ,width = 10)
        self.monthchoosenLaast.place_configure(x=335,y=175)  
        self.dayschoosenLaast=ttk.Combobox(self.menu, values=days, width=10)
        self.dayschoosenLaast.place_configure(x=420,y=175)                   
    def comboget(self):
       self.beginningDate=f"""{self.yearchoosen.get()}-{self.monthchoosen.get()}-{self.dayschoosen.get()}"""
       self.finishDate=f"""{self.yearchoosenLaast.get()}-{self.monthchoosenLaast.get()}-{self.dayschoosenLaast.get()}"""
       self.transaction_func()
    def transaction_func(self):  
        try:                  
            tr=td(self.id,self.pas)
            if self.x=='i':            
                text=tr.insert_money(int(self.amount),int(self.transactions['balance'])) #take return strin from newAtm
                self.var.set(text)   
                self.entry.delete(0, 'end')             
            elif self.x=='w':
                text=tr.withdraw_money(int(self.amount),int(self.transactions['balance']))
                self.var.set(text)
                self.entry.delete(0, 'end')
            elif self.x=='c':
                text=tr.brengen_of_schrijven_opmongo(balance='balance')
                self.var.set(text)                
            elif self.x=='s':
                if self.transactions['idnumber']!=self.send_id:
                    text=tr.send_money(int(self.amount),self.send_id,int(self.transactions['balance']))                    
                    self.var.set(text)
                    self.entry.delete(0, 'end') 
                    self.entry.insert(0,'amount:')               
                else:
                    self.var.set('You cannot send money to your account')
                    self.entry.delete(0, 'end')
            elif self.x =='r':
                text=tr.find_date(self.beginningDate,self.finishDate,self.transactions['transactions'])       
                self.transaction_hist(text)
            elif self.x=='v':
                text=tr.change_info(self.telephone, self.mail)  
                self.var_tel.set(text[1])
                self.var_mail.set(text[2])
                self.entry_telephone.config(state='disabled')
                self.entry_mail.config(state='disabled')                  
                self.var.set(text[0])

        except ValueError:
           self.var.set('Value is not true')
    def exitatm(self):
            self.menu.destroy()
