"""Calculadora de IMC com interface gráfica Tkinter."""

import tkinter as tk
from tkinter import messagebox


def calcular_imc(peso: float, altura: float) -> float:
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso e altura devem ser maiores que zero.")
    return peso / altura**2


def classificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "Abaixo do peso"
    if imc < 25:
        return "Peso normal"
    if imc < 30:
        return "Sobrepeso"
    return "Obesidade"


def criar_interface() -> tk.Tk:
    janela = tk.Tk()
    janela.title("Calculadora de IMC")
    janela.resizable(False, False)

    campos: dict[str, tk.Entry] = {}
    for linha, (chave, rotulo) in enumerate(
        (("nome", "Nome:"), ("altura", "Altura (m):"), ("peso", "Peso (kg):"))
    ):
        tk.Label(janela, text=rotulo).grid(row=linha, column=0, padx=8, pady=6, sticky="e")
        entrada = tk.Entry(janela, width=24)
        entrada.grid(row=linha, column=1, padx=8, pady=6)
        campos[chave] = entrada

    def exibir_resultado() -> None:
        try:
            nome = campos["nome"].get().strip() or "Usuário"
            altura = float(campos["altura"].get().replace(",", "."))
            peso = float(campos["peso"].get().replace(",", "."))
            imc = calcular_imc(peso, altura)
        except ValueError as erro:
            mensagem = str(erro) if str(erro) else "Preencha peso e altura com números válidos."
            messagebox.showerror("Entrada inválida", mensagem)
            return

        messagebox.showinfo(
            "Resultado",
            f"Olá, {nome}!\nSeu IMC é {imc:.2f}.\nClassificação: {classificar_imc(imc)}",
        )

    tk.Button(janela, text="Calcular IMC", command=exibir_resultado).grid(
        row=3, column=0, columnspan=2, pady=12
    )
    return janela


if __name__ == "__main__":
    criar_interface().mainloop()

