import pywhatkit


phone_number=input("Enter phone number")
pywhatkit.sendwhatmsg(phone_number, "Test", 15,47, 15, True, 2)
#number, messsage, hour, minute, second,after how many sec after open wapp will send,  condition, after h m sec close

group_id=input("enter group_id")
pywhatkit.sendwhatmsg_to_group("L4fK8yUKkaWLe1WM49AMqi", "test group", 15,59 )