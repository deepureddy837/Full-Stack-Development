const express=require('express');
const MongoClient=require('mongodb').MongoClient;

var app=express()
var mongo="mongodb://localhost:27017/"

app.get('/find',function(request,response){
    MongoClient.connect(mongo,function(err,db){
        if(err){
            throw err;
        }
        console.log('connected with db')
        var dbo=db.db('deepu');
        var data=[]
        const cur=dbo.collection('fullstack').find().toArray(function(err,result){
            console.log(result);
            for (let item of result){
                data.push(JSON.stringify(item));
            }
            response.end(data.toString());
        })
    })
})
app.listen(2003,function(){
    console.log("Server Started");
})