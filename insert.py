import psycopg2
from psycopg2.extras import RealDictCursor
from shapely.geometry import Polygon
import geopandas as gpd

import geopandas as gpd
from sqlalchemy import create_engine
# Define the connection parameters
params = {
    "host": "localhost",
    "database": "geography_db",
    "user": "postgres",
    "password": "mysecretpassword",
    "port": 5433,
}
# Connect to the database
conn = psycopg2.connect(**params)

polygons = gpd.read_file('polygon.geojson')
connection_string = "postgresql://postgres:mysecretpassword@localhost:5433/geography_db"
engine = create_engine(connection_string)

# Insert each polygon into the database using SQLAlchemy
for i, polygon in polygons.iterrows():
    id = polygon["id"]
    geometry = polygon["geometry"]
    geometry = geometry.wkt  # Convert the geometry to WKT format
    print(id, geometry)
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        # cursor.execute("INSERT INTO geography_table (id, geom) VALUES (%s, ST_GeographyFromText(%s))", (id, geometry))
        cursor.execute("INSERT INTO geometry_table (id, geom) VALUES (%s, ST_GeometryFromText(%s, 4326))", (id, geometry))
        conn.commit()

