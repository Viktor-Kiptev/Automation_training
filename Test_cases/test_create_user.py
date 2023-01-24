import requests, json, jsonpath, pytest
a = 17

# API url (response 201)
url = "https://reqres.in/api/users"

@pytest.fixture  # for execute just ones use (scope='module')
def start_execution():
    global file
    file = open('C:/Users/Vikto/PycharmProjects/PytestLearning/API_test/POST_request/test_json.json', 'r')
@pytest.mark.Smoke
# @pytest.mark.skip("This is not bor build 9.2.23")
def test_create_new_user1(start_execution):
    json_input = file.read()
    requests_json = json.loads(json_input)
# print(requests_json)
# Make POST request with json input body
    respone = requests.post(url, requests_json)
    print(respone.content)
# Validation response code
    assert respone.status_code == 201
# Fetch Header from response
    print(respone.headers.get('Content-Length'))
# Fetch response to Json format
    respone_json = json.loads(respone.text)

    # Pick id using Json path
    id = jsonpath.jsonpath(respone_json, 'id')
    print(id[0])

@pytest.mark.Smoke
def test_create_new_user_3(start_execution):
    json_input = file.read()
    requests_json = json.loads(json_input)
    respone = requests.post(url, requests_json)
    print(respone.content)
    assert respone.status_code == 201
    print(respone.headers.get('Content-Length'))
    respone_json = json.loads(respone.text)
    id = jsonpath.jsonpath(respone_json, 'id')
    print(id[0])

@pytest.mark.Sanity
# @pytest.mark.skipif(a < 18, reason="incorrect age ")
def test_create_new_user_2(start_execution):
    json_input = file.read()
    requests_json = json.loads(json_input)
    respone = requests.post(url, requests_json)
    print(respone.content)
    assert respone.status_code == 201
    print(respone.headers.get('Content-Length'))
    respone_json = json.loads(respone.text)
    id = jsonpath.jsonpath(respone_json, 'id')
    print(id[0])