from flask import Flask,request
import mysql.connector as mysql


db=mysql.connect(
    host="localhost",
    user="root",
    password="Ajaykumar@9550",
    database="kits"
)

cur=db.cursor()

app=Flask(__name__)

@app.route('/getdata',methods=['get'])
def getdata():
    sql='select * from kits'
    cur.execute(sql)
    result=cur.fetchall()
    data=[]
    for i in result:
        print(i)
        data.append(i)
    return str(data)

if __name__=="__main__":
    app.run(debug=True)