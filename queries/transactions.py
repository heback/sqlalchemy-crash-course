from models.connect import session
from models.tables import User

user = User(
    first_name="John",
    last_name="Smith",
    email="jsmith@gmail.com",
)

session.add(user)

raise Exception("Something went wrong")

preference = Preference(
    language="English",
    currency="GBP",
)

preference.user = user
session.commit()
