#取得firebase路徑
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
import pytz




# Fetch the service account key JSON file contents
cred = credentials.Certificate('arduino-2026-firebase-adminsdk-vvttj-2060635e68.json')
#Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'firebase_url'
})
while True:

    #抓取firebase資料
    Humi = db.reference('Humi').get()
    Light = db.reference('Light').get()
    Soil = db.reference('Soil').get()
    Temp = db.reference('Temp').get()

    import datetime
    tz = pytz.timezone(pytz.country_timezones('tw')[0])
    x = datetime.datetime.now(tz)
    print(x.year)
    print(x.strftime("%H:%M:%S"))

    #上傳firebase
    year = "%04d" % x.year
    month = "%02d" % x.month
    day = "%02d" % x.day
    hour = "%02d" % x.hour
    minute = "%02d" % x.minute
    second = "%02d" % x.second
    date1 = year+month+day
    time1 = hour+":"+minute+":"+second
    ref = db.reference('time')
    date = ref.child(date1)
    time2 = date.child(time1)
    time2.update({
        'Humi':Humi,
        'Light':Light,
        'Soil':Soil,
        'Temp':Temp
    })

    time.sleep(10)


