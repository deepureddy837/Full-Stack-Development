const express=require('express');

var app=express()
app.get('/',function(req,res){
    res.end("Deepu")
})
app.listen(2003)