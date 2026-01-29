import java.io.BufferedReader;
import java.io.InputStreamReader;

public class azki {
    public static void main(String[] args) throws Exception {
        
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);

        System.out.print("Masukkan nilai a: ");
        int a = Integer.parseInt(br.readLine());

        System.out.print("Masukkan nilai b: ");
        int b = Integer.parseInt(br.readLine());

        System.out.print("Masukkan nilai c: ");
        int c = Integer.parseInt(br.readLine());

        // Hitung rumus: a + b * c
        int hasil = a + b * c;

        System.out.println("Hasil dari " + a + " + " + b + " * " + c + " = " + hasil);
    }
}