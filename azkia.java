import java.util.Scanner;

public class azkia {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Masukkan alas: ");
        double alas = input.nextDouble();

        System.out.print("Masukkan tinggi: ");
        double tinggi = input.nextDouble();

        // Rumus: 1/2 * alas * tinggi
        double luas = 0.5 * alas * tinggi;

        System.out.println("Luas Segitiga adalah: " + luas);
    }
}