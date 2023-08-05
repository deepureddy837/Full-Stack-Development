const express=require('express');
const fs=require('fs')

var app=express();
app.get('/base',function(request,response){
    fs.readFile('base.html',function(err,data){
        if(err){
            throw err;
        }
        response.end(data);
    })
})


app.get('/name',function(request,response){
    fs.readFile('photo.html',function(err,data){
        if(err){
            throw err;
        }
        response.end(data);
    })
})
app.listen(2003,function(){
    console.log('Server started');
})