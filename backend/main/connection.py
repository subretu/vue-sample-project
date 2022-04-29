import psycopg2


# DB接続用関数
def get_connection():
    """
    user = os.getenv("POSTGRES_USER", None)
    pwd = os.getenv("POSTGRES_PASS", None)
    server = os.getenv("POSTGRES_HOST", None)
    port = os.getenv("POSTGRES_HOST", None)
    db = os.getenv("POSTGRES_PORT", None)
    """
    user = "postgres"
    pwd = "postgres"
    server = "127.0.0.1"
    port = "5432"
    db = "postgres"

    con = psycopg2.connect(
        "host="
        + server
        + " port="
        + port
        + " dbname="
        + db
        + " user="
        + user
        + " password="
        + pwd
    )

    return con
