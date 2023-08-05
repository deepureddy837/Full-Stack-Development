from flask import Flask,render_template,request
from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client['deepu']
col=db['fullstack']

app=Flask(__name__)

@app.route('/form')
def formPage():
    return render_template('form.html')

@app.route('/formdata',methods=['post'])
def formdata():
    Name=request.form['Name']
    Regdno =request.form['Regdno']
    Skills=request.form['Skills']
    print(Name,Regdno,Skills)
    k={}
    k['Name']=Name
    k['Regdno']=Regdno
    k['Skills']=Skills
    col.insert_one(k)
    return ('data collected')

if __name__=="__main__":
    app.run(debug=True)