#取得firebase路徑
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
from itertools import combinations
from itertools import product
import itertools

def main():
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate('serviceAccount.json')
    #Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'firebase url'
    })

    while True:
        array()

       

def array():
    import math
    global ans
    global pp
    global path
    global cpath
    global index
    global total
    global integer

    #抓取firebase資料
    EP = db.reference('EP').get()
    GCB = db.reference('GCB').get()
    JSB = db.reference('JSB').get()
    LIB = db.reference('LIB').get()
    PE = db.reference('PE').get()
    SG = db.reference('SG').get()
    f = db.reference('facility')
    EPf = f.child('EP').get()
    GCBf = f.child('GCB').get()
    JSBf = f.child('JSB').get()
    LIBf = f.child('LIB').get()
    PEf = f.child('PE').get()
    SGf = f.child('SG').get()


    facility = ['EP','GCB','JSB','LIB','PE','SG','G','H']
    N = len(facility)
    pp = 0
    ans = 1
    index = 0
    path = []
    cpath = []
    integer = []
    total = []
    
    for i in range(1,9):
        ans = ans * i

    p=[0,EP,GCB,JSB,LIB,PE,SG,20,8]    
    o=[0,EPf,GCBf,JSBf,LIBf,PEf,SGf,1,1]      
    t=[0,5,8,10,12,15,20,13,24]  
    r=[0,20,30,40,35,33,42,22,28]   
    l=[[0  ,290 ,160,590 ,720,260,650 ,123,240],
    [290,0   ,700,1130,620,315,550 ,340,330],
    [160,700 ,0  ,670 ,540,320,570 ,220,150],
    [590,1130,670,0   ,610,605,720 ,610,615],
    [720,550 ,800,680 ,0  ,805,690 ,520,428],
    [260,340 ,670,450 ,770,0  ,340 ,180,321],
    [650,700 ,750,380 ,780,880,1080,350,560],
    [123,150 ,540,406 ,250,245,600 ,260,303],
    [240,420 ,430,310 ,305,320,430 ,280,260]]
    
    for i in range(0,8):
        integer.append(i+1)
    
    nums = itertools.permutations(integer)
    
    for x in nums:
        path.append(x)
        
    for j in range(0,ans):
        qwe = 0
        pp = 0
        
        for k in range(0,8):
            qaz = (l[qwe][path[j][k]]/80+math.ceil(p[path[j][k]]/r[path[j][k]])*t[path[j][k]])*o[path[j][k]]
            qwe = path[j][k]
            pp = pp + qaz 
            
        total.append(pp)
        
    min1 = min(total)
    print(min1)
    index = total.index(min1)
    print(index)
    print("best path:",path[index])

     #上傳firebase
    ref = db.reference('place')
    for i in range(0,8):    
        ref.update({
            f'path{i+1}': facility[path[index][i]-1]
        })

    time.sleep(10)

if __name__ == '__main__':
    main()



