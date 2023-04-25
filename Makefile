IMAGE = migrate/migrate:latest
DATABASE_URL = postgres://postgres:mysecretpassword@localhost:5433/geography_db?sslmode=disable
VERSION = 20230425195113

migrate:
	docker run --network host --rm -v $(PWD)/migrations:/migrations $(IMAGE) -path=/migrations/ -database $(DATABASE_URL) $(args)

up:
	docker run --network host --rm -v $(PWD)/migrations:/migrations $(IMAGE) -path=/migrations/ -database $(DATABASE_URL) up 1

down:
	docker run -it --network host --rm -v $(PWD)/migrations:/migrations $(IMAGE) -path=/migrations/ -database $(DATABASE_URL) down 1

version:
	docker run --network host --rm -v $(PWD)/migrations:/migrations $(IMAGE) -path=/migrations/ -database $(DATABASE_URL) force $(VERSION)

create:
	docker run --network host --rm \
		--user=$$(id -u):$$(id -g) \
		-v $(PWD)/migrations:/migrations \
		$(IMAGE) create -ext sql -dir /migrations $(NAME)
