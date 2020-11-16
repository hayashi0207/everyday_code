import java.util.Scanner;

public class Main2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = a * b % 2;

        if (c == 0) {
            System.out.println("Even");
        } else {
            System.out.println("Odd");
        }
    }
}
