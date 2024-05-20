runserver:
	docker compose up -d --build

init_db:
	docker compose exec app poetry run alembic upgrade head

seed_db:
	docker compose cp example_data.sql db:/tmp/dump.sql
	docker compose exec -i db psql -U postgres -d postgres -f /tmp/dump.sql

dump_bd:
	docker compose exec -it db pg_dump -U postgres postgres -a -T alembic_version > example_data.sql

down:
	docker compose down

clean:
	docker-compose down -v --rmi all
