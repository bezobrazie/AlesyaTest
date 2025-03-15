import httpx
from config import BASE_URL, userID, user, password

def test_get_user():
    path = "/User/{userID}"
    
    # можно авторизовываться через хедеры
    # headers = {
    #     "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6IkFsZXN5YVRlc3QiLCJwYXNzd29yZCI6IjEyMzQ1NkFTRHp4YyEiLCJpYXQiOjE3NDIwMzYyMzh9.7iEdfoUzyCgcgz06Xt4ZgkaHRCKLHhnhlb4HGUkAZJM",
    # }
    
    # можно авторизовываться через базовую авторизацию
    auth = httpx.BasicAuth(username=user, password=password)
    
    response = httpx.get(
        url=BASE_URL + path.format(userID = userID),
        auth=auth
        # headers=headers
    )
    
    assert response.status_code == 200, f"Код ответа ожидался 200, по факту пришел {response.status_code}"
    response_json = response.json()
    print(response_json)