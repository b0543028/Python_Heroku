import cv2
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime
from flask import Flask

def test():
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate('serviceAccount.json')
    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'database realtime url'
    })

    for i in range(0,9999):
        year = "%04d" % 2019
        month = "%02d" % 4
        day = "%02d" % 4
        hour = "%02d" % 8
        minute = "%02d" % x.minute
        second = "%02d" % x.second
        j = "%04d" % i
        url = 'your video url'
        url_date = year+month+day
        url_time = hour+j
        r = requests.get(url)
        
        #判斷網址是否可連通
        if r.status_code == 200:
            print(i)
            print(r.status_code)
            print(url)

            cap = cv2.VideoCapture(url)
            length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            
            print(length)
            while True:
              # 從攝影機擷取一張影像
                ret, frame = cap.read()

              # 顯示圖片abs
                if ret == True:
                    cv2.imshow("[origin picture]", frame)
                    cv2.waitKey(1)
                    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    grayImage = cv2.GaussianBlur(grayImage,(3, 3), 0, 0)
                    cv2.imshow("[gray picture]", grayImage)
                    cv2.waitKey(1)

                    cannyImage = cv2.Canny(grayImage, 128, 255, 3)

                    cv2.imshow("[canny picture]", cannyImage)
                    cv2.waitKey(1)

                    contours, hierarchy = cv2.findContours(cannyImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                    for i in range(len(contours)):
                        cv2.drawContours(cannyImage, contours, i, (0,255,0), 1, 8);

                    sum = 0;
                    for i in range(len(contours)):
                        g_dConLength = cv2.arcLength(contours[i], True);
                        sum += g_dConLength;
                    
                    length = sum / len(contours);

                    print("平均長度為:", length);
                
                    x = datetime.datetime.now() #現在時間
                
                    ref = db.reference('field')
                    url_data_ref = ref.child(str(url_date))
                    url_time_ref = url_data_ref.child(str(url_time))
                    field_ref = url_time_ref.child('field001')
                    field_ref.update({
                        'time': str(x),
                        'length':length
                    })

                #   若按下 q 鍵則離開迴圈
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    print("ret false")
                    break

            # 釋放攝影機
            cap.release()

            # 關閉所有 OpenCV 視窗
            cv2.destroyAllWindows()
if __name__ == '__main__':
    test()




