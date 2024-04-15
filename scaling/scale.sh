docker compose up --build -d --scale webapp=5
docker compose exec nginx nginx -s reload