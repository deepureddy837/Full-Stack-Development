class Student{
    String name;
    int age;
    public void PrintInfo(String name)
    {
        System.out.println(name);
    }
    public void PrintInfo(int age)
    {
        System.out.println(age);
    }
    public void PrintInf(String name,int age)
    {
        System.out.println(name+"   "+age);
    }

}



public class poly {
    public static void main(String args[]){
        Student s1=new Student();
        s1.name="deepu";
        s1.age=20;
        s1.PrintInfo(s1.name);
        s1.PrintInfo(s1.age);
        s1.PrintInf(s1.name,s1.age);
       // s1.PrintInfo(s1.age,s1.name);
    }
    
}
