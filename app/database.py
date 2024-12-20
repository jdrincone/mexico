from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///gtfs_mexico.db"
engine = create_engine(DATABASE_URL)
