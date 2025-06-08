from db_config import get_connection

def fetch_all_products():
    conn = get_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT p.product_id, p.product_name, p.category, p.price, s.quantity,
                d.discount_percent, d.start_date, d.end_date
            FROM products p
            LEFT JOIN stock s ON p.product_id = s.product_id
            LEFT JOIN discounts d ON p.product_id = d.product_id
                AND CURDATE() BETWEEN d.start_date AND d.end_date;
        """)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    return []

def add_product(name, category, price):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO products (product_name, category, price) VALUES (%s, %s, %s)",
            (name, category, price)
        )
        conn.commit()
        cursor.close()
        conn.close()

def update_stock(product_id, quantity):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        # Check if stock exists
        cursor.execute("SELECT * FROM stock WHERE product_id = %s", (product_id,))
        if cursor.fetchone():
            cursor.execute("UPDATE stock SET quantity = %s WHERE product_id = %s", (quantity, product_id))
        else:
            cursor.execute("INSERT INTO stock (product_id, quantity) VALUES (%s, %s)", (product_id, quantity))
        conn.commit()
        cursor.close()
        conn.close()

def update_discount(product_id, discount_percent, start_date, end_date):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        # For simplicity, insert new discount without overlap checks
        cursor.execute(
            "INSERT INTO discounts (product_id, discount_percent, start_date, end_date) VALUES (%s, %s, %s, %s)",
            (product_id, discount_percent, start_date, end_date)
        )
        conn.commit()
        cursor.close()
        conn.close()