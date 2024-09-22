
import java.util.Scanner;

public class tenta {
    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner scanner = new Scanner(System.in);
        System.out.println("Escreva o tamanho do lado : ");
        int l1 = scanner.nextInt();
        System.out.println("Escreva o tamanho do lado : ");
        int l2 = scanner.nextInt();
        System.out.println("Escreva o tamanho do lado : ");
        int l3 = scanner.nextInt();

        if (triangulo(l1, l2, l3)){
            if (equilatero(l1, l2, l3)){
                System.out.println("triangulo equilatero");
            } else if (escaleno(l1, l2, l3)) {
                System.out.println("triangulo escaleno");    
            }
            
        }else{
            System.out.println("Não é um triangulo");
        }

    }

    public static boolean triangulo(int l1, int l2, int l3) {
        return (l1< l2 + l3) && (l2 < l1 + l3) && (l3 < l2 + l1);
    }
    public static boolean escaleno(int l1, int l2, int l3){
        return (l1 != l2) && (l2 != l3) && (l1 != l3);
    }
    public static boolean equilatero(int l1, int l2, int l3){
        return (l1 == l2) && (l2 == l3);
    }


    
}