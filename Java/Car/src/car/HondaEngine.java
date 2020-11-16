package car;

public class HondaEngine implements Engine{
	public HondaEngine() {
		super();
	}
	public void boot() {
		System.out.println("Hondaのエンジン起動");
	}
	public void stop() {
		System.out.println("Hondaのエンジン停止");
	}
}
