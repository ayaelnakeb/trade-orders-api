from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# For SQLite in a local file:
SQLALCHEMY_DATABASE_URL = "sqlite:///./orders.db"

# Uncomment and adjust for PostgreSQL:
# POSTGRES_USER = "postgres"
# POSTGRES_PASSWORD = "password"
# POSTGRES_DB = "ordersdb"
# POSTGRES_HOST = "db"  # if using docker-compose, otherwise "localhost"
# POSTGRES_PORT = "5432"
# SQLALCHEMY_DATABASE_URL = (
#     f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
#     f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
# )

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
