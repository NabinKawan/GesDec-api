from pony.orm import Database, PrimaryKey, Required
import os
db = Database()
print("init db")

# def init_local_db():
#     db.bind(provider='sqlite', filename='db.db',create_db=True)
#     db.generate_mapping(create_tables=True)

def init_db():
    db.bind(provider=os.getenv('DB_PROVIDER'),
                 user=os.getenv('DB_USER'),
                 password=os.getenv('DB_PASSWORD'),
                 host=os.getenv('DB_HOST'),
                 port=int(os.getenv('DB_PORT')),
                 database=os.getenv('DB_DATABASE'))
    db.generate_mapping(create_tables=True)

if __name__ == '__main__':
    init_db()
    # db.drop_all_tables(with_all_data=True)