import uuid
import httpx
from config import BASE_URL, password

def test_create_new_user():
    path = "/User/"
    
    body = {
        "userName": uuid.uuid4(),
        "password": password
    }
    
    response = httpx.post(
        url=BASE_URL + path,
        data=body
    )
    
    assert response.status_code == 200
    response_json = response.json()
    print(response_json)
