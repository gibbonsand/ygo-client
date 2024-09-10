import pandas as pd

import constants as c

ENGIGNE = pd.io.sql.create_engine('sqlite:///{}'.format(c.DB_NAME))

def create_db(df) -> None:
    # Write DataFrame to SQLite database
    df.to_sql("cards", ENGIGNE, if_exists='replace', index=False)


def query_db(query: str = None):
    # Example query: Get the total count of each card type
    if not query:
        query = """
            SELECT Name, Amount
            FROM cards
            LIMIT 10
        """
    result = pd.read_sql_query(query, ENGIGNE)
    print(result)