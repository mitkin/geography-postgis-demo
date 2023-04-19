Go ahead and run:
```
docker compose up
pip install -r requirements.txt
psql -U postgres -h localhost -p 5433 -d geography_db -f tables.sql
python insert.py
python intersects.py
```

The output should be like this:
```
GEOGRAPHY intersection:  True
GEOMETRY intersection:  False

```
