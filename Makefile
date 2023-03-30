build:
  	docker compose --env-file .env up --build -d --remove-orphans
up:
    docker compose --env-file .env up -d
down:
    docker compose down
show_logs:
    docker compose logs
