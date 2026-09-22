package assi2;
import java.util.*;

class SumEven{
	
	static int SumEven(int n) {
		if (n==0)
			return 0;
		
		int digit = n%10;
		if (digit % 2 == 0)
			return digit + SumEven(n/10);
		else
			return SumEven(n/10);
	}
}
public class q1 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Enter the number: ");
		int n = sc.nextInt();
		System.out.println("Sum of even digits = " + SumEven.SumEven(n));

	}


}
