import pytest
from conftest import CASES_SUCCESS, CASES_FAIL

@pytest.mark.parametrize("name,number", CASES_SUCCESS)
def test_add(agenda, monkeypatch, name:str, number):
    input_list = [name, number]

    def mock_input(_):
        if not input_list:
            return ""
        return input_list.pop(0)

    monkeypatch.setattr('builtins.input', mock_input)
    agenda_insert = agenda.add()

    assert agenda_insert == 201
    assert agenda.show_one("Luccas") == 404
    assert any(name.capitalize() in contanct for contanct in agenda.contatos)
    assert len(agenda.contatos) != 0


@pytest.mark.parametrize("name,number", CASES_FAIL )
def test_add_fail(agenda,monkeypatch,name,number):
    input_list = [name,number]
    def mock_input(_):
        return input_list.pop(0)
    
    monkeypatch.setattr('builtins.input',mock_input)
    agenda_insert = agenda.add()
    print(agenda.contatos)
    assert agenda_insert in [401,400,404]