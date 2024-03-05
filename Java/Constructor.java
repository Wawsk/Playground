// constructor for public class Constructor
class Machine {
    private String name;

    public Machine() {
        System.out.println("Constructor running...");

        name = "Microwave";
    }
}


public class Constructor {
    public static void main(String[] args) {
        Machine machine1 = new Machine();

        new Machine();
    }
    
}