CLOCAL_AMFLAGS = -I config/m4 -I aclocal
ACLOCAL_AMFLAGS = -I config/m4 -I aclocal

.PHONY: cluster docs paper presentation tests

clean:
	rm -rf _build *.egg-info
	@find . -name '*.pyc' | xargs rm -rf
	@find . -name '__pycache__' | xargs rm -rf
	@for trash in *.aux *.bbl *.blg *.lof *.log *.lot *.out *.pdf *.synctex.gz *.toc ; do \
		if [ -f "$$trash" ]; then \
			rm -rf $$trash ; \
		fi ; \
	done

cluster-collect: ## Build collection container for local cluster
	docker buildx use franklin
	docker build -t franklin:gnn-collection \
		--build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') gnn/collection | tee .buildlog

cluster-train: ## Build training container for local cluster
	docker buildx use franklin
	docker build --platform linux/arm/v7 -t franklin:gnn-training \
		--build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') gnn/training | tee .buildlog

python:
	@$(PY39) -m venv _build
	( \
		source _build/bin/activate; \
		_build/bin/python -m pip install --no-index --trusted-host storage1.lab.bitsmasher.net --find-links=http://storage1.lab.bitsmasher.net/pypi tox; \
		_build/bin/python -m pip install --trusted-host storage1.lab.bitsmasher.net --find-links=http://storage1.lab.bitsmasher.net/pypi --upgrade pip; \
		_build/bin/python -m pip install --trusted-host storage1.lab.bitsmasher.net --find-links=http://storage1.lab.bitsmasher.net/pypi -r gnn/collection/requirements.txt; \
		_build/bin/python -m pip install --trusted-host storage1.lab.bitsmasher.net --find-links=http://storage1.lab.bitsmasher.net/pypi -r gnn/training/requirements.txt; \
	)

