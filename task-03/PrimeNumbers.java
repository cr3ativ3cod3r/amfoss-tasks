import java.util.Scanner;
public class PrimeNumbers {
    static boolean isPrime(int num) {
        for (int i = 2;i < num; i += 1) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);


        System.out.print("Enter a number (n): ");
        int n = scanner.nextInt();

        
        if (n>=2){
            System.out.println("2");
            for (int i = 3; i <= n; i++) {
                if (isPrime(i)) {
                    System.out.print(i+"\n ");
                }
            }}
        scanner.close();
    }
}
