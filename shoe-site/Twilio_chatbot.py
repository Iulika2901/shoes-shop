
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



