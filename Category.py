from Database import Database


class Category:
    id = None
    name = None

    def __init__(self, turple_data=None):
        if (turple_data):
            self.id = turple_data[0]
            self.name = turple_data[1]
            print("Category Class is initialized.")

    def save(self):
        Database._cursor.execute(
            "insert into categories(name)values(%s)", [self.name])
        Database._db.commit()
        print(Database._cursor.lastrowid)
        self.id = Database._cursor.lastrowid

    def display(self):
        print(f"[{self.id}] - {self.name}")

    @staticmethod
    def find(id):
        Database._cursor.execute(
            "select * from categories where id=%s", [id])
        result = Database._cursor.fetchone()
        return Category(result)

    @staticmethod
    def get():
        Database._cursor.execute("select * from categories")
        # category_list=Database._cursor.fetchall()
        # print(type(category_list))
        # return category_list
        category_list = []
        for categoryTuple in Database._cursor.fetchall():
            category = Category(categoryTuple)
            category_list.append(category)
        return category_list


