docker build . -t app
docker run --name app -d -p 8000:5000 --rm app:latest
 
