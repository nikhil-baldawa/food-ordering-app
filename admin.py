import json,random
class Restaurant:
    def add_food_item(self):
        try:
            with open("food_data.json","r") as file:
                food_items_summary=json.load(file)
        except:
            food_items_summary={}
        self.Name = input("Enter the Food item Name : ")
        self.Quantity = (input("Enter Quantity : "))
        self.Price = int(input("Enter  Price : "))
        self.Discount = int(input("Enter Discount % : "))
        self.Stock = (input("Enter Stock : "))

        food_item ={"Name": self.Name, "Quantity": self.Quantity,
    "Price": self.Price,"Discount": self.Discount,"Stock": self.Stock}
        i=1
        while i<=900:
            food_id = '#'+str(random.randint(100,999))
            if food_id not in food_items_summary.keys():
                food_items_summary[food_id] = food_item
                break
            i+=1
        print(food_items_summary)
        with open("food_data.json","w") as file:
            json.dump(food_items_summary,file)
        print("Item Added Successfully")
        print('FooD ID is : ',food_id)

    def edit_food_item(self):
        food_id= input("Enter Food ID of the item you want to edit: ")
        file= open ('food_data.json','r')
        x=json.load(file)
        print(x[food_id])
        
        if food_id in x:
            update_key = input("Details to update in {}: Enter 'N' for 'Name',\
'Q' for 'Quantity','P' for 'Price',\
'D' for 'Discount' And 'S' for Stock: ".format(food_id))
            file.close()
            file=open('food_data.json','w')
            if 'N'== update_key or'n'== update_key:
                    x[food_id]["Name"] = input("Enter New Name : ")
                    print("Name Updated")   
            elif 'Q'== update_key or'q' == update_key:
                    x[food_id]["Quantity"] = input("Enter updated Qty. : ")
                    print("Quantity Updated")
            elif 'P' == update_key or 'p' == update_key:
                    x[food_id]["Price"] = input("Enter Revised Price : ")
                    print("Price Updated")
            elif 'D' == update_key or 'd' == update_key:
                    x[food_id]["Discount"] = input("Enter latest Discount : ")
                    print("Discount Updated")
            elif 'S'== update_key or 's' == update_key:
                    x[food_id]["Stock"] = input("Update the Stock : ")
                    print("Stock Updated")
            else:
                    print("Please enter correct input")
            json.dump(x,file)
                #self.food_items_summary.values =+ 1 
        else:
            print('Entered Food ID does not match.')
        file.close()
        
            
    def remove_food_item(self):
        food_id= (input("Enter Food ID of the item you want to delete : "))
        file=open('food_data.json','r')  
        food_items_summary=json.load(file)
        file.close()
        file=open('food_data.json','w')
        del food_items_summary[food_id]
        print("Remaining Items Available: ",food_items_summary)
        json.dump(food_items_summary,file)
        file.close()

    def showall(self):
        with open('food_data.json','r') as file:
            x=json.load(file)
            for k in x:
                print(k,x[k])

print('Welcome to admin page of Food order app.')
print('****************************************')
print('1. Add a new food item')
print('2. Edit a food item')
print('3. Remove a food item')
print('4. Show list of all food items')
print('5. Exit')
print('****************************************')
user_input=int(input('Select from above what you can do :'))
x=Restaurant()
if user_input==1:
    x.add_food_item()
elif user_input==2:
    x.edit_food_item()
elif user_input==3:
    x.remove_food_item()
elif user_input==4:
    x.showall()
elif user_input==5:
    exit()
else:
    print('Please enter a correct number.')