DROP TABLE IF EXISTS geography_table;
DROP TABLE IF EXISTS geometry_table;
CREATE TABLE geography_table (
            id SERIAL PRIMARY KEY,
            geom GEOGRAPHY(MULTIPOLYGON, 4326)
          );
CREATE TABLE geometry_table (
            id SERIAL PRIMARY KEY,
            geom GEOMETRY(MULTIPOLYGON, 4326)
          );

