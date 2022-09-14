import pytest
import generateDevOpsUserData

def test_get_user_data():
    url = "https://reqres.in/api/users"
    data = generateDevOpsUserData.get_user_data(url)
    assert any(data)
    url = "https://reqres.in/api/users/23"
    try:
        generateDevOpsUserData.get_user_data(url)
    except RuntimeError as exc:
        assert True

def test_generate_excel():
    data = [["adhi","balaji","adhi@gmail.com"]]
    generateDevOpsUserData.generate_excel(data)

def test_generate_html(monkeypatch):
    data = [["adhi","balaji","adhi@gmail.com"]]
    generateDevOpsUserData.generate_html(data)
