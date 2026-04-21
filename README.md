a Whatsapp server for nokia or other old devices that can't run whatsapp

docker build --no-cache -t nokia-wa .
docker run -it -p 3000:3000 nokia-wa