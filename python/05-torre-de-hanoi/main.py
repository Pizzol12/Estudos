import json
import os
import sys
from pathlib import Path

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
CYAN = "\033[96m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
WHITE = "\033[97m"
MAGENTA = "\033[95m"

DATA_FILE = Path(__file__).with_name("hanoi_scores.json")


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def carregar_recordes():
    if not DATA_FILE.exists():
        return {}
    try:
        with DATA_FILE.open("r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (json.JSONDecodeError, OSError):
        return {}


def salvar_recorde(dificuldade, movimentos):
    recordes = carregar_recordes()
    atual = recordes.get(str(dificuldade), 999999)
    if movimentos < atual:
        recordes[str(dificuldade)] = movimentos
        with DATA_FILE.open("w", encoding="utf-8") as arquivo:
            json.dump(recordes, arquivo, indent=2)
        return True
    return False


def mostrar_recordes():
    recordes = carregar_recordes()
    if not recordes:
        print(f"{YELLOW}Ainda não há recordes salvos.{RESET}")
        return

    print(f"{BOLD}{CYAN}Melhores recordes{RESET}")
    for dificuldade in sorted(recordes.keys(), key=lambda x: int(x)):
        print(f"{WHITE}Discos {dificuldade}: {recordes[dificuldade]} movimentos{RESET}")


def cabecalho():
    print(f"{BOLD}{CYAN}╔═════════════════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{CYAN}║                TORRE DE HANOI                     ║{RESET}")
    print(f"{BOLD}{CYAN}║              Jogo clássico de lógica              ║{RESET}")
    print(f"{BOLD}{CYAN}╚═════════════════════════════════════════════════════╝{RESET}")


def criar_torres(qtd_discos):
    return [list(range(qtd_discos, 0, -1)), [], []]


def mostrar_torres(torres):
    numero_maximo = max(len(t) for t in torres) if any(torres) else 1
    total_discos = sum(len(torre) for torre in torres)
    largura_base = max(11, total_discos * 2 + 3)

    print(f"\n{BOLD}{YELLOW}Estado atual:{RESET}")
    for nivel in range(numero_maximo, 0, -1):
        linha = ""
        for torre in torres:
            if len(torre) >= nivel:
                disco = torre[nivel - 1]
                largura = disco * 2 + 1
                espaco = (largura_base - largura) // 2
                linha += " " * espaco + f"{BOLD}{GREEN}{'█' * largura}{RESET}" + " " * espaco + "    "
            else:
                linha += " " * largura_base + "    "
        print(linha)

    print(f"{DIM}{'-' * (largura_base * 3 + 18)}{RESET}")
    print(f"{BOLD}{WHITE}       A                 B                 C{RESET}")
    print(f"{DIM}{'-' * (largura_base * 3 + 18)}{RESET}\n")


def validar_movimento(torres, origem, destino):
    if origem not in (0, 1, 2) or destino not in (0, 1, 2):
        return False, f"{RED}Torre inválida. Use A, B ou C.{RESET}"
    if origem == destino:
        return False, f"{RED}Escolha torres diferentes.{RESET}"
    if not torres[origem]:
        return False, f"{RED}A torre de origem está vazia.{RESET}"
    if not torres[destino] or torres[origem][-1] < torres[destino][-1]:
        return True, ""
    return False, f"{RED}Movimento inválido: um disco maior não pode ficar sobre um menor.{RESET}"


def mover_disco(torres, origem, destino):
    ok, mensagem = validar_movimento(torres, origem, destino)
    if not ok:
        return False, mensagem
    torres[destino].append(torres[origem].pop())
    return True, f"{GREEN}Movimento realizado com sucesso!{RESET}"


def venceu(torres, qtd_discos):
    return (
        not torres[0]
        and not torres[1]
        and torres[2] == list(range(qtd_discos, 0, -1))
    )


def limite_movimentos(qtd_discos):
    return (2 ** qtd_discos) - 1 + qtd_discos * 2


def mostrar_resultado(titulo, mensagem, cor):
    borda = "=" * (len(mensagem) + 10)
    print(f"\n{BOLD}{cor}{borda}{RESET}")
    print(f"{BOLD}{cor}{titulo.center(len(mensagem) + 10)}{RESET}")
    print(f"{BOLD}{cor}{mensagem.center(len(mensagem) + 10)}{RESET}")
    print(f"{BOLD}{cor}{borda}{RESET}\n")


def interpretar_jogada(texto):
    texto = texto.strip().lower()
    if texto in {"sair", "exit", "quit", "q"}:
        return None, None, "sair"
    if texto in {"help", "ajuda", "?"}:
        return None, None, "ajuda"
    if texto in {"hint", "dica", "solve", "resolver"}:
        return None, None, "dica"

    partes = texto.split()
    if len(partes) != 2:
        return None, None, "erro"

    origem, destino = partes
    mapa = {"a": 0, "b": 1, "c": 2, "0": 0, "1": 1, "2": 2}
    if origem not in mapa or destino not in mapa:
        return None, None, "erro"
    return mapa[origem], mapa[destino], "ok"


def resolver_hanoi(qtd_discos):
    movimentos = []

    def mover(n, origem, auxiliar, destino):
        if n == 1:
            movimentos.append((origem, destino))
            return
        mover(n - 1, origem, destino, auxiliar)
        movimentos.append((origem, destino))
        mover(n - 1, auxiliar, origem, destino)

    mover(qtd_discos, 0, 1, 2)
    return movimentos


def mostrar_ajuda():
    print(f"{BOLD}{MAGENTA}Como jogar:{RESET}")
    print(f"{WHITE}1. Digite a torre de origem e a de destino.{RESET}")
    print(f"{WHITE}2. Exemplo: A B, B C ou 1 2.{RESET}")
    print(f"{WHITE}3. Só é permitido mover um disco por vez.{RESET}")
    print(f"{WHITE}4. Nunca coloque um disco maior em cima de um menor.{RESET}")
    print(f"{WHITE}5. O objetivo é mover todos os discos para a torre C.{RESET}")
    print(f"{WHITE}6. Durante o jogo, você pode digitar 'dica' para ver uma sugestão.{RESET}")
    print(f"{WHITE}7. Digite 'sair' para encerrar.{RESET}")
    input(f"\n{DIM}Pressione Enter para voltar...{RESET}")


def mostrar_dica(torres, qtd_discos):
    seq = resolver_hanoi(qtd_discos)
    for origem, destino in seq:
        if torres[origem] and (not torres[destino] or torres[origem][-1] < torres[destino][-1]):
            print(f"{YELLOW}Dica: tente mover o disco {torres[origem][-1]} de {chr(65 + origem)} para {chr(65 + destino)}.{RESET}")
            return
    print(f"{YELLOW}A torre alvo já está correta ou o próximo passo depende do estado atual.{RESET}")
    input(f"\n{DIM}Pressione Enter para continuar...{RESET}")


def pedir_qtd_discos():
    while True:
        try:
            valor = input(f"{WHITE}Quantos discos deseja usar? (mínimo 3, máximo 8): {RESET}").strip() or "3"
            qtd = int(valor)
            if 3 <= qtd <= 8:
                return qtd
            print(f"{RED}Escolha um número entre 3 e 8.{RESET}")
        except ValueError:
            print(f"{RED}Digite um número válido.{RESET}")


def menu_principal():
    while True:
        limpar_tela()
        cabecalho()
        print(f"{BOLD}{WHITE}Menu principal{RESET}")
        print(f"{GREEN}1. Jogar{RESET}")
        print(f"{CYAN}2. Como jogar{RESET}")
        print(f"{YELLOW}3. Recordes{RESET}")
        print(f"{RED}4. Sair{RESET}")

        opcao = input(f"\n{BLUE}Escolha uma opção: {RESET}").strip()
        if opcao == "1":
            return "jogar"
        if opcao == "2":
            mostrar_ajuda()
        elif opcao == "3":
            limpar_tela()
            cabecalho()
            mostrar_recordes()
            input(f"\n{DIM}Pressione Enter para voltar...{RESET}")
        elif opcao == "4":
            print(f"{YELLOW}Obrigado por jogar!{RESET}")
            sys.exit(0)
        else:
            print(f"{RED}Opção inválida.{RESET}")
            input(f"{DIM}Pressione Enter para tentar novamente...{RESET}")


def jogar_partida():
    qtd_discos = pedir_qtd_discos()
    torres = criar_torres(qtd_discos)
    movimentos = 0
    melhor = carregar_recordes().get(str(qtd_discos), None)

    max_movimentos = limite_movimentos(qtd_discos)

    while True:
        limpar_tela()
        cabecalho()
        mostrar_torres(torres)
        print(f"{BOLD}{YELLOW}Movimentos: {movimentos}/{max_movimentos}{RESET}")
        if melhor is not None:
            print(f"{DIM}Recorde atual: {melhor} movimentos{RESET}")

        if venceu(torres, qtd_discos):
            limpar_tela()
            cabecalho()
            mostrar_resultado("VITÓRIA!", f"Você venceu em {movimentos} movimentos.", GREEN)
            if salvar_recorde(qtd_discos, movimentos):
                print(f"{YELLOW}Novo recorde registrado!{RESET}")
            else:
                print(f"{DIM}Melhor score mantido.{RESET}")
            input(f"\n{DIM}Pressione Enter para voltar ao menu...{RESET}")
            return

        if movimentos >= max_movimentos:
            limpar_tela()
            cabecalho()
            mostrar_resultado("DERROTA!", f"Você excedeu o limite de {max_movimentos} movimentos.", RED)
            print(f"{WHITE}Tente novamente e melhore sua estratégia.{RESET}")
            input(f"\n{DIM}Pressione Enter para voltar ao menu...{RESET}")
            return

        print(f"{BOLD}{WHITE}Sua jogada:{RESET} escolha origem e destino (ex.: A B ou 1 2)")
        print(f"{DIM}Comandos: 'dica', 'ajuda', 'sair'{RESET}")
        entrada = input(f"{BLUE}> {RESET}").strip()

        origem, destino, status = interpretar_jogada(entrada)

        if status == "sair":
            limpar_tela()
            cabecalho()
            mostrar_resultado("JOGO ENCERRADO", "Até a próxima!", YELLOW)
            input(f"{DIM}Pressione Enter para voltar ao menu...{RESET}")
            return

        if status == "ajuda":
            mostrar_ajuda()
            continue

        if status == "dica":
            mostrar_dica(torres, qtd_discos)
            continue

        if status == "erro":
            print(f"{RED}Formato inválido. Use 'A B' ou '0 1'.{RESET}")
            input(f"{DIM}Pressione Enter para tentar novamente...{RESET}")
            continue

        ok, mensagem = mover_disco(torres, origem, destino)
        print(mensagem)
        if ok:
            movimentos += 1
        input(f"{DIM}Pressione Enter para continuar...{RESET}")


def main():
    while True:
        opcao = menu_principal()
        if opcao == "jogar":
            jogar_partida()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Programa encerrado pelo usuário.{RESET}")
        sys.exit(0)
