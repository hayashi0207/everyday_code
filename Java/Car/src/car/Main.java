package car;

public class Main {

	public static void main(String[] args) {
		Engine engine1 = new HondaEngine();
		Engine engine2 = new NissanEngine();
		Car car1 = new Car(engine1);
		Car car2 = new Car(engine2);
		
		car1.engineStart();
		car2.engineStart();
		car1.engineStop();
		car2.engineStop();
	}
}
