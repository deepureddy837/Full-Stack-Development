from flask import Flask
from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client['deepu']
col=db['fullstack']

app=Flask(__name__)

@app.route('/getdata',methods=['get'])
def getdata():
    k=col.find()
    data=[]
    for i in k:
        data.append(i)
    return str(data)
if __name__=="__main__":
    app.run(debug=True)