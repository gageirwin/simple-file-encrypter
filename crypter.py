import os
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(file_path  + '.crypt', 'wb') as f:
        f.write(encrypted_data)

    os.remove(file_path)

def decrypt_file(file_path, key):
    if file_path[-6:] != '.crypt':
        raise f"File: {file_path} was not encrypted by crypter.py"

    with open(file_path, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(data)

    with open(file_path[:-6], 'wb') as f:
        f.write(decrypted_data)

    os.remove(file_path)

from args import get_args


if __name__ == '__main__':
    args = get_args()

    if args.encrypt:
        
        encrypt_file(args.file_path, args.encrypt)
        print('File encrypted successfully.')
    else:
        decrypt_file(args.file_path, args.decrypt)
        print('File decrypted successfully.')