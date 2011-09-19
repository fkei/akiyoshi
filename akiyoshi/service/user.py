from db.model.user import User
from db.access.user import userAccess

from lib.crypt import sha1encrypt, sha1compare

class UserService:

    def login(self, orm, email, password):
        if not email and password:
            return None

        _r = orm.query(User).filter(User.email == email).first()

        if _r is None:
            return None

        if sha1compare(_r.password, password, _r.salt) is True:
            return _r
        else:
            return None

    def getUser(self, session, email):
        return userAccess.findByemail(session, email)

    def merge(self, session, email, plain, nickname):
        (password, salt) = sha1encrypt(plain)
        user = User(email, password, salt, nickname)

        return userAccess.merge(session, user)

userService = UserService()
