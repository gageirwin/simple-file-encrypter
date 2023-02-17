import argparse
import os
import base64
import binascii

def get_args():
    parser = argparse.ArgumentParser(description='crypter.py is a simple file encypter / decrypter cli script')
    parser.add_argument('file_path', type=str, help='Path to file', metavar='FILE_PATH')
    parser.add_argument('--encrypt', action='store_true', default=False, help='encrypt file')
    parser.add_argument('--decrypt', type=str, default='', help='key to decrypt', metavar='KEY')
    args = parser.parse_args()

    if not os.path.exists(args.file_path):
        parser.error(f"File path does not exist: {args.file_path}")

    if args.encrypt and args.decrypt:
        parser.error("Only one of --encrypt or --decrypt can be provided")

    if not args.encrypt and not args.decrypt:
        parser.error("At least one of --encrypt or --decrypt must be provided")

    if args.encrypt:
        from cryptography.fernet import Fernet
        args.encrypt = Fernet.generate_key()
        print(f"Randomly generated key: {args.encrypt.decode('utf-8')}")

    if args.decrypt:
        try:
            args.decrypt = args.decrypt.encode('utf-8')
            valid = base64.urlsafe_b64decode(args.decrypt)
        except binascii.Error:
            parser.error("Fernet key must be 32 url-safe base64-encoded bytes.")
        if len(valid) != 32:
            parser.error("Fernet key must be 32 url-safe base64-encoded bytes.")

    return args

