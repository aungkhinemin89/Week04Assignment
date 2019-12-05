from Database import Database
from Category import Category


class Stock:
    def __init__(self, tuple_data=None):
        if(tuple_data):
            self.id = tuple_data[0]
            self.name = tuple_data[1]
            self.sale_price = tuple_data[2]
            self.purchase_price = tuple_data[3]
            self.stock_in_qty = tuple_data[4]
            self.stock_out_qty = tuple_data[5]
            self.category_id = tuple_data[6]
            self.category = Category.find(self.category_id)

    def save(self):
        Database._cursor.execute("insert into stocks(name, sale_price, purchase_price,stock_in_qty,stock_out_qty,category_id)values( %s, %s, %s, 0, 0, %s)", [
                                 self.name, self.sale_price, self.purchase_price, self.category_id])
        Database._db.commit()
        self.id = Database._cursor.lastrowid
        self.category = Category.find(self.category_id)
        self.display()

        # self.display()

    def display(self):
        # print(self.category)
        # print("test")
        print(f"[{self.id}] - {self.name} - {self.sale_price} - {self.purchase_price} - {self.stock_in_qty} - {self.stock_out_qty} - {self.category.name}=={self.category_id}")

    @staticmethod
    def find(id):
        Database._cursor.execute("select * from stocks where id=%s", [id])
        stockById = Database._cursor.fetchone()
        return Stock(stockById)

    @staticmethod
    def get():
        Database._cursor.execute(
            "select s.*,c.name from stocks s left join categories c on s.category_id=c.id")
        stock_list = []
        for stockTuple in Database._cursor.fetchall():
            stock = Stock(stockTuple)
            stock_list.append(stock)
        return stock_list

    @staticmethod
    def getByCategory(category_id):
        Database._cursor.execute(
            "select * from stocks where category_id=%s", [category_id])
        stock_list = []
        for stockTuple in Database._cursor.fetchall():
            stock = Stock(stockTuple)
            stock_list.append(stock)
        return stock_list
