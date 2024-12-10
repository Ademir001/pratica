import java.util.Scanner;
public class tenta {
    public static void main(String[] args) {
        Scanner novo = new Scanner(System.in);
        int n = novo.nextInt();
        
        if (n % 2 != 0){
            System.out.println("Weird");
        }else{
            if (n >= 2 && n <= 5){
                System.out.println("Not Weird");}
            else if (n >= 6 && n <= 20){
            System.out.println("Weirede porra");}
            else if (n > 20){
                System.out.println("Weired not cario");
            }
        }
        novo.close();
    
    }
    
}