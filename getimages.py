import os
import requests
import pandas as pd

url = "http://ddragon.leagueoflegends.com/cdn/13.21.1/data/en_US/champion.json"
image_base_url = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-icons/"

try:
    response = requests.get(url)
    data = response.json()

    # Tạo DataFrame từ dữ liệu
    champions_data = data["data"]
    champions_list = [{"id": champ["id"], "key": champ["key"], "full": champ.get("full", "")} for champ in champions_data.values()]
    df = pd.DataFrame(champions_list)

    # Thêm chuỗi ".png" vào cột "id"
    df['id'] = df['id'] + '.png'

    # Ghi DataFrame ra file Excel
    df.to_excel('champions_info_output.xlsx', index=False)

    # Tải hình và lưu vào thư mục 'images'
    image_folder = 'images'
    os.makedirs(image_folder, exist_ok=True)

    for key in df['key']:
        image_url = image_base_url + str(key) + '.png'
        image_path = os.path.join(image_folder, str(key) + '.png')

        image_response = requests.get(image_url)
        with open(image_path, 'wb') as image_file:
            image_file.write(image_response.content)

    print("Thông tin từ thuộc tính 'id', 'key', 'full' và hình đã được xuất và tải xuống.")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
