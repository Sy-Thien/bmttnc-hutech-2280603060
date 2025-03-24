from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

def generate_dh_parameters():
    """Tạo tham số Diffie-Hellman với generator=2 và kích thước khóa 2048 bit"""
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    return parameters

def generate_server_key_pair(parameters):
    """Tạo cặp khóa riêng tư và công khai cho máy chủ"""
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def main():
    """Hàm chính để tạo và lưu khóa công khai"""
    parameters = generate_dh_parameters()
    private_key, public_key = generate_server_key_pair(parameters)

    # Lưu khóa công khai vào tệp tin
    with open("server_public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

if __name__ == "__main__":
    main()
