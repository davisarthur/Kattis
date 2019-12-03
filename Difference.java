import java.util.Scanner;

public class Difference {

  public static void main(String[] args) {

    Scanner input = new Scanner(System.in);

    while (input.hasNextLine()) {
      Scanner numReader = new Scanner(input.nextLine());
      long a = numReader.nextLong();
      long b = numReader.nextLong();
      long diff = Math.abs(a - b);
      System.out.println(diff);
    }
  }
}
