const express=require('express');
const MongoClient=require('mongodb').MongoClient;
const url=require('url')

var mongo="mongodb://localhost:27017"
var app=express()

app.get('/insertbook',function(request,response){
    urldata=url.parse(request.url,true);
    var BookName=urldata.query.BookName;
    var Author=urldata.query.Author;
    var Category=urldata.query.Category;
    console.log(BookName,Author,Category);
    MongoClient.connect(mongo,function(err,db){
        if(err){
            throw err;
        }
        var dbo=db.db('deepu');
        var doc={'BookName':BookName,'Author':Author,'Category':Category};
        dbo.collection('fullstack').insertOne(doc,function(err,result){
            if(err){
                throw err;
            }
            response.end("Data Inserted Successfully..")
        })
    })
})
app.listen(2003,function(){
    console.log("Server Started");
})