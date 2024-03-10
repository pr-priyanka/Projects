package oasis;
import java.util.Scanner;
public class solution {
	Scanner sc=new Scanner(System.in);
	void game() {
		int r= 96;
		System.out.println("Random Number" +r);
		int k=5;
		while(k>0) {
			System.out.println("Enter the guess");
			int guess=sc.nextInt();
			if(guess==r) {
				System.out.println("Correct");
				break;
			}
			else if(guess<r) {
				System.out.println("Wrong! number is greater than guess");
				//break;
			}
			else if(guess>r) {
				System.out.println("Wrong! number is lesser than guess");
				//break;
			}
			k--;
		System.out.println("You have"+k+"more attempts left");
		}
		int count=k;
		switch(count) {
		case 5:
			System.out.println("YOUR SCORE IS 100");
			break;
		case 4:
			System.out.println("YOUR SCORE IS 80");
			break;
		case 3:
			System.out.println("YOUR SCORE IS 60");
			break;
		case 2:
			System.out.println("YOUR SCORE IS 40");
			break;
		case 1:
			System.out.println("YOUR SCORE IS 20");
			break;
		default:
			System.out.println("YOYR SCORE IS 0");
		    
		}
		
	}
  
}


  
package oasis;

public class guessgame {
	public static void main(String agrs[]) {
	    solution obj=new solution();
	    obj.game();
	}

}

	



	
 
