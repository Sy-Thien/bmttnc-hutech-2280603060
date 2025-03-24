import hashlib

def calculate_md5(input_string):
    """Tính toán mã băm MD5 của một chuỗi"""
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

# Nhập chuỗi từ người dùng
input_string = input("Nhập chuỗi cần băm: ")

# Tính toán mã MD5
md5_hash = calculate_md5(input_string)

# In kết quả
print("Mã băm MD5 của chuỗi '{}' là: {}".format(input_string, md5_hash))
