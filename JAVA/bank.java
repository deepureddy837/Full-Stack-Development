class Account{
    public String name;
    protected String email;
    private String password;
    public String getpassword(){
        return this.password;
    }
    public void setPassword(String pass){
        this.password=pass;
    }
    public void print()
    {
        System.out.println(name);
        System.out.println(email);
    }
}

public class bank {
    public static void main(String[] args){
        Account a1=new Account();
        a1.name="Deepu Reddy";
        a1.email="deepureddy837@gmail.com";
        a1.setPassword("Ajaykumar@9550");
        a1.print();
        System.out.println(a1.getpassword());
    }
    
}
