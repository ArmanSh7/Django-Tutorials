build:
	docker build --force-rm $(options) -t django-webite:latest .

build-prod:
	$(MAKE) build options="--target production"

# it removes the previous containers
compose-start:
	docker-compose up --remove-orphans $(options)

compose-stop:
	docker-compose down --remove-orphans $(options)

compose-manage-py:
	docker-compose run --rm $(options) website python manage.py $(cmd)