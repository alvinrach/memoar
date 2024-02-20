import requests
import time

def test_response():
    time.sleep(10)
    response = requests.get('http://localhost:8000/docs')
    print(response.status_code)
    assert response.status_code == 200
    print(1)
    return 1

test_response()