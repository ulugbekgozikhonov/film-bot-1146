create_user_table="""CREATE TABLE IF NOT EXISTS users(
id SERIAL PRIMARY KEY,
full_name VARCHAR(55),
phone_number VARCHAR(31),
chat_id BIGINT UNIQUE NOT NULL,
lang VARCHAR(3) DEFAULT 'en'
    )"""


insert_user = """INSERT INTO users(full_name,phone_number,chat_id,lang) VALUES(%s,%s,%s,%s)"""

get_user_by_chat_id = "SELECT * FROM users WHERE chat_id=%s"


create_channels_table = """CREATE TABLE IF NOT EXISTS channels(
    id SERIAL PRIMARY KEY,
    url VARCHAR,
    admin_id INTEGER NOT NULL,
    FOREIGN KEY (admin_id) REFERENCES users (id)
    )"""
    
get_channles = "SELECT * FROM channels"