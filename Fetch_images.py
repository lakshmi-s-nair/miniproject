
import pyrebase
from datetime import date, datetime

config = {
    "apiKey": "AIzaSyCWq2F-6h_82SJdt_bjawGh6pH2bpNpHzA",
    "authDomain": "fintrack-d05af.firebaseapp.com",
    "databaseURL": "https://fintrack-d05af-default-rtdb.firebaseio.com",
    "projectId": "fintrack-d05af",
    "storageBucket": "fintrack-d05af.appspot.com",
    "messagingSenderId": "475771069065",
    "appId": "1:475771069065:web:c39cd59224de3bdb9f1c58",
    "serviceAccount": "serviceAccount.json" 
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
database = firebase.database()
storage.child()

storage.download("receipt.jpg" ,"temp.jpg" )
## 1. download image from database
# all_files = storage.child().list_files()
# for file in all_files:            
#     try:
#         print(file.name) 
#         storage.download(file.name, file.name)
#     except:    
#         print('Download Failed')

## 2. set data to firebase
# set data in given format only
# database.child()
# data = {"Data": # "Data" spelling should be correct
#                 {"cat1":"price1", ## this doesnt matter
#                  "cat2":"price2"}
#        }
# database.push(data)

## 3. get val from database
# price = database.child("Receipt").get()
# data = price.val() 
# print(data)

## 4. number of days

# current_time = datetime.now()

# d0 = date(current_time.year, 6, 1)
# d1 = date(current_time.year, current_time.month, current_time.day)
# delta = d1 - d0
# data2 = {"analytics":
#          {  
#             "months":(delta.days)//30,
#             "days":delta.days,
#             "total":"total",
#         }}
# database.child()
# database.push(data2)


