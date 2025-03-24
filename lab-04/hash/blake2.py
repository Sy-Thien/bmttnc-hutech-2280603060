import hashlib

def blake2(message):
    """Tính toán mã băm BLAKE2b của một chuỗi"""
    blake2_hash = hashlib.blake2b(digest_size=64)  # Tạo đối tượng BLAKE2b với kích thước băm 64 byte
    blake2_hash.update(message)  # Cập nhật dữ liệu vào hàm băm
    return blake2_hash.digest()  # Trả về giá trị băm dạng bytes

def main():
    # Nhập chuỗi từ người dùng
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')

    # Tính toán giá trị băm BLAKE2b
    hashed_text = blake2(text)

    # Hiển thị kết quả
    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))
    print("BLAKE2 Hash:", hashed_text.hex())  # Chuyển đổi sang dạng hex

if __name__ == "__main__":
    main()
