const express=require('express');
const fs=require('fs')
const parser=require('body-parser')
const mysql=require('mysql2')

var con=mysql.createConnection({
    host:"localhost",
    user:"root",
    password:"Ajaykumar@9550",
    database:"deepu"
})
var encodedp=parser.urlencoded({'extended':false});

var app=express();
app.get('/',function(request,response){
    fs.readFile('book.html',function(err,data){
        if(err){
            throw err;
        }
        response.end(data);
    })
})

app.post('/addbook',encodedp,function(request,response){
    var BookName=request.body.name;
    var Author=request.body.author;
    var Category=request.body.category;
    var Branch=request.body.branch;
    var Year=request.body.year;
    con.connect(function(err){
        if(err){
            throw err;
        }
        var sql="INSERT INTO library (BookName,Author,Category,Branch,Year) VALUES ('"+BookName+"','"+Author+"','"+Category+"','"+Branch+"','"+Year+"')";
        con.query(sql,function(err,result){
            if(err){
                throw err;
            }
        })
    })
    response.end("Data stored")
})

app.listen(2003,function(){
    console.log('Server started');
})