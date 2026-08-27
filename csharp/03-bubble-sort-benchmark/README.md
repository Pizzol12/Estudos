# Benchmark de Bubble Sort

Implementação do algoritmo Bubble Sort com medição de tempo e verificação automática do resultado.

O tamanho padrão é de 10.000 elementos. O limite foi definido em 50.000 porque o Bubble Sort possui complexidade **O(n²)** e se torna extremamente lento para entradas grandes.

## Executar

```bash
dotnet run
```

Para escolher o tamanho do array:

```bash
dotnet run -- 5000
```

## Conceitos praticados

- Algoritmos de ordenação;
- Complexidade de tempo O(n²);
- `Stopwatch`;
- Fisher–Yates para embaralhamento;
- Validação do resultado.

