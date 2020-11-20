package iterator;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Set;

public class iterator {
	public static void main(String[] args) {
		List<String> siLang = new ArrayList<String>();
		siLang.add("Java");
		siLang.add("Python");
		siLang.add("C#");
		printIterable(siLang.iterator());
	
		Set<String> webLang = new HashSet<String>(); 
		webLang.add("PHP");
		webLang.add("Ruby");
		webLang.add("Node.js");
		printIterable(webLang.iterator());
	}
			
		public static void printIterable(Iterator<String> i) {
			while(i.hasNext()) {
				String s = (String) i.next();
				System.out.println(s);
			}	
		}
}
