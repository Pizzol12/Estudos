bool continuar = true;

while (continuar)
{
    Console.WriteLine("\n=== Fundamentos de C# ===");
    Console.WriteLine("1 - Exibir uma tabuada");
    Console.WriteLine("2 - Somar dois números");
    Console.WriteLine("3 - Gerar números aleatórios");
    Console.WriteLine("0 - Sair");
    Console.Write("Escolha uma opção: ");

    switch (Console.ReadLine())
    {
        case "1":
            ExibirTabuada();
            break;
        case "2":
            SomarNumeros();
            break;
        case "3":
            GerarNumerosAleatorios();
            break;
        case "0":
            continuar = false;
            break;
        default:
            Console.WriteLine("Opção inválida.");
            break;
    }
}

static void ExibirTabuada()
{
    if (!LerInteiro("Digite um número: ", out int valor))
    {
        Console.WriteLine("Entrada inválida.");
        return;
    }

    for (int multiplicador = 1; multiplicador <= 10; multiplicador++)
    {
        Console.WriteLine($"{valor} x {multiplicador} = {valor * multiplicador}");
    }
}

static void SomarNumeros()
{
    if (!LerInteiro("Digite o primeiro número: ", out int primeiro) ||
        !LerInteiro("Digite o segundo número: ", out int segundo))
    {
        Console.WriteLine("Entrada inválida.");
        return;
    }

    Console.WriteLine($"Resultado: {primeiro + segundo}");
}

static void GerarNumerosAleatorios()
{
    int[] numeros = new int[10];

    for (int indice = 0; indice < numeros.Length; indice++)
    {
        numeros[indice] = Random.Shared.Next(0, 1_001);
    }

    Console.WriteLine("Números gerados: " + string.Join(", ", numeros));
}

static bool LerInteiro(string mensagem, out int valor)
{
    Console.Write(mensagem);
    return int.TryParse(Console.ReadLine(), out valor);
}

