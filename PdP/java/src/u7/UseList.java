package u7;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class UseList {

 
	public static void main(String[] args) throws IOException{

		try{
		List<Integer> intList = new List<>();
		ListElement<Integer> elem1 = new ListElement<>();
		ListElement<Integer> elem2 = new ListElement<>();
		ListElement<Integer> elem3 = new ListElement<>();
		ListElement<Integer> elem4 = new ListElement<>();

		elem1.value = 1;
		elem2.value = 2;
		elem3.value = 3;
		elem4.value = 4;

		intList.insert(elem1); 
		intList.insert(elem2);
		intList.insert(elem3);

		intList.show();

		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

		String temp = reader.readLine();
		int pos = Integer.parseInt(temp);

		if(pos < 0){
			throw new LListIndexOutOfRangeException("Index to to low.");
		}
		else if(pos >= intList.length()){
			throw new LListIndexOutOfRangeException("Index to high.");
		}

		intList.insertNew(elem4, pos);
		intList.show();
		}
		catch(IOException e){
			System.out.println(e);
		}
		catch(NumberFormatException e){
			System.out.println("Input a number that is positiv.");
		}

		
	}

}
