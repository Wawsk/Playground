import java.util.Scanner;

public class inputWhileDo {
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);

        System.out.println("Enter your text:");
        String line = input.nextLine();

        System.out.println("You entered: " + line);

        Scanner scanner = new Scanner(System.in);
        int value = 0;
        do {
            System.out.println("Enter a number: ");
            value = scanner.nextInt();
        }
        while(value != 5);
        System.out.println("Yes, 5 is the answer");
    }
}
