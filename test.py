class Parent {
    int x = 10;

    Parent() {
        System.out.print("A");
    }

    Parent(int x) {
        this.x = x;
        System.out.print("B");
    }

    void show() {
        System.out.print("C");
    }
}

class Child extends Parent {
    Child() {
        super(20);
        System.out.print("D");
    }

    Child(int x) {
        System.out.print("E");
    }

    void show() {
        System.out.print(x);
    }
}

public class Main {
    public static void main(String[] args) {
        Parent p1 = new Child();
        Parent p2 = new Child(30);
        p1.show();
        p2.show();
    }
}print('Hello Git')
