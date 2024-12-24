import requests


def test_homepage_content():
    url = "http://localhost:3000"
    response = requests.get(url)
    assert "WebSocket Chat" in response.text, "Homepage content validation failed"


if __name__ == "__main__":
    test_homepage_content()
    print("Content validation test passed!")
