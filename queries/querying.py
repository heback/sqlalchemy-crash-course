from sqlalchemy import desc
from models.tables import User, Role

# all_users = User.query.all()
# print(all_users)
# first_user = User.query.first()
# print(first_user)

# johns = User.query.filter_by(first_name="John").all()
# johns = User.query.filter(User.first_name == "John").all()
#
# gmail_users = User.query.filter(User.email.ilike("%@gmail.com")).all()
# ilike는 대소문자 구분 안함.
# gmail_users = User.query.filter(User.email.like("%@gmail.com")).all()

# super_admins = (
#     User.query
#     .join(User.roles)
#     .filter(Role.slug == "super-admin")
#     .all()
# )
# for user in super_admins:
#     print(user)

#
# users_by_name = (
#     User.query
#     .order_by(User.first_name)
#     .all()
# )

# users_by_name_desc = (
#     User.query
#     .order_by(desc(User.first_name))
#     .all()
# )
#
# users_by_names_desc = (
#     User.query
#     .order_by(desc(User.first_name))
#     .order_by(desc(User.last_name))
#     .all()
# )
#
# first_three_users = User.query.limit(3).all()
#
# skip_three_users = User.query.offset(3).all()
#
# num_of_users = User.query.count()
#
# print(num_of_users)
