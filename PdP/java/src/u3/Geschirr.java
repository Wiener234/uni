package u3;

public abstract class Geschirr {
	private int gewicht;
	private int durchmesser;
	private int höhe;

	Geschirr(){
		this.gewicht = 0;
		this.durchmesser = 0;
		this.höhe = 0;
	}

	Geschirr(int gewicht, int höhe, int durchmesser){
		this.gewicht = gewicht;
		this.durchmesser = durchmesser;
		this.höhe = höhe;
	}



	public void setGewicht(int gewicht){
		this.gewicht = gewicht;
	}
	public int getGewicht(){
		return this.gewicht;
	}

	abstract void g();
	abstract void s();
	abstract void n();

}
