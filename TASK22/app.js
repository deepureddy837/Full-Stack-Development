const express=require('express');

var app=express()
app.get('/',function(request,response){
    response.send('Deepu');
})
app.listen(2003,function(){
    console.log('Server started');
})