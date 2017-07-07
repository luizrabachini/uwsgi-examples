DJANGO_CMD = python manage.py

NUM_REQUESTS = 100
NUM_CONCURRENT_REQUESTS = 5


clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".cache" -type d | xargs rm -rf


requirements-pip:
	@pip install -r requirements.txt

requirements-apt:
	@sudo apt-get install $(shell cat requirements.apt | tr "\n" " ")


run-server: clean
	$(DJANGO_CMD) runserver localhost:8000

run-uwsgi: clean
	uwsgi --ini server/uwsgi.ini

run-uwsgi-cheaper: clean
	uwsgi --ini server/uwsgi-cheaper.ini

run-test:
	ab -n $(NUM_REQUESTS) -c $(NUM_CONCURRENT_REQUESTS) http://localhost:8000/test/
