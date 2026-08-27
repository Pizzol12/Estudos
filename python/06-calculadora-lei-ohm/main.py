"""Calculadora das grandezas da Lei de Ohm: V = R × I."""


def calcular_resistencia(tensao: float, corrente: float) -> float:
    if corrente == 0:
        raise ValueError("A corrente não pode ser zero.")
    return tensao / corrente


def calcular_corrente(tensao: float, resistencia: float) -> float:
    if resistencia == 0:
        raise ValueError("A resistência não pode ser zero.")
    return tensao / resistencia


def calcular_tensao(resistencia: float, corrente: float) -> float:
    return resistencia * corrente


def ler_numero(mensagem: str) -> float:
    return float(input(mensagem).replace(",", "."))


def main() -> None:
    print("=== Calculadora da Lei de Ohm ===")
    print("1 - Calcular resistência (R)")
    print("2 - Calcular corrente (I)")
    print("3 - Calcular tensão (V)")
    escolha = input("Escolha uma opção: ").strip()

    try:
        if escolha == "1":
            resultado = calcular_resistencia(
                ler_numero("Tensão em volts: "),
                ler_numero("Corrente em amperes: "),
            )
            print(f"Resistência: {resultado:.2f} Ω")
        elif escolha == "2":
            resultado = calcular_corrente(
                ler_numero("Tensão em volts: "),
                ler_numero("Resistência em ohms: "),
            )
            print(f"Corrente: {resultado:.2f} A")
        elif escolha == "3":
            resultado = calcular_tensao(
                ler_numero("Resistência em ohms: "),
                ler_numero("Corrente em amperes: "),
            )
            print(f"Tensão: {resultado:.2f} V")
        else:
            print("Opção inválida.")
    except ValueError as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()

