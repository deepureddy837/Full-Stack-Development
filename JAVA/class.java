class Pen{
    String color;
    String brand;
    String type;
    public void write(){
        System.out.println(this.color);
        System.out.println(this.brand);
        System.out.println(this.type);
    }
    public void read(){
        System.out.println(this.color);
        System.out.println(this.brand);
        System.out.println(this.type);
    }
    Pen(String color,String brand,String type){
        this.color=color;
        this.brand=brand;
        this.type=type;
    }
}
class OOPS{
    public static void main(String args[]){
       /*  Pen p1=new Pen();
        p1.color="blue";
        p1.brand="saino";
        p1.type="cello";
        Pen p2=new Pen();
        p2.color="black";
        p2.brand="bitco";
        p2.type="ballpoint";*/
        Pen p3=new Pen("red","santoor","gel");
        p3.read();
        p3.read();
    }
}