CLOCAL_AMFLAGS = -I config/m4 -I aclocal
ACLOCAL_AMFLAGS = -I config/m4 -I aclocal

all:
	pypi python

pypi: 
	( \
		$(PYTHON) -m pip download -d /mnt/clusterfs/pypi tox; \
		$(PYTHON) -m pip download -d /mnt/clusterfs/pypi --no-deps --platform linux_armv7l -r ../gnn/collection/requirements.txt; \
		$(PYTHON) -m pip download -d /mnt/clusterfs/pypi --no-deps --platform linux_armv7l -r ../gnn/training/requirements.txt; \
		$(PYTHON) -m pip download -d /mnt/clusterfs/pypi --no-deps --platform linux_armv7l -r ../tests/requirements.txt; \
	)

python: 
	@$(PY39) -m venv _build
	( \
		source _build/bin/activate; \
		$(PYTHON) -m pip install --upgrade pip; \
		$(PYTHON) -m pip install --no-index --find-links=/mnt/clusterfs/pypi tox; \
		$(PYTHON) -m pip install --no-index --find-links=/mnt/clusterfs/pypi -r../gnn/collection/requirements.txt --no-warn-script-location; \
		$(PYTHON) -m pip install --no-index --find-links=/mnt/clusterfs/pypi -r ../gnn/training/requirements.txt; \
		$(PYTHON) -m pip install --no-index --find-links=/mnt/clusterfs/pypi -r ../tests/requirements.txt --no-warn-script-location; \
	)

