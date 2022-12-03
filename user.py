# refer attached file user_registered_data.json for trial of program
import json
class Restaurant:
    def place_order(self):
        menu_card=[
        {'Food Name':'Tandoori Chicken','Quantity': '4 pieces','Price':'INR 240'},
        {'Food Name':'Vegan Burger','Quantity': '1 Piece','Price':'INR 320'},
        {'Food Name':'Truffle Cake','Quantity': '500gm','Price':'INR 900'}]
        print('Here is the menu card for you :')
        for dict in menu_card:
            print('Enter {} for {}--{}--{}'.format((menu_card.index(dict)+1),dict["Food Name"],dict['Quantity'],dict['Price']))
        print('*******************')
        order_input=input('Enter with space what items you would like to have : ')
        order_list=(order_input.split(' '))
        dummy_list=[]
        print(order_list)
        for i in order_list:
            j=int(i)
            dummy_list.append(j)
        print(dummy_list)
        print('Your order is :')
        dumper=tuple()
        for i in dummy_list:
            if i==1:
                print(menu_card[i-1]['Food Name'])
                dumper+=(menu_card[i-1]['Food Name'],)
            elif i==2:
                print(menu_card[i-1]['Food Name'])
                dumper+=(menu_card[i-1]['Food Name'],)
            elif i==3:
                print(menu_card[i-1]['Food Name'])
                dumper+=(menu_card[i-1]['Food Name'],)
        print(dumper)
        confirmer=input('Do you want to confirm order? (Y/N/E) :')
        if confirmer=='y'or confirmer=='Y':
            print('Order placed Successfully')
            with open('user_registered_data','r')as file:
                user_registered_list=json.load(file)
            for dict in user_registered_list:
                if dict['Name']==self.welcome_name and dict['Password']==self.user_password:
                    z=dict['Order History']
                    z.append(dumper)
                    dict['Order History']=z
            with open('user_registered_data','w') as f:
                json.dump(user_registered_list,f)
        elif confirmer=='n'or confirmer=='N':
            self.place_order()    

    def order_history(self):   
        with open('user_registered_data','r')as file:
                user_registered_list=json.load(file)
        for dict in user_registered_list:
            if dict['Name']==self.welcome_name and dict['Password']==self.user_password:
                z=dict['Order History']
                for k in z:
                    print(k)

    ##################### PROFILE UPDATE #######################
    def update_profile(self):
        with open('user_registered_data','r') as file:
            user_registered_list=json.load(file)
        print('Select what you want to update:')
        print('Enter N, for updating Name')
        print('Enter M, for updating Mobile No.')
        print('Enter E, for updating Email')
        print('Enter A, for updating Address')
        print('Enter P, for updating Password')
        update_key=input('Enter here : ')
        
        if 'n'==update_key or 'N'==update_key:
            user_registered_list[self.count]['Name']=input('Enter New Name : ')
        elif 'm'==update_key or 'M'==update_key:
            user_registered_list[self.count]['Mobile No.']=input('Enter New Mobile Number : ')
        elif 'e'==update_key or 'E'==update_key:
            user_registered_list[self.count]['Email']=input('Enter New Email : ')
        elif 'a'==update_key or 'A'==update_key:
            user_registered_list[self.count]['Address']=input('Enter New Address : ')   
        elif 'p'==update_key or 'P'==update_key:
            user_registered_list[self.count]['Password']=input('Enter New Password : ')
        else:
            print('Wrong input.Enter correct option.')
            self.update_profile()
            
        with open('user_registered_data','w') as file:
            json.dump(user_registered_list,file)
        print('Update successful')
        print('*******************')
        self.after_login()
        
#################### AFTER LOGIN ####################
    def after_login(self):
        print('Welcome,{}'.format(self.welcome_name))
        print('*******************')
        print('1. Place new order.')
        print('2. Order History')
        print('3. Update profile')
        print('4. Exit')
        user_input2=int(input('Enter the number of task you want to do :'))
        print('*******************')
        if user_input2 == 1:
            self.place_order()
        elif user_input2==2:
            self.order_history()
        elif user_input2==3:
            self.update_profile()
        elif user_input2==4:
            self.exit()
        else:
            print('Insert an integer from above options.')

    ##################### LOGIN SCREEN #######################
    def login(self):
        self.user_name=input('Enter your mobile no./email id. ')
        self.user_password=input('Enter password ')
        try:
            with open('user_registered_data') as file:
                user_registered_list=json.load(file)
        except:
            print('Nothing found in database. Register your self')
            self.register()

        self.count=0
        for dicts in user_registered_list:
            if dicts['Mobile No.']==self.user_name or dicts['Email']==self.user_name:
                if dicts['Password']==self.user_password:
                    self.welcome_name=dicts['Name']
                    print('*******************')
                    print('Login Successful.')
                    self.after_login()
                else:
                    print('Incorrect username/password. Try again :)')
                    self.login()
                    break
                self.count+=1
            
        


##################### REGISTER SCREEN #######################
    def register(self):
        print('Enter your details in the following')
        user_name=input('Enter your Full Name : ')
        user_mobile=int(input('Enter your Mobile Number : '))
        user_email=input('Enter your Email Id : ')
        user_address=input('Enter your address : ')
        user_password=input('Enter password : ')
        user_data={'Name':user_name,'Mobile No.':str(user_mobile),'Email':user_email,'Address':user_address,'Password':user_password,"Order History":tuple() }
        try:
            with open('user_registered_data','r') as file:
                user_registered_list=json.load(file)
        except:
            user_registered_list=[]
        user_registered_list.append(user_data)
        with open('user_registered_data','w') as file:
            json.dump(user_registered_list,file)
        print('Registration Successful')
        print('Proceed to Login')
        self.login()
    
    
    
   

##################### FIRST SCREEN #######################
print('Welcome to Food Order App')
print('*******************')
print('1. New here? Register.')
print('2. You Hungry? Login')
print('3. Exit')
x=Restaurant()
user_input1=int(input('Enter the number of task you want to do :'))
if user_input1==1:
    x.register()
elif user_input1==2:
    x.login()
elif user_input1==3:
    exit()
else:
    print('Insert an integer from above options.')