import httpx
from config import BASE_URL, user, password

def test_aurhorized():
    path = "/Authorized/"
    
    body = {
        "userName": user,
        "password": password
    }
    
    response = httpx.post(
        url=BASE_URL + path,
        data=body
    )
    
    assert response.status_code == 200
    assert response.text == 'true'
    # Проверка которая всегда проходит.
    assert True
