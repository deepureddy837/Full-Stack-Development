
from flask import Flask,render_template,request
import mysql.connector as mysql

db=mysql.connect(
    host="localhost",
    user="root",
    password="Ajaykumar@9550",
    database="kits"
)
cur=db.cursor()
app=Flask(__name__)

@app.route('/form')
def indexPage():
    return render_template('index.html')

@app.route('/formdata',methods=['post'])
def formdata():
    name=request.form['name']
    regdno =request.form['regdno']
    print(name,regdno)
    sql="INSERT INTO kits (name,regdno) VALUES (%s,%s)"
    values=(name,regdno)
    cur.execute(sql,values)
    db.commit()
    return ('data stored')

if __name__=="__main__":
    app.run(debug=True)