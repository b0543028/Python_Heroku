# 取得稻田中稻子的平均長度

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
   
