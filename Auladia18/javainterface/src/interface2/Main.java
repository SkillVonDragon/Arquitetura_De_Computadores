package interface2;

import java.text.NumberFormat;

public class Main {
	
	public static void main(String[] args)
	{
		 EstrategiaMedia estrategiaSimples = new MediaSimples();
		 Aluno aluno = new Aluno("Thalles", estrategiaSimples);
		 aluno.obterMedia(10., 6., null);
			 
		 EstrategiaMedia estrategiaTrabalho = new MediaTrabalho();
		 Aluno aluno2 = new Aluno("Thalles", estrategiaTrabalho);
		 aluno2.obterMedia(6.0, 5.0, 15.);
	
	}
}
