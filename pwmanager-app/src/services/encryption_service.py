import bcrypt

class EncryptionService:
    def __init__(self, salt_number=10):
        self._salt_number = salt_number

    def encrypt_password(self, password_string):
        encoded_password = self._encode_password(password_string)
        encrypted_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt(self._salt_number))
        return encrypted_password
    
    def password_match_comparison(self, password_string, hash_string):
        encoded_password = self._encode_password(password_string)
        #encoded_hash = self._encode_password(hash_string)
        return bcrypt.checkpw(encoded_password, hash_string)

    def _encode_password(self, password_string):
        encoded_password = password_string.encode()
        return encoded_password

encryption_service = EncryptionService()