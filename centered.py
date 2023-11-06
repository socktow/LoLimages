import os
import requests
import json

# Đọc danh sách "id" từ file JSON
with open('champions_ids_output.json', 'r') as file:
    champions_ids = json.load(file)['id']

# URL cơ bản cho splash-art centered
base_url = "https://cdn.communitydragon.org/13.21.1/champion/"

# Tạo thư mục để lưu splash-art
image_folder = 'centered'
os.makedirs(image_folder, exist_ok=True)

try:
    for champion_id in champions_ids:
        # Tạo URL hoàn chỉnh cho splash-art centered
        image_url = f"{base_url}{champion_id}/splash-art/centered"

        # Tạo đường dẫn để lưu splash-art
        image_path = os.path.join(image_folder, f"{champion_id}_centered.jpg")

        # Tải splash-art từ URL và lưu vào thư mục nếu file không tồn tại
        if not os.path.exists(image_path):
            image_response = requests.get(image_url)
            with open(image_path, 'wb') as image_file:
                image_file.write(image_response.content)

    print("Toàn bộ splash-art centered của mỗi champion đã được tải xuống và lưu vào thư mục 'centered'.")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
