package FactoryMethod;

import FactoryMethod.factory.Factory;
import FactoryMethod.factory.Human;
import FactoryMethod.pirates.PiratesFactory;

public class Main {
	public static void main(String[] args) {
		
		Factory factory = new PiratesFactory();
		
		Human rufy = factory.create("Rufy");
		Human zoro = factory.create("Zoro");
		
		rufy.join();
		zoro.join();
	}
}
