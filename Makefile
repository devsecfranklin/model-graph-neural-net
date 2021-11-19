build: 
	docker build -t frank378:model-html \
		--build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') . | tee .buildlog

python: ## generate the python venv
	python3 -m venv _build
	. _build/bin/activate
	python3 -m pip install -rrequirements.txt
	python3 -m pip install -rrequirements-ntwk-model.txt
