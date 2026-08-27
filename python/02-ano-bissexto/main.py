"""Verifica se um ano informado é bissexto."""


def eh_bissexto(ano: int) -> bool:
    return ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)


def main() -> None:
    try:
        ano = int(input("Digite um ano: "))
    except ValueError:
        print("Entrada inválida. Digite um ano inteiro.")
        return

    if eh_bissexto(ano):
        print(f"{ano} é bissexto e possui 366 dias.")
    else:
        print(f"{ano} não é bissexto e possui 365 dias.")


if __name__ == "__main__":
    main()

