package FactoryMethod.pirates;

import FactoryMethod.factory.Human;

public class Pirates extends Human{
	private String name;
	
	public Pirates(String name){
		super();
		this.name = name;
	}
	
	@Override
	public void join() {
		System.out.println(name + "が参加しました。");
	}
	
	public String getName() {
		return this.name;
	}
}
