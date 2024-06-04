"""
This module contains a Caribou migration.

Migration Name: planned_database 
Migration Version: 20240604110957
"""

def upgrade(connection):
    # add your upgrade step here
    topics_table_sql = """
    CREATE TABLE IF NOT EXISTS topics
    (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        link TEXT NOT NULL
    )
    """
    images_table_sql = """
    CREATE TABLE IF NOT EXISTS images
    (
        id INTEGER PRIMARY KEY,
        title TEXT,
        link TEXT NOT NULL,
        idTopic INT,
        FOREIGN KEY (idTopic) REFERENCES topics (id)
    )
    """
    connection.execute(topics_table_sql)
    connection.commit()
    connection.execute(images_table_sql)
    connection.commit()

def downgrade(connection):
    # add your downgrade step here
    connection.execute('DROP TABLE favorites')
    connection.commit()