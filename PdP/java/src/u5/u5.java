package u5;

import java.util.*;


public class u5 {

	public static void main(String[] args){
		TreeSet<String> ts = new TreeSet<>();

		ts.add("Aal");
		ts.add("Tanne");
		ts.add("Birke");
		ts.add("Baum");


		Iterator<String> it = ts.iterator();

		while(it.hasNext()){
			System.out.println(it.next());
		}

		HashSet<String> hs = new HashSet<>();

		hs.add("Aal");
		hs.add("Tanne");
		hs.add("Birke");
		hs.add("Baum");

		it = hs.iterator();

		while(it.hasNext()){
			System.out.println(it.next());
		}

		Pair<Integer, Integer> pair = new Pair<>(1,2);

		Pair arr[] = new Pair[5];
		arr[0] = new Pair(2,3);
		arr[1] = new Pair(1,2);
		arr[2] = new Pair(5,4);
		arr[3] = new Pair(8,8);
		arr[4] = new Pair(6,4);

		Arrays.sort(arr);

		// for(int i =0;i<arr.length; i++){
			// System.out.println(arr[i].getA());
		// }

		for(Pair elem : arr){
			System.out.println(elem.getA());
		}


	}
}
