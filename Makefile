WORKDIR = .
MANAGE = python $(WORKDIR)/manage.py

style:
	black -S -l 79 $(WORKDIR)
	isort $(WORKDIR)
	flake8 $(WORKDIR)
	$(MANAGE) test

migrate:
	$(MANAGE) makemigrations
	$(MANAGE) migrate

superuser:
	$(MANAGE) createsuperuser

run:
	$(MANAGE) runserver

shell:
	$(MANAGE) shell