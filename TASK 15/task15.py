from flask import Flask,render_template,request
import mysql.connector as mysql
flag=0
db=mysql.connect(
    host="localhost",
    user="root",
    password="Ajaykumar@9550",
    database="kits"
)
cur=db.cursor()
app=Flask(__name__)

@app.route('/registration')
def indexPage():
    return render_template('registration.html')

@app.route('/registerdata',methods=['post'])
def registerdata():
    global flag
    name=request.form['name']
    regdno =request.form['regdno']
    password=request.form['password']
    print(name,regdno,password)
    sql="select * from deepu"
    cur.execute(sql)
    result=cur.fetchall()
    data1=[]
    for i in result:
        print(i)
        data1.append(i)
    for j in data1:
        if name==j[0] or regdno==j[1]:
            flag=0
            sql1="select * from deepu"
            cur.execute(sql1)
            result1=cur.fetchall()
            data1=[]
            for i in result1:
                print(i)
                data1.append(i)
        else:
            flag=1
            sql1="select * from deepu"
            cur.execute(sql1)
            result1=cur.fetchall()
            data1=[]
            for i in result1:
                print(i)
                data1.append(i)
    if flag==1:
        sql="INSERT INTO deepu(name,regdno,password) VALUES (%s,%s,%s)"
        values=(name,regdno,password)
        cur.execute(sql,values)
        db.commit()
        return render_template('registration1.html')
    else:
        return render_template('registration2.html')

@app.route('/login')
def logindata():
    return render_template("login.html")
@app.route('/logindata',methods=['post'])
def login():
    lFlag=0
    regdno=request.form['regdno']
    password=request.form['password']
    sql='select * from deepu'
    cur.execute(sql)
    result1=cur.fetchall()
    data=[]
    for i in result1:
        print(i)
        data.append(i)
    for i in data:
        if regdno==i[1] and password==i[2]:
            lFlag=1           
    if(lFlag==1):
        return render_template("loginsuccess.html")
    else:
        return render_template('loginerror.html')


if __name__=="__main__":
    app.run(debug=True)