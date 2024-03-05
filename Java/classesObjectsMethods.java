class Person {
    String name;
    int age;

    void speak() {
        System.out.println("I'm " + name + " and I am " + age);
    }
    int calculateRetirement() {
        int years_left = 60 - age;
        return years_left;
    }
}

public class classesObjectsMethods {
    public static void main(String[] args) {

        Person person1 = new Person();
        person1.name = "Bob Dylan";
        person1.age = 82;
        person1.speak();                                                            

        Person person2 = new Person();
        person2.name = "Taylor Swift";
        person2.age = 34;
        person2.speak();

        int years2 = person2.calculateRetirement();
        System.out.println("Years until retirement: " + years2);
    }
}
