##### Common Deploy Script
##### Usage:
#####   ./scripts/deploy.sh
###############################################################################

set -Eeuo pipefail

echo "=================================================="
echo " Deploy Start"
echo " Host : $(hostname)"
echo " Date : $(date '+%Y-%m-%d %H:%M:%S')"
echo "=================================================="

##### STEP1

echo
echo "===== STEP 1 : Permission ====="

sudo chown -R bitnami:bitnami .

##### STEP2

echo
echo "===== STEP 2 : Docker Compose Up ====="

docker compose up -d

echo
echo "Containers"

docker compose ps

##### STEP3

echo
echo "===== STEP 3 : Install Python Packages ====="

docker compose exec -T web pip install -r requirements.txt

##### STEP4

echo
echo "===== STEP 4 : Database Migration ====="

docker compose exec -T web python manage.py migrate --noinput

##### STEP5

echo
echo "===== STEP 5 : Collect Static ====="

docker compose exec -T web python manage.py collectstatic --noinput

##### STEP6

echo
echo "===== STEP 6 : Touch WSGI ====="

docker compose exec -T web touch my_django_project/wsgi.py

##### STEP7

echo
echo "===== STEP 7 : Restart Django Container ====="

docker compose restart web

##### STEP8

echo
echo "===== STEP 8 : Restart Apache ====="

sudo /opt/bitnami/ctlscript.sh restart apache

##### STEP9

echo
echo "===== STEP 9 : Status ====="

docker compose ps

echo
echo "Docker Containers"

docker ps

##### END

echo
echo "=================================================="
echo " Deploy Finished Successfully"
echo "=================================================="
