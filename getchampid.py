import json

# Đọc nội dung từ file JSON
with open('champions_info_output.json', 'r') as file:
    data = json.load(file)

# Tạo một đối tượng mới có cấu trúc {"id": ["Aatrox", "Ahri", "Akali", ...]}
result = {"id": list(data.keys())}

# Ghi dữ liệu mới ra file JSON mới
with open('champions_ids_output.json', 'w') as output_file:
    json.dump(result, output_file, indent=2)

print("Thông tin từ thuộc tính 'id' đã được xuất ra file champions_ids_output.json.")
