package oasis;
import java.util.Scanner;
public class ATM {
	String userId, userPin;
	double amount,amt,balance=6000,p;
	ATM(String userId, String userPin){
		this.userId=userId;
		this.userPin=userPin;
		
	}
	void deposit(double amount) {
		if(amount!=0) {
			balance=balance+amount;
			p=amount;
		}
	}
	void withdraw (double amt) {
		if(amt!=0 && balance>=amt) {
			balance=balance-amt;
			p=-amt;
		}
		else {
			System.out.println("BANK BALANCE IS LESS THAN AMOUNT");
		}
	}
	void transaction() {
		if(p>0) {
			System.out.println("DEPOSITED AMOUNT"+p);
		}
		else if(p<0) {
			System.out.println("WITHDRAWN AMOUNT"+Math.abs(p));
		}
		else {
			System.out.println("NO TRANSACTIONS DONE");
		}
	}
	void use() {
		char option;
		System.out.println("WELCOME"+userId);
		System.out.println("ENTER YOUR PIN"+userPin);
		System.out.println("1.CHECK BALANCE");
		System.out.println("2.DEPOSIT AMOUNT");
		System.out.println("3.WITHDRAW AMOUNT");
		System.out.println("4.TRANSACTIONS");
		System.out.println("5.EXIT");
		do {
			Scanner sc=new Scanner(System.in);
			System.out.print("ENTER AN OPTION= ");
			option =sc.next().charAt(0);
			switch (option) {
			case'1':
				System.out.println("BALANCE="+balance);
				break;
			case'2':
				System.out.println("DEPOSIT AMOUNT=");
				double amount=sc.nextDouble();
				deposit(amount);
				break;
			case'3':
				System.out.println("WITHDRAW AMOUNT=");
				double amt=sc.nextDouble();
				withdraw(amt);
				break;
			case'4':
				System.out.println("TRANSACTIONS=");
				transaction();
				break;
			case'5':
				System.out.println("EXIT SUCCESSFULLY");
				break;	
			default:
				System.out.println("INVALID OPTION");
				break;
			}
			
		}while(option!='5');
		System.out.println("THANKYOU FOR BANKING WITH US");
		
		
	}

}



package oasis;
import java.util.Scanner;
public class ATMuse {

	public static void main(String[]args) {
		Scanner sc =new Scanner(System.in);
		System.out.println("USERID:");
		String userId =sc.nextLine();
		System.out.println("ENTER USER PIN:");
		String userPin =sc.nextLine();
		ATM a =new ATM(userId,userPin);
		a.use();
		
		
		

	}

}
