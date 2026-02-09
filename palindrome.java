import java .util.Scanner;
 public class palindrome{
  public static void main (String args[]){
    Scanner sc=new Scanner(System.in);
    int n=sc.nextInt();
    int temp=n;
    int rev=0;
    while(n!=0){
      rev=rev*10+n%10;
      n/=10;
    }
    if (temp==rev){
    System.out.println("the given number is palindrome");
    } else {
      System.out.println("the given number is  not palindrome");
    }
  }
 }
      
                      
    