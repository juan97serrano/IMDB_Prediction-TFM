eliminar todos los contenedores: docker system prune

eliminar una imagen: docker rmi id_imagen

docker build -t flask-tutorial:latest .

docker container logs CONTAINER_ID

docker run -d -p 5000:5000 flask-tutorial

http://localhost:5000