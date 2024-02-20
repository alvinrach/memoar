import requests

def test_response():
    response = requests.get('http://localhost:8000/doc')
    print(response.status_code)
    assert response.status_code == 200
    print(1)
    return 1

test_response()