
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
    agenda = Agenda(testing=True)
    yield agenda  


CASES_SUCCESS = [
        ("Teste A", "32132132112", "testea@email.com"),
        ("Teste B", "12312312312", "testeb@gmail.com"),
        ("Teste C", "12312312312", "testec@net.co"),
        ("Teste D", "123sdadaddc45sdadadwds678dsadasdwds09", "testea@yahoo.com.br"),
    ]

CASES_FAIL = [
        ("", "32132132112", "testea@email.com"),
        ("Teste AA", "", "testea@email.com"),
        ("Teste BB", "12312", "testea@email.com"),
        ("Teste CC", "dsadwvc", "testea@email.com"),
        ("Teste DD", "12312312332", "")
    ]


CASES_UPDATE_SUCCESS = [
    ("Teste A", "11111111111"),
    ("Teste B", "01010101011")
]
CASES_UPDATE_FAIL = [
    ("","32112312332"),
    ("Teste C","12332"),
    ("Teste T", "12312312322")
]


CASES_DELETE_SUCCESS = [("Teste C"),("Teste A")]
CASES_DELETE_FAIL = [(""),("Te"),("213"),(123)]