import hashlib

def calculate_sha256_hash(data):
    """Tính toán mã băm SHA-256 của một chuỗi"""
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))  # Chuyển đổi chuỗi thành bytes và cập nhật vào đối tượng hash
    return sha256_hash.hexdigest()  # Trả về biểu diễn hex của giá trị băm

# Nhập dữ liệu từ người dùng
data_to_hash = input("Nhập dữ liệu để hash bằng SHA-256: ")

# Tính toán giá trị băm SHA-256
hash_value = calculate_sha256_hash(data_to_hash)

# Hiển thị kết quả
print("Giá trị hash SHA-256:", hash_value)
