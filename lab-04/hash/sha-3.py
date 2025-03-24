from Crypto.Hash import SHA3_256

def sha3(message):
    """Tính toán mã băm SHA-3 256-bit của một chuỗi"""
    sha3_hash = SHA3_256.new()
    sha3_hash.update(message)
    return sha3_hash.digest()  # Trả về giá trị băm dạng bytes

def main():
    # Nhập chuỗi từ người dùng
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    
    # Tính toán giá trị băm SHA-3
    hashed_text = sha3(text)

    # Hiển thị kết quả
    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))
    print("SHA-3 Hash:", hashed_text.hex())  # Chuyển đổi sang dạng hex

if __name__ == "__main__":
    main()
