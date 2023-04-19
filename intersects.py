import psycopg2

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

# Execute the query to find intersecting polygons
with conn.cursor() as cur:
    cur.execute("""
        SELECT t1.id AS id1, t2.id AS id2
        FROM geography_table t1, geography_table t2
        WHERE t1.id <> t2.id AND ST_Intersects(t1.geom, t2.geom);
    """)
    geog_result = cur.fetchall()

# Execute the query to find intersecting polygons in geometry table
with conn.cursor() as cur:
    cur.execute("""
        SELECT t1.id AS id1, t2.id AS id2
        FROM geometry_table t1, geometry_table t2
        WHERE t1.id <> t2.id AND ST_Intersects(t1.geom, t2.geom);
    """)
    geom_result = cur.fetchall()
# Print the result
print("GEOGRAPHY intersection: ", any(geog_result))
print("GEOMETRY intersection: ",  any(geom_result))

# Close the connection
conn.close()
