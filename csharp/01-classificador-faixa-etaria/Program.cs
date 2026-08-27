Console.Write("Digite a sua idade: ");

if (!int.TryParse(Console.ReadLine(), out int idade) || idade < 0)
{
    Console.WriteLine("Idade inválida. Digite um número inteiro maior ou igual a zero.");
    return;
}

string faixaEtaria = idade switch
{
    <= 10 => "criança",
    <= 17 => "adolescente",
    <= 59 => "adulto",
    _ => "idoso"
};

Console.WriteLine($"Você é {faixaEtaria}.");

