package u6;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Copy {

	public static void main(String[] args){
		
		try{
			BufferedReader reader = new BufferedReader(new FileReader(args[0]));
			BufferedWriter writer = new BufferedWriter(new FileWriter(args[1]));
			String line = null;

			while ((line = reader.readLine()) != null){
				writer.write(line);
				writer.newLine();

			}
			reader.close();
			writer.close();
		}
		catch(IOException e){
			System.out.println("IOExeption: " + e);
		}
	}

}
