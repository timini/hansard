all: iepy api

stop: docker-stop-api docker-stop-iepy

# api ------------------

docker-build-api:
	docker-compose -f docker-compose-api.yml build

docker-up-api: docker-rm-api docker-build-api
	docker-compose -f docker-compose-api.yml up -d

docker-stop-api:
	docker-compose -f docker-compose-api.yml stop

docker-rm-api: docker-stop-api
	docker-compose -f docker-compose-api.yml rm -f

wait-for-postgres: docker-up-api
	docker exec hansard_db_1 bash -c "while ! pg_isready; do echo \"$(date) - waiting for database to start\"; sleep 3; done"

migrate-api: docker-up-api wait-for-postgres
	docker exec hansard_api_1 python api/manage.py migrate

createsuperuser-api: migrate-api
	docker exec hansard_api_1 bash -c "echo \"from users.models import User; User.objects.create_superuser('admin', 'tim@rewire.it', 'sn0wb1rd')\" | python api/manage.py shell"

init-data: migrate-api
	docker exec -ti hansard_api_1 python api/manage.py init_data

test-api: migrate-api
	docker exec -ti hansard_api_1 bash -c "cd api && python manage.py test"

api: createsuperuser-api
	echo "api running on localhost:8000"

#--------------------

docker-build-iepy:
	docker-compose -f docker-compose-iepy.yml build

docker-up-iepy: docker-stop-iepy docker-build-iepy
	docker-compose -f docker-compose-iepy.yml up -d

docker-stop-iepy:
	docker-compose -f docker-compose-iepy.yml stop

docker-rm-iepy: docker-stop-iepy
	docker-compose -f docker-compose-iepy.yml rm -f

migrate-iepy: docker-up-iepy
	docker exec hansard_iepy_1 python /hansard/bin/manage.py migrate

createsuperuser-iepy: migrate-iepy
	docker exec hansard_iepy_1 bash -c "echo \"from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'tim@rewire.it', 'sn0wb1rd')\" | python /hansard/bin/manage.py shell"

iepy: createsuperuser-iepy
	echo "iepy running on localhost:8001"
