from models.connect import session
from models.tables import User

user = User.query.first()

print(user)


session.delete(user)
session.commit()


user = User.query.first()

print(user)