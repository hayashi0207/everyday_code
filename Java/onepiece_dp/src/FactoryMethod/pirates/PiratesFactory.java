package FactoryMethod.pirates;

import FactoryMethod.factory.Factory;
import FactoryMethod.factory.Human;

public class PiratesFactory extends Factory{
	@Override
	protected Human createHuman(String name) {
		return new Pirates(name);
	}
}
