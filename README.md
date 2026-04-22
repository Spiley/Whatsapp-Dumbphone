a Whatsapp server for nokia or other old devices that can't run whatsapp

docker build --no-cache -t nokia-wa .
docker run -d --env-file .env -p 3000:3000 nokia-wa
docker logs -f CONTAINER_ID

IMPORTANT: after whatsapp gateway ready, wait for a minute

to start: python run.py