import pymongo
import datetime
import re
class Customer:   
    def __init__(self, id_number,password):      
        self.id_number,self.password=id_number,password      
        #self.customer_log_in()          
        self.date=datetime.datetime.now()      
    
    def new_customer(self): #GUI new customer butonu olusturulacak
        _id,name,surname,telephone,mail,password=input("id: "),input("name: "),input("surname: "),input("telephone: "),input("mail: "),input("password: ")
        new_customer= {"idnumber":_id,
                        "name":name,
                        "surname":surname,
                        "telephone":telephone,
                        "mail":mail,
                        "password":password,
                        "balance":0,
                        "date":[self.date],
                        "transactions":["0"]
         }
        self.brengen_of_schrijven_opmongo(new_rekening=new_customer) 

    def link_mongo(self):
        connect=pymongo.MongoClient("mongodb+srv://emr:2520@atm02.vfb9g.mongodb.net/Emrah?ssl=true&ssl_cert_reqs=CERT_NONE")
        db=connect.Emrah
        collection=db.atm
        return collection      

    def brengen_of_schrijven_opmongo(self,telephone=None,mail=None, new_rekening=None,display=None,balance=None):        
        if new_rekening is not None:
            self.link_mongo().insert_one(new_rekening)
            print("new rekening is created....")          
        elif telephone is not None and self.id_number is not None:
           self.link_mongo().update_one({"idnumber":self.id_number},{'$set':{'telephone':telephone}})            
        elif mail is not None and self. id_number is not None:
            self.link_mongo().update_one({"idnumber":self.id_number},{'$set':{'mail':mail}}) 
        elif display is not None and self.id_number is not None:  
          print( self.link_mongo().find_one({"idnumber":self.id_number})) #customer's all informations    
        elif balance == "balance":
            return f"""Balance: {self.link_mongo().find_one({"idnumber":self.id_number})["balance"] } € """        
        else:
            print('wrong info')        
    def customer_log_in(self):             
        try:                    
            if len(self.id_number)==4 and len(self.password)==4:            
                a,b=self.link_mongo().find_one({"idnumber":self.id_number})['idnumber'] ,self.link_mongo().find_one({"idnumber":self.id_number})['password'] 
                if a==self.id_number and b==self.password:                      
                    self.set_informations=self.link_mongo().find_one({"idnumber":self.id_number})
                    return self.set_informations
                else:
                    return("username or password is incorrect")                         
            else:
                return("username or password is incorrect")
        except (TypeError):
            return('username or password is incorrect')
        
       
    def change_info(self,telephone, mail):       
        check_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        check_telep=r"\+31\d\d\d\d\d\d\d\d\d"
        result_mail=bool(re.fullmatch(check_email, mail))
        result_telephone=bool(re.search(check_telep, telephone))
        if result_mail==False and result_telephone ==False:
                return (' invalid email and telephone number')
        elif result_mail==False:
                return ('invalid email')
        elif result_telephone==False:
                return ('invalid telephone (e.g. +31000000000)')
        else :                
                self.brengen_of_schrijven_opmongo(telephone=telephone)
                self.brengen_of_schrijven_opmongo(mail=mail)
                telephone=self.link_mongo().find_one({"idnumber":self.id_number})['telephone']
                mail=self.link_mongo().find_one({"idnumber":self.id_number})['mail']
                return ('changed jouw informatie'),telephone,mail
            
    def find_date(self,eerst, laast,set_information):   #parameters wil come from guimenu         
        x=[]
        year,mount,day=eerst.split('-')
        process=set_information
        while len(x)==0:            
            for i in process:
                result=bool(re.search(f'{year}-{mount}-{day}' , i))        
                if result==True:
                    x.append(process.index(i))
                    break
            day=str(int(day)+1).zfill(2)   #iIf the day is not found, the next closest day is selected.
        for i in process:   
            result2=bool(re.search(laast,i)  )  
            if result2==True:
                a=i                      
        x.append(process.index(a)) 
        return self.proces_show(x,process) 
    def proces_show(self,x,process):
        showed_dates=process[x[0]:x[1]+1]
        return showed_dates
                                  
class Transaction(Customer):    
    def __init__(self, id_number, password):
        super().__init__( id_number, password)
                
    def insert_money(self, insert, balance): #money insert add transaction and update balance 
        self.link_mongo().update_one({"idnumber":self.id_number},{'$set':{"balance":(balance+insert)}})  #balance updated
        self.link_mongo().update_one({"idnumber":self.id_number},{'$push':{"transactions":f'+{insert}  date:{self.date}'}}) #mondey added to transactions with date.
        return (f'{insert} Euros added to your account')  

    def withdraw_money(self,money,balance):         
        if money<balance:
            self.link_mongo().update_one({"idnumber":self.id_number},{'$set':{"balance":balance-money}}) 
            self.link_mongo().update_one({"idnumber":self.id_number},{'$push':{"transactions":f'-{money}  date:{self.date}'}})
            return (f'{money} euro withdrew')                    
        else:
            return("Balance is not enough") 

    def send_money(self,money,sent_account, balance):
        try:
            areaid_balance=self.link_mongo().find_one({"idnumber":sent_account})["balance"]# fiedl account balance amount
            if balance>=money:
                new_balance_areaid=areaid_balance+money
                self.link_mongo().update_one({"idnumber":sent_account},{'$set':{"balance":(new_balance_areaid)}})
                self.link_mongo().update_one({"idnumber":sent_account},{'$push':{"transactions":f'+{money}  date:{self.date}'}})
                self.link_mongo().update_one({'idnumber':self.id_number},{'$set':{'balance':(balance-money)}})
                self.link_mongo().update_one({"idnumber":self.id_number},{'$push':{"transactions":f'-{money} /EFT  date:{self.date}'}})
                return (f'{money}€  sended from your account to acoount {sent_account}')
            else:
                return (f'your account balance is not enough')
        except TypeError:
            return ('Wrong acoount number')