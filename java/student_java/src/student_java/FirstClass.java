package student_java;

public class FirstClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("hello java.2.");
		
	int i, j, k;
		for(i = 1, j = 1, k = 0; i < 5; i++ ) {
			if((i%2) == 0) {
				System.out.println(i);
				System.out.println(j);
				System.out.println(k);
				System.out.println("정수 end");
				continue;
				
			}
			k += i * j++;
		}
		System.out.println(k);
	}
}
