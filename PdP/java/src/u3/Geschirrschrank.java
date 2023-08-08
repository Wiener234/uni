package u3;

public class Geschirrschrank {
	private int kapazität;

	Geschirrschrank(){
		this.kapazit = 0;
	}
	Geschirrschrank(int kapazit){
		this.kapazit = kapazit;
	}

	public void einräumen(Geschirr pGeschirr){
		this.kapazit = this.kapazit - pGeschirr.getGewicht();
	}

}
