from flask import Flask ,request, render_template,jsonify
import mysql.connector as mysql
db = mysql.connect(
      host="localhost",
      user="root",
      password="Ajaykumar@9550",
      database="deepu"
)

app=Flask(__name__)
cur=db.cursor()

@app.route('/')
def HomePage():
     return render_template('Index Page.html')
@app.route('/login')
def loginpage():
     return render_template('login.html')
@app.route('/logindata',methods=['post'])
def login():
     flag=0
     email=request.form['email']
     password=request.form['password']
     sql='select * from book'
     cur.execute(sql)
     result=cur.fetchall()
     data=[]
     for i in result:
          print(i)
          data.append(i)
     for i in data:
          if email==i[0] and password==i[1]:
               flag=1
     if(flag==1):
          return render_template('index1.html')
     else:
          return render_template('register.html')
if __name__=="__main__":
    app.run(debug=True)