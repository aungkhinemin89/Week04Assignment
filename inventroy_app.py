from Category import Category
from Stock import Stock


# Method(01)


def addNewCategory():
    category = Category()
    category.name = input("Enter category name for new category : \n")
    category.save()
    category.display()

# Method(02)


def addNewStock():
    stock = Stock()
    stock.name = input("Enter stock name for new stock : \n")
    stock.sale_price = input("Enter sale price for new stock : \n")
    stock.purchase_price = input("Enter purchase price for new stock : \n")
    displayAllCategory()
    stock.stock_in_qty = 0
    stock.stock_out_qty = 0
    stock.category_id = input("Enter category code for new stock : \n")
    stock.save()

# Other Method


def getStockByID(id):
    stock=Stock.find(id)
    stock.category=Category.find(stock.category_id)
    return stock
    

# # Method(03)


# def stockInEntryByStockID():
#     displayAllStockBalanceList()
#     stock_id = input("Plz select stock id : ")
#     stock = getStockByID(stock_id)
#     user_choice = input(
#         f"Are you sure you want to receive for {stock[1]} ? y/n \n : ")
#     if user_choice == "y":
#         qty = int(input(
#             f"How many quantity do you want to  receivce for {stock[1]}? : \n"))
#         newQty = qty+stock[4]
#         cursor.execute(
#             "update stocks set stock_in_qty = %s where id=%s", [newQty, stock_id])
#         mydb.commit()
#         displayAllStockBalanceList()

# # Method(04)


# def stockOutEntryByStockID():
#     displayAllStockBalanceList()
#     stock_id = input("Plz select stock id : ")
#     stock = getStockByID(stock_id)
#     user_choice = input(
#         f"Are you sure you want to issue for {stock[1]} ? y/n \n : ")
#     if user_choice == "y":
#         qty = int(input(
#             f"How many quantity do you want to  issue for {stock[1]}? : \n"))
#         newQty = qty+stock[5]
#         cursor.execute(
#             "update stocks set stock_out_qty = %s where id=%s", [newQty, stock_id])
#         mydb.commit()
#         displayAllStockBalanceList()

# Method(05)


def displayAllStockBalanceList():
    stock_list=Stock.get()
    for stock in stock_list:
        stock.display()
    # cursor.execute(
    #     "select s.*,c.name from stocks s left join categories c on s.category_id=c.id")
    # for stock in cursor.fetchall():
    #     print(f"[{stock[0]}] - {stock[1]} - {stock[2]} - {stock[3]} - {stock[4]} - {stock[5]} - {stock[6]}=={stock[7]}")

# Method(06)


def displayStockBalanceListByStockID():
    stock_id = input("Plz select stock id : ")
    stock=getStockByID(stock_id)
    stock.display()
    # oneStock = getStockByID(stock_id)
    # user_choice = input(
    #     f"Are you sure you want to see for stockID={oneStock[0]}({oneStock[1]}) ? y/n \n : ")
    # if user_choice == "y":
    #     cursor.execute("select s.*,c.name from stocks s left join categories c on s.category_id=c.id where s.id=%s",[stock_id])
    #     stock=cursor.fetchone()
    #     print(f"[{stock[0]}] - {stock[1]} - {stock[2]} - {stock[3]} - {stock[4]} - {stock[5]} - {stock[6]}=={stock[7]}")

# Method(07)


def displayStockBalanceListByCategoryID():
    displayAllCategory()
    selected_cat=input("Select Category Id : \n")
    stock_list = Stock.getByCategory(selected_cat)
    for stock in stock_list:
        stock.display()    
    # cursor.execute("select * from stocks s left join categories c on s.category_id=c.id where c.id=%s",[selected_cat])
    # stocks=cursor.fetchall()
    # for stock in stocks:
    #     print(f"[{stock[0]}] - {stock[1]} - {stock[2]} - {stock[3]} - {stock[4]} - {stock[5]} - {stock[6]}=={stock[7]}")

# Method(8)


def displayAllCategory():
    category_list = Category.get()
    for category in category_list:
        category.display()
        # print(type(category))
        # print(f"[{category[0]}] - {category[1]}")


def displayMenu():
    try:
        selected_option = int(input(
            f'Please select the action you want to do.\n'
            f'[1] Add New Category\n'
            f'[2] Add New Stock\n'
            # f'[3] Stock Receive Quantity Entry\n'
            # f'[4] Stock Issue Quantity Entry\n'
            f'[5] View All Stock Balance \n'
            f'[6] View Stock Balance by Stock ID \n'
            f'[7] View Stock Balance by Category ID \n'
            f'[8] View All Category \n : '
        ))
        if selected_option == 1:
            addNewCategory()
        elif selected_option == 2:
            addNewStock()
        # elif selected_option == 3:
        #     stockInEntryByStockID()
        # elif selected_option == 4:
        #     stockOutEntryByStockID()
        elif selected_option == 5:
            displayAllStockBalanceList()
        elif selected_option==6:
            displayStockBalanceListByStockID()
        elif selected_option==7:
            displayStockBalanceListByCategoryID()
        elif selected_option == 8:
            displayAllCategory()

        user_choice = input("Do you want to go back to menu? : y/n \n")
        if(user_choice == "y"):
            displayMenu()
        else:
            print("Bye Bye")
    except KeyboardInterrupt:
        print("Bye Bye")


displayMenu()
