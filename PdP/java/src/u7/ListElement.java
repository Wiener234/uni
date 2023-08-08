package u7;

public class ListElement<T> {
	public T value;
	public ListElement<T> next;

	ListElement(T value){
		this.value = value;
		this.next = null;
	}

	ListElement(){
		this.value = null;
		this.next = null;
	}
}
