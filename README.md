# 將Python腳本部屬到Heroku

**NOTE:** 這邊並不會針對輪廓偵測的部份去做解釋，主要介紹如何部屬heroku

**NOTE2:** 此為部屬Python腳本，並非部屬網頁
<h2>開始</h2>
<h3>環境準備</h3>

1. 要先下載並安裝 [Heroku CLI][1]

2. 下載並安裝 [Git][2]

[1]: https://devcenter.heroku.com/articles/heroku-cli
[2]: https://git-scm.com/downloads

3. 到 [Heroku][3] 官網建立一個新的app

    >region選United States

[3]: https://www.heroku.com/

4. App設定好後，打開cmd並輸入

    ```
    heroku login
    heroku git:clone -a your-app-name
    cd /path/your-app-name
    ```
    
   這時電腦中會出現clone下來的資料夾
   
5. 若已經有準備好的資料夾，直接輸入

     ```
    heroku git:remote -a your-app-name
    ```
   
<h3>資料準備</h3>

將以下檔案丟入clone下來的資料夾中，如果程式中有使用到其他檔案也要記得丟進來

1. requirements.txt

   在python中import套件要寫進requirments.txt裡
   可開啟cmd輸入
   
    ```
    pip freeze
    ```
    
   查詢套件版本
   
2. Procfile

   >注意後面不能有.txt
   
   檔案中輸入<process type>: <command>
    
   這邊使用的是process type 為 worker
   
    ```
    worker: python python檔name.py
    ```
    
3. xxx.py

   將寫好的python腳本丟入資料夾中
   
<h3>push到伺服器</h3>

1. cmd中輸入

    ```
    git add .
    git commit -am "make it better"
    git push heroku master
    ```
    
    上述操作都沒問題的話，應該會順利將檔案push到heroku上
    
2. 執行worker
    
    ```
    cd /path/folder
    git init
    heroku ps:scale worker=1
    ```
    
3. 查看logs

    ```
    heroku logs --tail
    ```
    
<h2>License</h2>

   詳細請參閱 [LICENSE][4]

[4]: https://github.com/b0543028/get-field-contour/blob/master/LICENSE
