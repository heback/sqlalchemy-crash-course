# python 콘솔에서 다음 코드 실행

# from connect import engine
# from models.base import Model
# from models.tables import *
# Model.metadata.create_all(engine)

# 실행 결과
# 2023-09-18 17:21:01,826 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2023-09-18 17:21:01,827 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("users")
# 2023-09-18 17:21:01,827 INFO sqlalchemy.engine.Engine [raw sql] ()
# 2023-09-18 17:21:01,827 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("users")
# 2023-09-18 17:21:01,827 INFO sqlalchemy.engine.Engine [raw sql] ()
# 2023-09-18 17:21:01,827 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("preferences")
# 2023-09-18 17:21:01,827 INFO sqlalchemy.engine.Engine [raw sql] ()
# 2023-09-18 17:21:01,828 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("preferences")
# 2023-09-18 17:21:01,828 INFO sqlalchemy.engine.Engine [raw sql] ()
# 2023-09-18 17:21:01,828 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("addresses")
# 2023-09-18 17:21:01,828 INFO sqlalchemy.engine.Engine [raw sql] ()
# 2023-09-18 17:21:01,828 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("addresses")
# 2023-09-18 17:21:01,828 INFO sqlalchemy.engine.Engine [raw sql] ()
# 2023-09-18 17:21:01,828 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("roles")
# 2023-09-18 17:21:01,828 INFO sqlalchemy.engine.Engine [raw sql] ()
# 2023-09-18 17:21:01,828 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("roles")
# 2023-09-18 17:21:01,828 INFO sqlalchemy.engine.Engine [raw sql] ()
# 2023-09-18 17:21:01,828 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("user_roles")
# 2023-09-18 17:21:01,828 INFO sqlalchemy.engine.Engine [raw sql] ()
# 2023-09-18 17:21:01,828 INFO sqlalchemy.engine.Engine PRAGMA temp.table_info("user_roles")
# 2023-09-18 17:21:01,828 INFO sqlalchemy.engine.Engine [raw sql] ()
# 2023-09-18 17:21:01,829 INFO sqlalchemy.engine.Engine
# CREATE TABLE users (
#         id INTEGER NOT NULL,
#         first_name VARCHAR(80) NOT NULL,
#         last_name VARCHAR(80) NOT NULL,
#         email VARCHAR(320) NOT NULL,
#         created_at DATETIME,
#         updated_at DATETIME,
#         PRIMARY KEY (id),
#         UNIQUE (email)
# )
#
#
# 2023-09-18 17:21:01,829 INFO sqlalchemy.engine.Engine [no key 0.00005s] ()
# 2023-09-18 17:21:01,891 INFO sqlalchemy.engine.Engine
# CREATE TABLE roles (
#         id INTEGER NOT NULL,
#         name VARCHAR(80) NOT NULL,
#         slug VARCHAR(80) NOT NULL,
#         PRIMARY KEY (id),
#         UNIQUE (slug)
# )
#
#
# 2023-09-18 17:21:01,891 INFO sqlalchemy.engine.Engine [no key 0.00010s] ()
# 2023-09-18 17:21:01,892 INFO sqlalchemy.engine.Engine
# CREATE TABLE preferences (
#         id INTEGER NOT NULL,
#         language VARCHAR(80) NOT NULL,
#         currency VARCHAR(3) NOT NULL,
#         user_id INTEGER NOT NULL,
#         created_at DATETIME,
#         updated_at DATETIME,
#         PRIMARY KEY (id),
#         FOREIGN KEY(user_id) REFERENCES users (id) ON DELETE CASCADE
# )
#
#
# 2023-09-18 17:21:01,892 INFO sqlalchemy.engine.Engine [no key 0.00006s] ()
# 2023-09-18 17:21:01,900 INFO sqlalchemy.engine.Engine CREATE UNIQUE INDEX ix_preferences_user_id ON preferences (user_id)
# 2023-09-18 17:21:01,900 INFO sqlalchemy.engine.Engine [no key 0.00006s] ()
# 2023-09-18 17:21:01,902 INFO sqlalchemy.engine.Engine
# CREATE TABLE addresses (
#         id INTEGER NOT NULL,
#         road_name VARCHAR(80) NOT NULL,
#         postcode VARCHAR(80) NOT NULL,
#         city VARCHAR(80) NOT NULL,
#         user_id INTEGER NOT NULL,
#         created_at DATETIME,
#         updated_at DATETIME,
#         PRIMARY KEY (id),
#         FOREIGN KEY(user_id) REFERENCES users (id) ON DELETE CASCADE
# )
#
#
# 2023-09-18 17:21:01,902 INFO sqlalchemy.engine.Engine [no key 0.00004s] ()
# 2023-09-18 17:21:01,903 INFO sqlalchemy.engine.Engine CREATE INDEX ix_addresses_user_id ON addresses (user_id)
# 2023-09-18 17:21:01,903 INFO sqlalchemy.engine.Engine [no key 0.00004s] ()
# 2023-09-18 17:21:01,904 INFO sqlalchemy.engine.Engine
# CREATE TABLE user_roles (
#         user_id INTEGER NOT NULL,
#         role_id INTEGER NOT NULL,
#         created_at DATETIME,
#         updated_at DATETIME,
#         PRIMARY KEY (user_id, role_id),
#         FOREIGN KEY(user_id) REFERENCES users (id) ON DELETE CASCADE,
#         FOREIGN KEY(role_id) REFERENCES roles (id) ON DELETE CASCADE
# )
#
#
# 2023-09-18 17:21:01,904 INFO sqlalchemy.engine.Engine [no key 0.00008s] ()
# 2023-09-18 17:21:01,904 INFO sqlalchemy.engine.Engine COMMIT
