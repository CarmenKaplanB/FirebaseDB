# FirebaseDB

docker build -t app:v1 .
docker images
docker run -it -p 8080:8080 -v /workspace/FirebaseDB/prueba:/prueba --name python -h ubuntu app:v1