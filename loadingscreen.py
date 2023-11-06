import os
import requests
import json

# Đọc danh sách "id" từ file JSON
with open('champions_ids_output.json', 'r') as file:
    champions_ids = json.load(file)['id']

# URL cơ bản cho hình loading screen
base_url = "http://ddragon.leagueoflegends.com/cdn/img/champion/loading/"

# Tạo thư mục để lưu hình ảnh
image_folder = 'loading-screen'
os.makedirs(image_folder, exist_ok=True)

try:
    for champion_id in champions_ids:
        # Tạo URL hoàn chỉnh cho hình loading screen
        image_url = f"{base_url}{champion_id}_0.jpg"

        # Tạo đường dẫn để lưu hình ảnh
        image_path = os.path.join(image_folder, f"{champion_id}_0.jpg")

        # Tải hình ảnh từ URL và lưu vào thư mục
        image_response = requests.get(image_url)
        with open(image_path, 'wb') as image_file:
            image_file.write(image_response.content)

    print("Toàn bộ hình loading screen đã được tải xuống và lưu vào thư mục 'loading-screen'.")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
