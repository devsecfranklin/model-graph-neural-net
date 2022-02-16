ACLOCAL_AMFLAGS = -I m4
#SUBDIRS=cluster
#CCLD = $(CC)
#LINK = $(CCLD) $(AM_CFLAGS) $(CFLAGS) $(AM_LDFLAGS) $(LDFLAGS) -o $@

python: ## build the python env
	$(PYTHON) -m venv _build
	( \
		source _build/bin/activate; \
		pip install --upgrade pip; \
		pip install tox; \
		pip install -r ../cluster/requirements.txt --no-warn-script-location; \
		pip install -r ../tests/requirements-test.txt --no-warn-script-location; \
	)
