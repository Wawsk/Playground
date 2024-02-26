import java.util.Scanner;

public class input {
    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);

        System.out.println("Enter your text:");
        String line = input.nextLine();

        System.out.println("You entered: " + line);
    }
}
