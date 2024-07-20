create_user_table="""CREATE TABLE IF NOT EXISTS users(
id SERIAL PRIMARY KEY,
full_name VARCHAR(55),
phone_number VARCHAR(31),
chat_id VARCHAR(55) UNIQUE NOT NULL,
lang VARCHAR(3) DEFAULT 'en'
    )"""


insert_user = """INSERT INTO users(full_name,phone_number,chat_id,lang) VALUES(%s,%s,%s,%s)"""
