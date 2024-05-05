from flask import Flask,request,redirect
from datetime import datetime
import sqlite3 as db

class DB():
    def init(self):
        self.con= db.connect("UrlDB")
        self.con.execute("CREATE TABLE IF NOT EXISTS URLTABLE (url string PRIMARY KEY,shortUrl string)")
    
    def insert(self,url:str,shortUrl:str):
        self.init()
        with self.con:
            self.con.execute(f"INSERT INTO URLTABLE VALUES ('{url}','{shortUrl}') ")
    
    def select(self,shortUrl:str):
        self.init()
        with self.con:
            res=list(self.con.execute(f"SELECT url FROM URLTABLE WHERE shortUrl='{shortUrl}'"))
        return res[0][0]

app=Flask(__name__)

@app.route("/",methods = ["POST"])
def fn():
    url=request.json["url"]
    shorturl= str(datetime.now().timestamp()).replace(".","")
    db=DB()
    db.insert(url,shorturl)
    return "http://0.0.0.0:5000/"+shorturl

@app.route("/<shortUrl>")
def fn2(shortUrl):
    db=DB()
    url = db.select(shortUrl)
    return redirect(url)


if(__name__ =="__main__"):
    app.run(host="0.0.0.0",port=5000)