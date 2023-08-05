const express=require('express');
const fs=require('fs');
const parser=require('body-parser');

var encodedp=parser.urlencoded({'extended':false})

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
          console.log(request.body.name);
          console.log(request.body.author);
          console.log(request.body.category);
          console.log(request.body.branch);
          console.log(request.body.year);
          response.end('data collected');
})

app.listen(2003,function(){
    console.log('Server started');
})