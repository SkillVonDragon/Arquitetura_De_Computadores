package varargs;

public class Main {
	
	public static void main(String[] args)
	{
		Aluno aluno = new Aluno();		
		try
		{
			aluno.setNome("Thalles");
			aluno.setNota1(6.);
			aluno.setNota2(9.);
		}
		catch(Exception ex)
		{
			
		}
		System.out.println();
		
	}
}
