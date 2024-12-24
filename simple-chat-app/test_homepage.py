import requests


def test_homepage():
    url = "http://localhost:3000"
    response = requests.get(url)
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"


if __name__ == "__main__":
    test_homepage()
    print("Homepage test passed!")
