from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def generate_client_key_pair(parameters):
    """Tạo cặp khóa riêng tư và công khai cho client"""
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def derive_shared_secret(private_key, server_public_key):
    """Tính toán khóa chung từ khóa riêng tư của client và khóa công khai của server"""
    shared_key = private_key.exchange(server_public_key)
    return shared_key

def main():
    """Hàm chính để tải khóa công khai của server và tạo khóa chung"""
    # Tải khóa công khai của server từ file
    with open("server_public_key.pem", "rb") as f:
        server_public_key = serialization.load_pem_public_key(f.read())

    # Lấy tham số Diffie-Hellman từ khóa công khai của server
    parameters = server_public_key.parameters()

    # Tạo cặp khóa client
    private_key, public_key = generate_client_key_pair(parameters)

    # Tính toán khóa chung
    shared_secret = derive_shared_secret(private_key, server_public_key)

    print("Shared Secret:", shared_secret.hex())

if __name__ == "__main__":
    main()
