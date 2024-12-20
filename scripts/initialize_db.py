import pandas as pd
import logging
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import (Base, Stop, Agency, Calendar,
                    CalendarDate, FeedInfo,
                    Routes, Shape, Trip, StopTime)

BASE_DIR = os.path.abspath("../")
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'gtfs_mexico.db')}"
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)


def load_data(file_path, table_class, engine):
    """
    Carga datos desde un archivo CSV en
     la tabla de la base de datos correspondiente.
    """
    # Leer el archivo .txt como un DataFrame
    df = pd.read_csv(file_path)

    # Cargar los datos en la base de datos
    with engine.connect() as connection:
        df.to_sql(table_class.__tablename__, con=connection, if_exists='append', index=False)
        print(f"Datos cargados en la tabla {table_class.__tablename__} desde {file_path}.")


def main():
    """
    Punto de entrada principal para cargar
    los datos GTFS en la base de datos.
    """
    # Crear las tablas
    Base.metadata.create_all(engine)
    logging.info("Tablas creadas correctamente.")

    # Rutas de los archivos GTFS
    files = {
        "data/agency.txt": Agency,
        "data/calendar.txt": Calendar,
        "data/calendar_dates.txt": CalendarDate,
        "data/feed_info.txt": FeedInfo,
        "data/shapes.txt": Shape,
        "data/stop_times.txt": StopTime,
        "data/routes.txt": Routes,
        "data/stops.txt": Stop,
        "data/trips.txt": Trip,
    }

    for file_path, model in files.items():
        try:
            db_file_path = os.path.join(BASE_DIR, 'gtfs_mexico.db')

            if os.path.exists(db_file_path):
                logging.info("La base de datos ya existe. Omitiendo pasos de inicialización.")
            else:
                load_data(f"{file_path}", model, engine)
        except Exception as e:
            logging.error(f"Error al cargar {file_path}: {e}")


if __name__ == "__main__":
    main()
