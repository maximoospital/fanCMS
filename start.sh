echo 'Iniciando FanCMS'
echo 'First, cleanup:'
echo 'Cleaning all previous docker instances'
echo 'Removing containers'
docker rm fancms-nginx1-1
docker rm fancms-api-1
docker rm fancms-cms-1
docker rm fancms-db-1
echo 'Removing images'
docker rmi fancms-cms:latest
docker rmi fancms-api:latest
echo 'Ready, starting:'
docker compose up
