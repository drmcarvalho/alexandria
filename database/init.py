create_tables_stmt = [
    """CREATE TABLE IF NOT EXISTS file (id INTEGER PRIMARY KEY AUTOINCREMENT, path TEXT NOT NULL, comment TEXT);""",
    """CREATE TABLE IF NOT EXISTS tag (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)""",
    """CREATE TABLE IF NOT EXISTS FileTag (id_file INTEGER NOT NULL, id_tag INTEGER NOT NULL)""",
]


def create_tables():
    for stmt in create_tables_stmt:
        pass
