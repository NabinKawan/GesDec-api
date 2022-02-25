from pony.orm import Database, PrimaryKey, Required

db = Database()
print("init db")

def init_db():
    db.bind(provider='sqlite', filename='db.db',create_db=True)
    db.generate_mapping(create_tables=True)


if __name__ == '__main__':
    init_db()
    # db.drop_all_tables(with_all_data=True)