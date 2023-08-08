package u3;

public class Point {

	private int x,y;

	public Point(){
		this.x = 0;
		this.y = 0;
	}

	public Point(int x, int y){
		this.x = x;
		this.y = y;
	}

	public int getX(){
		return this.x;
	}

	public int getY(){
		return this.y;
	}

	public void moveAbs(int x, int y){
		this.x = x;
		this.y = y;
	}

	public void moveRel(int x, int y){
		this.x += x;
		this.y += y;
	}


}
