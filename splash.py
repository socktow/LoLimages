import os
import requests

# URL cơ bản cho hình splash
base_url = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-splashes/"

# Tạo thư mục để lưu hình ảnh
image_folder = 'splashes'
os.makedirs(image_folder, exist_ok=True)

try:
    for folder_number in range(1, 100):  # Thay thế 100 bằng số folder bạn muốn lấy
        # Tạo URL hoàn chỉnh cho hình splash
        image_url = f"{base_url}{folder_number}/{folder_number * 1000}.jpg"

        # Tạo đường dẫn để lưu hình ảnh
        image_path = os.path.join(image_folder, f"{folder_number * 1000}.jpg")

        # Tải hình ảnh từ URL và lưu vào thư mục nếu file không tồn tại
        if not os.path.exists(image_path):
            image_response = requests.get(image_url)
            with open(image_path, 'wb') as image_file:
                image_file.write(image_response.content)

    print("Toàn bộ hình splash đã được tải xuống và lưu vào thư mục 'splashes'.")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
