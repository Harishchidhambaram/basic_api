from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'])

class Hash():
    def bcrypt(password):
        return pwd_cxt.hash(password)
    def verfiy(password,encrypted_password):
        return pwd_cxt.verify(password,encrypted_password)
