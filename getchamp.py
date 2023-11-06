import requests
import json

url = "http://ddragon.leagueoflegends.com/cdn/13.21.1/data/en_US/champion.json"

try:
    response = requests.get(url)
    data = response.json()

    # Lấy thông tin sau "id"
    champions_info = {key: value for key, value in data["data"].items()}

    # Ghi dữ liệu ra file JSON mới
    with open('champions_info_output.json', 'w') as output_file:
        json.dump(champions_info, output_file, indent=2)

    print("Thông tin sau 'id' đã được xuất ra file champions_info_output.json.")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
