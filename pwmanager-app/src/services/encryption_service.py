import bcrypt

class EncryptionService:
    """Luokka joka mahdollistaa salasanojen encryptoinnin bcrypt kirjastolla.
    """

    def __init__(self, salt_number=10):
        """Luokan konstruktori, joka asettaa automaattisesti salt_rounds
        parametriksi 10, mutta tätä voi muuttaa jos haluaa kun luodaan
        luokan instanssi.

        Args:
            salt_number (int, optional): salt_rounds parametri bcryptin hashpw metodille.
            Defaults to 10.
        """

        self._salt_number = salt_number

    def encrypt_password(self, password_string):
        """Encryptaa annetun merkkijonon bcryptin hashpw metodilla.

        Args:
            password_string (merkkijono): käyttäjän antama salasana

        Returns:
            merkkijono: palauttaa encryptatun merkkijonon
        """

        encoded_password = self._encode_password(password_string)
        encrypted_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt(self._salt_number))
        return encrypted_password

    def password_match_comparison(self, password_string, hash_string):
        """Vertaa annettua merkkijonoa ja annettua encryptattua hashia,
        ja kertoo vastaavatko nämä toisiaan.

        Args:
            password_string (merkkijono): salasana jota verrataan
            hash_string (merkkijono): salasana hash joka on otettu tietokannasta

        Returns:
            boolean: palauttaa True jos matchaavat, False jos eivät.
        """

        encoded_password = self._encode_password(password_string)
        return bcrypt.checkpw(encoded_password, hash_string)

    def _encode_password(self, password_string):
        encoded_password = password_string.encode()
        return encoded_password

encryption_service = EncryptionService()
