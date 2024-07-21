
from flask  import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import io
import datetime

appbot=Flask(__name__)
@appbot.route("/sms", methods=["get", "post"])

def reply():
  with io.open("response.csv","a", encoding="utf-8") as f1:
    ur=request.form.get("Body")
    un=request.form.get("From")
    un=un.relapce("watsapp:","")
    dt=datetime.datetime.now().strftime("%y%m%d--%H%M%S")
    data=un+","+ ur +"," + dt + "\n"
    f1.write(data)
    resp=MessagingResponse()
    resp.message("you sent"+ " " + ur + " "+"from"+" "+un + " " +"on"+" "+dt)
    resp.message("today NikeProMax has 15% /disscount")
    return(str(resp))
  f1.close() 

if(__name__=="__main__"):
 appbot.run()

# send notification with price+discounts for all users
# send photos of new models

#import pywhatkit


#model=[None]*5
#model[0]= {'shoe': 'NikeProMax',
 #           'price':'100',
   #         'discount':'15%'}



#def watsapp_message_bot(phone, id):
# price_str=model[0]['price']
# price = float(price_str)
# output="New disscount,just today: " + model[0]['shoe'] +" at the unice price: "+ price_str
 #output.replace(model[0]['price'],price)
# pywhatkit.sendwhatmsg(phone, output , 15,8, 15, True, 2)
# pywhatkit.sendwhatmsg_to_group(id, output, 17, 6)
                                  #L4fK8yUKkaWLe1WM49AMqi

#phone_number=input("Enter phone number")
#group_id=input("enter group_id") 
#watsapp_message_bot(phone_number, group_id)

#create database

import sqlite3

#conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('data.db')





#def sqlite():
c =conn.cursor() #cursor create
  
      #create database

c.execute("INSERT INTO customer VALUES('John','Elder','john_elder@gmail.com')")




