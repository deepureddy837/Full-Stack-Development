let screen=document.getElementById("screen")
buttons=document.querySelectorAll("button");
let screenValue="";
for(item of buttons){
    item.addEventListener('click',(e)=>{
    button Text=e.target.innerText;
    console.log('Button Text is',buttonText);
    if(buttonText=='*'){
        buttonText='*';
        screenValue+=buttonText;
        screen.value=screenValue;

    }    
    else if(buttonText=='C'){
        ScreenValue=" ";
        screen.value=screenvalue;
    }
    }
    
}
