##### Common Deploy Script

echo "=================================================="

set -Eeuo pipefail

echo "===== Deploy Start ====="

echo "===== STEP 1 : Permission ====="

sudo chown -R bitnami:bitnami .

echo "===== STEP 2 : Build and start containers ====="

docker compose up -d --build

echo "===== STEP 3 : Apply database migrations ====="

docker compose exec -T web python manage.py migrate --noinput

echo "===== STEP 4 : Collect static files ====="

docker compose exec -T web python manage.py collectstatic --noinput

echo "===== STEP 5 : Reload web service ====="

docker compose exec -T web touch my_django_project/wsgi.py
docker compose restart web

echo "===== STEP 6 : Restart Apache ====="

sudo /opt/bitnami/ctlscript.sh restart apache

##### "===== STEP 7 : Restart Django Container ====="

##### docker compose restart web


echo " Deploy Finished Successfully"
echo "=================================================="
