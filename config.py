import os

POOL_MINCONN = 3
POOL_MAXCONN = 10

PG_DSN = os.environ.get(
    "PG_DSN",
    "postgresql://agnieszka:aga1984@127.0.0.1/phone_numbers"
)
