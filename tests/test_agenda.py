import pytest
from conftest import CASES_SUCCESS, CASES_FAIL, CASES_UPDATE_SUCCESS, CASES_UPDATE_FAIL, CASES_DELETE_SUCCESS, CASES_DELETE_FAIL

@pytest.mark.parametrize("name,number, email", CASES_SUCCESS)
def test_add(agenda, monkeypatch, name:str, number, email):
    input_list = [name, number, email]

    def mock_input(_):
        if not input_list:
            return ""
        return input_list.pop(0)

    monkeypatch.setattr('builtins.input', mock_input)
    agenda_insert = agenda.add()

    assert agenda_insert == 201
    assert agenda.show_one("Luccas") == 404
    assert name in [x.get('name') for x in agenda.contatos]
    assert len(agenda.contatos) != 0


@pytest.mark.parametrize("name,number, email", CASES_FAIL )
def test_add_fail(agenda,monkeypatch,name,number, email):
    input_list = [name,number, email]
    def mock_input(_):
        return input_list.pop(0)
    
    monkeypatch.setattr('builtins.input',mock_input)
    agenda_insert = agenda.add()
    agenda.reset_state()
    print(agenda.contatos)
    assert agenda_insert in [401,400,404]

@pytest.mark.parametrize("name,number", CASES_UPDATE_SUCCESS)
def test_update(agenda,monkeypatch,name,number):
    input_list = [name,number]
    def mock_input(_):
        return input_list.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)

    assert agenda.update() == 204

@pytest.mark.parametrize("name", [("Teste B"),("Teste B")])
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
    agenda.reset_state()

    assert agenda.update() in [400,401,404]
    

@pytest.mark.parametrize("name", CASES_DELETE_SUCCESS)
def test_delete(agenda, monkeypatch, name):
    input_list = [name]
    def mock_input(_):
        return input_list.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)
    agenda.reset_state()
    assert agenda.delete() == 204
    
@pytest.mark.parametrize('name', CASES_DELETE_FAIL)
def test_delete_fail(agenda, monkeypatch, name):
    input_list = [name]
    def mock_input(_):
        return input_list.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)
    
    agenda.reset_state()

    assert agenda.delete() in [401, 404]