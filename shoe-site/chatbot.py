# send notification with price+discounts for all users
# send photos of new models

import pywhatkit


model=[None]*5
model[0]= {'shoe': 'NikeProMax',
            'price':'100',
            'discount':'15%'}

price_str=model[0]['price']
price = float(price_str)
optput=model[0]['shoe'] + price
#output.replace(model[0]['price'],price)
phone_number=input("Enter phone number")
pywhatkit.sendwhatmsg(phone_number, optput , 17,7, 15, True, 2)
#number, messsage, hour, minute, second,after how many sec after open wapp will send,  condition, after h m sec close
#print('shoe {size} and price {price}').format(model[0]['shoe'],model[0]['price'])
#print('Hello'[0:len('hello'):1] from 0 to 4 one by one )

group_id=input("enter group_id")
pywhatkit.sendwhatmsg_to_group("L4fK8yUKkaWLe1WM49AMqi", "test group", 17, 6)


