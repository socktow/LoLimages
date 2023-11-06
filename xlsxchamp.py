import requests
import pandas as pd

url = "http://ddragon.leagueoflegends.com/cdn/13.21.1/data/en_US/champion.json"

try:
    response = requests.get(url)
    data = response.json()

    # Tạo DataFrame từ dữ liệu
    champions_data = data["data"]
    champions_list = []

    for champ in champions_data.values():
        champ_info = {"id": champ["id"], "key": champ["key"]}
        if "full" in champ:
            champ_info["full"] = champ["full"]
        else:
            champ_info["full"] = ""
        champions_list.append(champ_info)

    df = pd.DataFrame(champions_list)

    # Ghi DataFrame ra file Excel
    df.to_excel('champions_info_output.xlsx', index=False)

    print("Thông tin từ thuộc tính 'id', 'key', 'full' đã được xuất ra file champions_info_output.xlsx.")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
