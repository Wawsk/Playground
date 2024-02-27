public class arrays {
    public static void main(String[] args) {
        int[] values;
        values = new int [2];
        values[0] = 10;
        values[1] = 20;

        System.out.println(values[1]);
        System.out.println(values[0]);
        System.out.println();

        for(int i=0; i<values.length; i++) {
            System.out.println(values[i]);
        }
        System.out.println();

        int[] numbers = {5, 10, 15};
        for(int i=0; i<numbers.length; i++) {
            System.out.println(numbers[i]);
        }
    }
}
