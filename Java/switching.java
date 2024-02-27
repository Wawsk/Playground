import java.util.Scanner;

public class switching {
    public static void main(String[] args) {
        
        // init input
        Scanner input = new Scanner(System.in);

        // collect input
        System.out.println("Enter a command: ");
        String text = input.nextLine();

        // switch
        switch (text) {
            case "start":
                System.out.println("Application started...");
                break;
            case "stop":
                System.out.println("Application stopped...");
                break;
            default:
                System.out.println("Not valid input...");
                break;
        }
    }
}
