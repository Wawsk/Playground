public class arrays {
    public static void main(String[] args) {

// Arrays

        int[] values;
        values = new int [2];
        values[0] = 10;
        values[1] = 20;

        System.out.println(values[1]);
        System.out.println(values[0]);
        System.out.println();

// Iterating arrays

        for(int i=0; i<values.length; i++) {
            System.out.println(values[i]);
        }
        System.out.println();

        int[] numbers = {5, 10, 15};
        for(int i=0; i<numbers.length; i++) {
            System.out.println(numbers[i]);
        }
        System.out.println();

        String[] words = new String[2];

        words[0] = "Hello ";
        words[1] = "World!";

        System.out.print(words[0]);
        System.out.println(words[1]);
        System.out.println();

        String[] pets = {"cat", "hamster", "dog"};

        for(String pet: pets) {
            System.out.println(pet);
        }
        System.out.println();

// 2D arrays

        int[][] grid = {
            {5, 10, 15},
            {2, 4},
            {1, 2, 3, 5, 7, 11, 13, 17}
        };
        System.out.println(grid[1][1]);
        System.out.println(grid[0][2]);
        System.out.println();

        for(int row=0; row<grid.length; row++) {
            for(int col=0; col < grid[row].length; col++) {
                System.out.println(grid[row][col] + "\t");
            }
            System.out.println();
        }
    }
}