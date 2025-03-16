import httpx
from config import BASE_URL, user, password

def test_create_existing_user():
    path = "/User/"
    
    body = {
        "userName": user,
        "password": password
    }
    
    response = httpx.post(
        url=BASE_URL + path,
        data=body
    )
    
    assert response.status_code == httpx.codes.NOT_ACCEPTABLE
    response_json = response.json()
    print(response_json)
