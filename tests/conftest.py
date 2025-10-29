
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_folder = os.path.join(current_dir, '..')

sys.path.insert(0, project_folder)

from app import Agenda
import pytest

@pytest.fixture(scope="module")
def agenda():
    """
    Cria uma instância de Agenda que persiste por todo o módulo de teste.
    Útil para cenários onde a inserção de dados deve acumular.
    """
    agenda = Agenda()
    yield agenda  


CASES_SUCCESS = [
        ("Teste A", "32132132112"),
        ("Teste B", "12312312312"),
        ("Teste C", "12312312312"),
        ("Teste D", "123sdadaddc45sdadadwds678dsadasdwds09"),
    ]

CASES_FAIL = [
        ("", "32132132112"),
        ("Teste A", ""),
        ("Teste B", "12312"),
        ("Teste C", "dsadwvc"),
    ]
