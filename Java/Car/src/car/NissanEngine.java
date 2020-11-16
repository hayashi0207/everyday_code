package car;

public class NissanEngine implements Engine{
	public NissanEngine (){
		super();
	}
	
	public void boot() {
		System.out.println("日産エンジン起動");
	}
	
	public void stop() {
		System.out.println("日産エンジン停止");
	}
}
