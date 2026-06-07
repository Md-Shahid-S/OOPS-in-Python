class DatabaseConnection:
    """
    A database connection that automatically opens and closes.
    Works with Python's 'with' statement via __enter__ and __exit__.
    """

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = None
        self.query_count = 0

    # Called when 'with' block starts — setup goes here
    # Must return the resource to use inside the 'with' block
    def __enter__(self):
        print(f"[DB] Connecting to {self.db_name}...")
        self.connection = f"conn://{self.db_name}"   # simulate connection
        print(f"[DB] Connection established")
        return self   # 'as db' gets this value

    # Called when 'with' block ends — cleanup goes here
    # exc_type, exc_val, exc_tb are None if no exception occurred
    # Return True to suppress the exception, False/None to let it propagate
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"[DB] Error occurred: {exc_val}. Rolling back...")
        else:
            print(f"[DB] Committing {self.query_count} queries...")
        self.connection = None
        print(f"[DB] Connection to {self.db_name} closed cleanly")
        return False   # don't suppress exceptions — let them propagate

    def execute(self, query: str):
        if not self.connection:
            raise RuntimeError("No active connection")
        self.query_count += 1
        print(f"[DB] Executing: {query}")
        return f"Result of: {query}"


# Clean usage — connection always closes, even if an error occurs
with DatabaseConnection("production_db") as db:
    result = db.execute("SELECT * FROM employees")
    db.execute("UPDATE salaries SET amount = amount * 1.1")
    print(result)

# The connection is guaranteed closed here — no matter what happened inside
print(f"Connection active after 'with': {db.connection}")  # None