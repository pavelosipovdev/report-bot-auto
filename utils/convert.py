# Импортируйте библиотеку для кодирования в Base64
import base64
import json


# Создайте функцию, которая кодирует файл и возвращает результат.
def encode_file(image):
    with open(image, 'rb') as image_file:
        base64_bytes = base64.b64encode(image_file.read())

    return base64_bytes


def convert_json_vin(image):
    text = encode_file(image)
    # print(text)

    with open("body_vin.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        data["analyze_specs"][0]["content"] = str(text)[2:-1]
        # print(data)
        json_object = json.loads(str(data).replace("\'", "\""))
    with open("body_vin.json", 'w') as fp:
        json.dump(json_object, fp, indent=2)


def convert_json_japan(image):
    text = encode_file(image)
    # print(text)

    with open("body_japan.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        data["analyze_specs"][0]["content"] = str(text)[2:-1]
        # print(data)
        json_object = json.loads(str(data).replace("\'", "\""))
    with open("body_japan.json", 'w') as fp:
        json.dump(json_object, fp, indent=2)
