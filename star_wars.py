import requests, os.path, json

baseUrl = "https://swapi.dev/api/"

def writefile(file, content):
    try:
        tempFile = open(file, "w")
        tempFile.write(content)
        tempFile.close()
    except:
        return False

    return True

def readFile(file):
    if not os.path.isfile(file):
        return False

    file = open(file, "r")
    content = file.read()
    file.close()
    return content

def getJson(url):
    fileCacheJson = url + '.json'
    jsonFile = readFile(fileCacheJson)
    if jsonFile:
        return json.loads(jsonFile)

    response = requests.get(baseUrl + url)

    if response.status_code != 200:
        print('erro')

    jsonResponse = response.json()
    pageCount = len(jsonResponse["results"])
    total = jsonResponse["count"]
    print(f"get ... {url} {pageCount}/{total}")
    writefile(fileCacheJson, response.text)

    return jsonResponse

print('getting jsons...')
people = getJson("people")
films = getJson("films")
species = getJson("species")
vehicles = getJson("vehicles")
starships = getJson("starships")
print('finish')