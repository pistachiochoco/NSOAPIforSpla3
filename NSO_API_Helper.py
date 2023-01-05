import NSO_API
import os, sys, json, re
import requests
from bs4 import BeautifulSoup

class Query:
    def __init__(self, name, hashid, operation):
        self.name = name
        self.id = hashid
        self.opr = operation

    def __str__(self):
        return f"{self.name}, {self.id}, {self.opr}"

    def __repr__(self):
        return self.__str__()

SPLA3_API_URL = NSO_API.SPLA3_API_URL
self_path = os.path.dirname(__file__)
data_path = os.path.join(self_path + '/Data')
try:
    os.mkdir(data_path)
except(FileExistsError):
    pass

def load_tokens():
    config_path = os.path.join(self_path, "config.txt")
    try:
        config_file = open(config_path, "r")
        config_data = json.load(config_file)
        config_file.close()
    except (IOError, ValueError):
        print("No tokens available. Please generate tokens first.")
        sys.exit(1)

    web_service_token = config_data["web_service_token"]
    return web_service_token


def get_main_js_file(web_service_token):
    '''
    Uses web service token(gtoken) to fetch main.js file for getting the queries' names and corresponding hashed codes.
    '''

    cookie = {
        '_dnt': '1',
        '_gtoken': web_service_token
    }

    response = requests.get(SPLA3_API_URL, cookies=cookie)
    if response.status_code != 200:
        print("Token is invalid.")
        sys.exit(1)

    soup = BeautifulSoup(response.text, "html.parser")
    main_js = soup.select_one("script[src*='static']")
    main_js_url = SPLA3_API_URL + main_js.attrs["src"]
    main_js_response = requests.get(main_js_url, cookies=cookie)

    file_name = main_js.attrs["src"][main_js.attrs["src"].find("main"):]
    main_js_path = os.path.join(data_path, file_name)
    try:
        main_js_file = open(main_js_path, "r")
        main_js_file.close()
        print(f"{file_name} file exists.")
    except (IOError, ValueError):
        main_js_file = open(main_js_path, "w")
        main_js_file.seek(0)
        main_js_file.write(main_js_response.text)
        main_js_file.close()
        print(f"{file_name} file created.")
    return file_name


def get_query_data(file_name):
    '''
    Fetches all query-id pairs and saves them locally for access Spla3 API.
    '''

    main_js_file = open(os.path.join(data_path, file_name), "r")
    content = main_js_file.read()
    main_js_file.close()

    pattern = r"\{id:\"(?P<id>[0-9a-z]{32})\",metadata:\{\},name:\"(?P<name>\w+)\",operationKind:\"(?P<operation>\w+)\""
    match = re.findall(pattern, content)
    match.sort(key=lambda m: (m[2], m[1]))

    # query = {m[1]: Query(m[1], m[0], m[2]) for m in match}
    query_name_id = {m[1]: m[0] for m in match}
    # query_name_operation = {m[1]: m[2] for m in match}

    query_data_path = os.path.join(data_path, "query_hashmap.json")
    try:
        query_data_file = open(query_data_path, "r")
        query_data_file.close()
        print("query_hashmap.json file exists.")
    except (IOError, ValueError):
        query_data_file = open(query_data_path, "w")
        query_data_file.seek(0)
        query_data_file.write(json.dumps(query_name_id, indent=4, separators=(',', ': ')))
        query_data_file.close()
        print("query_hashmap.json file created.")

    return

def get_webview_ver(file_name):
    '''
    TODO: Fetches web view version from main.js file.
    '''


if __name__ == '__main__':
    web_service_token = load_tokens()
    file_name = get_main_js_file(web_service_token)
    get_query_data(file_name)
    # get_webview_ver()

    sys.exit(0)