package Pessoa;

import java.util.Random;
//Classe
public class Pessoa {
	//Atributos
	private String nome;
	private double codigo_identificador;
	private Random aleatorio;
	//Métodos
	public Pessoa (String nome) {
		aleatorio = new Random();
		this.setNome(nome);
		this.codigo_identificador = aleatorio.nextDouble();
		
	}
	private void setNome(String nome) {
		this.nome = nome;
		
	}
	public String getNome() {
		return this.nome;
	}
	public double getCodigoIdentificador() {
		return this.codigo_identificador;
	}
	public static void main(String[] args) {
		Pessoa p1 = new Pessoa("Teste A");
		System.out.println("Pessoa 1:"+p1.getNome());
	}
}	
	
	
	
	


