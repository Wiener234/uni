package u7;

public class List<T> {

	public ListElement<T> head;

	public void insert(ListElement<T> listElement){
		listElement.next = head;
		head = listElement;
	}

	public void insertNew(ListElement<T> newElem, int i) {
		if (i == 0)
			insert(newElem);
		else {
  		  ListElement<T> tmp = head;
  		  ListElement<T> prev = null;
  		  int l = 0;
  		  // Aufsuchen des i-ten Elements
  		  while (l < i) {
  		    prev = tmp;
  		    tmp = prev.next;
  		    l++;
  		  } // l == i ist erreicht
  		prev.next = newElem;
  		newElem.next = tmp;
  }
}

	public boolean delete(){
		head = head.next;
		return true;
	}

	public boolean isEmpty(){
		if(head != null){
			return true;
		}
		return false;
	}

	public int length(){
		ListElement<T> elem;
		elem = head;
		int i = 0;

		// if you are not dumb use only while with elem != null
		if(elem != null){
			while(elem.next != null){
				i++;
	 	   		elem = elem.next;
	 	   }
		   if(elem.next == null){
			   i++;
		   }
		}
		return i; 
	}

	public void show(){
		ListElement<T> elem;
		elem = head;

		// if you are not dumb use only while with elem != null
		if(elem != null){
			while(elem.next != null){
				System.out.print(elem.value + ", ");
	 	   		elem = elem.next;
	 	   }
		   if(elem.next == null){
			   System.out.println(elem.value + ", ");
		   }
		}
	}	

}
