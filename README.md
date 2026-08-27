# Estudos de Programação — Davi Pizzol

Repositório que reúne meus projetos e exercícios desenvolvidos durante a graduação em Ciência da Computação. O objetivo é registrar minha evolução em lógica de programação, algoritmos, C# e Python.

## Projetos em destaque

| Projeto | Linguagem | Conceitos praticados |
| --- | --- | --- |
| [Classificador de faixa etária](csharp/01-classificador-faixa-etaria) | C# | Entrada de dados, validação e condicionais |
| [Fundamentos interativos](csharp/02-fundamentos-interativos) | C# | Métodos, arrays, laços e menu |
| [Benchmark de Bubble Sort](csharp/03-bubble-sort-benchmark) | C# | Algoritmos, complexidade e medição de tempo |
| [Calculadora de IMC](python/03-calculadora-imc) | Python | Funções, validação e interface Tkinter |
| [Pixel art com matrizes](python/04-pixel-art-mario) | Python | NumPy, matrizes e visualização de dados |
| [Torre de Hanói](python/05-torre-de-hanoi) | Python | Recursão, estruturas de dados e persistência JSON |
| [Calculadora da Lei de Ohm](python/06-calculadora-lei-ohm) | Python | Funções, tratamento de erros e física aplicada |
| [Template de catering](html/template-catering) | HTML | Estrutura de página e personalização de template |

## Estrutura

```text
.
├── csharp/   # Projetos de console em .NET
├── python/   # Exercícios e aplicações em Python
├── html/     # Exercícios de desenvolvimento web
└── docs/     # Informações complementares
```

Cada pasta possui um README com objetivo, conceitos utilizados e instruções de execução.

## Como executar

### C#

É necessário ter o [.NET SDK](https://dotnet.microsoft.com/download) instalado.

```bash
cd csharp/01-classificador-faixa-etaria
dotnet run
```

### Python

É necessário ter Python 3.10 ou superior.

```bash
cd python/02-ano-bissexto
python main.py
```

Projetos com bibliotecas externas possuem um arquivo `requirements.txt` na própria pasta.

## Trabalhos acadêmicos

Materiais de banco de dados, Power BI, Excel e arquitetura de computadores permanecem em repositórios próprios:

- [Modelagem de dados e Power BI](https://github.com/Pizzol12/Modelagem-de-dados)
- [Projeto NextBank — versão final](https://github.com/Pizzol12/NEXT-BANK-FINAL)
- [Documentação original do NextBank](https://github.com/Pizzol12/Nextbank-banco-de-dados)
- [Trabalho de formulário em Excel](https://github.com/Pizzol12/Trabalho-Formulario-)

## Testes

Os principais cálculos e regras de negócio dos projetos Python possuem testes automatizados:

```bash
python -m unittest discover -s tests -v
```

## Autor

**Davi Pizzol de Oliveira Caixeta**  
Estudante de Ciência da Computação — Faculdade Anhanguera
