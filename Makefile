# инструкция по работе с файлом "Makefile" – https://bytes.usc.edu/cs104/wiki/makefile/

# обновление сборки Docker-контейнера
build:
	docker compose build

# запуск автоматических тестов
test:
	docker compose run app pytest src/tests/conftest.py


