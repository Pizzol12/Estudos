"""Testes básicos das funções centrais dos projetos Python."""

import importlib.util
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]


def carregar_modulo(nome: str, caminho: str):
    especificacao = importlib.util.spec_from_file_location(nome, RAIZ / caminho)
    if especificacao is None or especificacao.loader is None:
        raise ImportError(f"Não foi possível carregar {caminho}")
    modulo = importlib.util.module_from_spec(especificacao)
    especificacao.loader.exec_module(modulo)
    return modulo


ano_bissexto = carregar_modulo("ano_bissexto", "python/02-ano-bissexto/main.py")
imc = carregar_modulo("imc", "python/03-calculadora-imc/main.py")
hanoi = carregar_modulo("hanoi", "python/05-torre-de-hanoi/main.py")
lei_ohm = carregar_modulo("lei_ohm", "python/06-calculadora-lei-ohm/main.py")


class TestAnoBissexto(unittest.TestCase):
    def test_regras_do_calendario_gregoriano(self):
        self.assertTrue(ano_bissexto.eh_bissexto(2024))
        self.assertFalse(ano_bissexto.eh_bissexto(1900))
        self.assertTrue(ano_bissexto.eh_bissexto(2000))


class TestCalculadoraImc(unittest.TestCase):
    def test_calculo_e_classificacao(self):
        resultado = imc.calcular_imc(72, 1.80)
        self.assertAlmostEqual(resultado, 22.2222, places=3)
        self.assertEqual(imc.classificar_imc(resultado), "Peso normal")

    def test_rejeita_altura_zero(self):
        with self.assertRaises(ValueError):
            imc.calcular_imc(72, 0)


class TestTorreDeHanoi(unittest.TestCase):
    def test_vitoria_exige_todos_os_discos_na_torre_c(self):
        self.assertFalse(hanoi.venceu([[3, 2], [], [1]], 3))
        self.assertTrue(hanoi.venceu([[], [], [3, 2, 1]], 3))

    def test_impede_disco_maior_sobre_menor(self):
        valido, _ = hanoi.validar_movimento([[2], [1], []], 0, 1)
        self.assertFalse(valido)


class TestLeiDeOhm(unittest.TestCase):
    def test_calculos(self):
        self.assertEqual(lei_ohm.calcular_resistencia(12, 2), 6)
        self.assertEqual(lei_ohm.calcular_corrente(12, 6), 2)
        self.assertEqual(lei_ohm.calcular_tensao(6, 2), 12)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            lei_ohm.calcular_resistencia(12, 0)


if __name__ == "__main__":
    unittest.main()

