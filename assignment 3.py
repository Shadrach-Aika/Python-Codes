# This program creates a function and performs calculations with it
def  calculate_discount (price, discount_percent):
    if discount_percent >= 20:
       discount_offered = price * 0.2
       discounted_price = price - discount_offered
       return discounted_price
        
    else:
        return price



# Call to function
price = int(input("User, Enter the Original price of item: "))
discount_percent = int(input("User, Enter the Percentage discount offered: "))
print("The Discounted price or Original price is: ", calculate_discount(price, discount_percent))

 
 
