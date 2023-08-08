package u5;

public class Pair<T extends Number, U extends Number> implements Comparable<Pair>{

	private T a;
	private U b;

	Pair(T a, U b){
		this.a = a;
		this.b = b;

	}

	public T getA(){
		return a;
	}

	public U getB(){
		return b;
	}

	// @Override
	// public int compareTo(Pair a){
	// 	if(this.a.doubleValue() > a.a.doubleValue()){
	// 		return -1;
	// 	}
	// 	else if(this.a.doubleValue() < a.a.doubleValue()){
	// 		return 1;
	// 	}
	// 	else{
	// 		return 0;
	// 	}
	// }
	@Override
	public int compareTo(Pair a){
		if(this.a.doubleValue()/this.b.doubleValue() > a.a.doubleValue()/a.b.doubleValue()){
			return -1;
		}
		else if(this.a.doubleValue()/this.b.doubleValue() < a.a.doubleValue()/a.b.doubleValue()){
			return 1;
		}
		else{
			return 0;
		}
	}

}
