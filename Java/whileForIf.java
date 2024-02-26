public class whileForIf {
    public static void main(String[] args) {
        
        int value = 0;
        
        while(value < 5) {
            value = value +1;
            System.out.println(value + ". G'day!");
        }
        System.out.println("");
        for (int i=0; i < 5; i++) {
            System.out.printf("The index is: %d\n", i);
        }
        System.out.println("");
        if(value == 0) {
            System.out.printf("value %d is equal to 0", value);
        }
        else if(value != 0) {
            System.out.printf("value %d is not equal to 0", value);
        }
    }
}
