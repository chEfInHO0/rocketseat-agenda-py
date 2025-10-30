import pytest
from conftest import CASES_SUCCESS, CASES_FAIL, CASES_UPDATE_SUCCESS, CASES_UPDATE_FAIL, CASES_DELETE_SUCCESS, CASES_DELETE_FAIL

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

@pytest.mark.parametrize("name,number", CASES_UPDATE_SUCCESS)
def test_update(agenda,monkeypatch,name,number):
    input_list = [name,number]
    def mock_input(_):
        return input_list.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)

    assert agenda.update() == 204

@pytest.mark.parametrize("name", [("Teste b"),("Teste b")])
def test_update_favorite(agenda,monkeypatch, name):
    input_list = [name]
    def mock_input(_):
        return input_list.pop(0)
    monkeypatch.setattr('builtins.input',mock_input)
    
    assert agenda.update(update_type='favorite') == 204

@pytest.mark.parametrize("name,number", CASES_UPDATE_FAIL)
def test_update_fail(agenda,monkeypatch,name,number):
    input_list = [name, number]
    def mock_input(_):
        return input_list.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)
    print(agenda.contatos)
    assert agenda.update() in [400,401]