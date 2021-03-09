class Customer
" Contains properties for first name, last name and email address."

def __init__(self, first_name, last_name, cust_email):
	self.first_name = first_name
	self.last_name = last_name
	self.cust_email = cust_email
	
	
first_name = input('Please enter your first name: ')
last_name = input('Please enter your last name: ')
cust_email = input('Please enter your email: ')

print(f' {first_name}{last_name}, (email)')



class OrderLineItem
"Contains properties for number, unit cost, and unit_quantity"
 
def __init__(self, part_number, unit_cost, quantity):
	self.part_number = part_number
	self.unit_cost = unit_cost
	self.unit_quantity = unit_quantity 
	
	part_number = 
	def get_part_number():
    """Part numbers available."""
    list_of_part_numbers = ['screwdriver':001, 'hammer':002, 'nails':003 ]
	
	




class ItemToPurchase:
	    def __init__(self, name, price, quantity):
	        self.item_name = name
	        self.item_price = price
	        self.item_quantity = quantity
	    
	    def get_item_cost(self):
	        return self.item_price * self.item_quantity

	    

	    
	    def add_items(self, ItemToPurchase):
	        self.shopping_cart.append(ItemToPurchase)
	    
	    def remove_items(self, name):
	        for i in self.shopping_cart:
	            if (i.item_name == name):
	                self.shopping_cart.remove(i)
	                return True
	        return False
	    
	    def checkOut(self):
	        print("Customer Name: " + self.get_customer_name())
	        print("Shopping Date: " + self.get_shopping_date())
	        totalAmount = 0
	        for i in self.shopping_cart:
	            print(str(i.item_quantity) + ' ' + i.item_name + ' @ '+ str(i.item_price))
	            totalAmount = totalAmount + i.get_item_cost()
	        
	        print('Total Amount: ' + str(totalAmount)) 