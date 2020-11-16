package FactoryMethod.factory;

public abstract class Factory {
	public final Human create(String name) {
		Human human = createHuman(name);
		return human;
	}

	protected abstract Human createHuman(String name);
}
