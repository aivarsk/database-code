up:
	docker-compose up

pgtail:
	MSYS_NO_PATHCONV=1 docker exec -it database-code_postgres_1 tail -n 0 -f /tmp/postgresql.log

pgshell:
	docker exec -it database-code_postgres_1 bash -c 'PGPASSWORD=postgres psql -U postgres -h localhost -d postgres'	
