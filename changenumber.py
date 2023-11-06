import os
import pandas as pd

# Đọc DataFrame từ file Excel
df_info = pd.read_excel('champions_info_output.xlsx')

# Thư mục chứa các ảnh
image_folder = 'centered'

# Duyệt qua các tệp trong thư mục
for filename in os.listdir(image_folder):
    if filename.endswith("_centered.jpg"):
        # Tách id từ tên tệp
        champion_id = filename.split("_")[0]

        # Kiểm tra xem id có trong thông tin từ champions_info_output.xlsx không
        if champion_id in df_info['id'].values:
            # Lấy key tương ứng
            key = df_info.loc[df_info['id'] == champion_id, 'key'].iloc[0]

            # Tạo tên mới
            new_filename = f"{key}.jpg"

            # Đổi tên tệp
            os.rename(os.path.join(image_folder, filename), os.path.join(image_folder, new_filename))

print("Đã đổi tên các ảnh thành công.")
