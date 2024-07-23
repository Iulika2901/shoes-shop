# send notification with price+discounts for all users
# send photos of new models

import pywhatkit


model=[None]*5
model[0]= {'shoe': 'NikeProMax',
            'price':'100',
            'discount':'15%'}



def watsapp_message_bot(phone, id):
 price_str=model[0]['price']
 price = float(price_str)
 output="New disscount,just today: " + model[0]['shoe'] +" at the unice price: "+ price_str
 output.replace(model[0]['price'],price)
  pywhatkit.sendwhatmsg(phone, output , 15,8, 15, True, 2)
 pywhatkit.sendwhatmsg_to_group(id, output, 17, 6)
                                  #L4fK8yUKkaWLe1WM49AMqi
phone_number=input("Enter phone number")
group_id=input("enter group_id") 
watsapp_message_bot(phone_number, group_id)
