import sqlite3

class ProductManager:
    def __init__(self, db_path='products.db'):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY,
                product_name TEXT,
                price REAL
            )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def insert_product(self, product_name, price):
        query = 'INSERT INTO products (product_name, price) VALUES (?, ?)'
        self.conn.execute(query, (product_name, price))
        self.conn.commit()

    def update_product(self, product_id, product_name, price):
        query = 'UPDATE products SET product_name=?, price=? WHERE product_id=?'
        self.conn.execute(query, (product_name, price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        query = 'DELETE FROM products WHERE product_id=?'
        self.conn.execute(query, (product_id,))
        self.conn.commit()

    def select_all_products(self):
        query = 'SELECT * FROM products'
        cursor = self.conn.execute(query)
        return cursor.fetchall()

# 샘플 데이터 추가
product_manager = ProductManager()

sample_data = [
    ("Laptop", 1200.0),
    ("Smartphone", 800.0),
    ("Headphones", 150.0),
    ("Mouse", 30.0),
    ("Keyboard", 50.0),
    ("Monitor", 300.0),
    ("Tablet", 500.0),
    ("Printer", 200.0),
    ("Camera", 700.0),
    ("Speakers", 100.0)
]

for data in sample_data:
    product_manager.insert_product(*data)

# 모든 제품 출력
all_products = product_manager.select_all_products()
for product in all_products:
    print(product)

# 제품 업데이트
product_manager.update_product(1, "Updated Laptop", 1300.0)

# 업데이트 후 모든 제품 다시 출력
all_products_after_update = product_manager.select_all_products()
for product in all_products_after_update:
    print(product)

# 제품 삭제
product_manager.delete_product(3)

# 삭제 후 모든 제품 다시 출력
all_products_after_delete = product_manager.select_all_products()
for product in all_products_after_delete:
    print(product)
