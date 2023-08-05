//Single Inheritance
class Shape{
    String type;
    public void area()
    {
        System.out.println("Print area"+this.type);
    }
}
class Square extends Shape{
    int s;
    public void area()
    {
        System.out.println(this.s*this.s);
    }
}

public class inheritance {
    public static void main(String[] args){
        Square s1=new Square();
        s1.type="Square";
        s1.s=4;
        s1.area();
        s1.area();
    }
    
}
