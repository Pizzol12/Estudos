using System.Diagnostics;

const int tamanhoPadrao = 10_000;
const int tamanhoMaximo = 50_000;

int tamanho = LerTamanho(args, tamanhoPadrao, tamanhoMaximo);
int[] numeros = CriarArrayEmbaralhado(tamanho);

Console.WriteLine($"Ordenando {tamanho:N0} elementos com Bubble Sort...");

Stopwatch cronometro = Stopwatch.StartNew();
BubbleSort(numeros);
cronometro.Stop();

Console.WriteLine($"Array ordenado: {EstaOrdenado(numeros)}");
Console.WriteLine($"Tempo: {cronometro.Elapsed.TotalMilliseconds:N3} ms");

if (tamanho <= 100)
{
    Console.WriteLine(string.Join(", ", numeros));
}

static int LerTamanho(string[] argumentos, int padrao, int maximo)
{
    if (argumentos.Length == 0)
    {
        return padrao;
    }

    if (!int.TryParse(argumentos[0], out int tamanho) || tamanho < 1 || tamanho > maximo)
    {
        Console.WriteLine($"Tamanho inválido. Será usado o padrão de {padrao:N0} elementos.");
        return padrao;
    }

    return tamanho;
}

static int[] CriarArrayEmbaralhado(int tamanho)
{
    int[] numeros = Enumerable.Range(1, tamanho).ToArray();

    for (int indice = numeros.Length - 1; indice > 0; indice--)
    {
        int destino = Random.Shared.Next(indice + 1);
        (numeros[indice], numeros[destino]) = (numeros[destino], numeros[indice]);
    }

    return numeros;
}

static void BubbleSort(int[] numeros)
{
    for (int limite = numeros.Length - 1; limite > 0; limite--)
    {
        bool houveTroca = false;

        for (int indice = 0; indice < limite; indice++)
        {
            if (numeros[indice] <= numeros[indice + 1])
            {
                continue;
            }

            (numeros[indice], numeros[indice + 1]) = (numeros[indice + 1], numeros[indice]);
            houveTroca = true;
        }

        if (!houveTroca)
        {
            break;
        }
    }
}

static bool EstaOrdenado(int[] numeros)
{
    for (int indice = 1; indice < numeros.Length; indice++)
    {
        if (numeros[indice - 1] > numeros[indice])
        {
            return false;
        }
    }

    return true;
}

