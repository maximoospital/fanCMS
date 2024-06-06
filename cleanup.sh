echo 'Limpiando docker de servicms'
echo 'Removiendo contenedores'
docker rm fanCMS-nginx1-1
docker rm fanCMS-api-1
docker rm fanCMS-cms-1
docker rm fanCMS-db-1
echo 'Removiendo imagenes'
docker rmi fanCMS-cms:latest
docker rmi fanCMS-api:latest