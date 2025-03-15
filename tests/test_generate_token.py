import httpx
from config import BASE_URL, user, password

def test_create_user():
    path = "/GenerateToken/"
    
    body = {
        "userName": user,
        "password": password
    }
    
    response = httpx.post(
        url=BASE_URL + path,
        data=body
    )
    
    assert response.status_code == 200, f"Код ответа ожидался 200, по факту пришел {response.status_code}"
    response_json = response.json()
    response_json['token'] = 'custom_token'
    response_json['expires'] = 'custom_time'
    assert response_json == {'token': 'custom_token', 'expires': 'custom_time', 'status': 'Success', 'result': 'User authorized successfully.'}
    