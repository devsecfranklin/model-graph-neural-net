.PHONY: cluster docs tests

PYTHON := $(shell command -v python3 2> /dev/null)
ifndef PYTHON
    PYTHON := $(shell command -v python 2> /dev/null)
endif

SHELL:=/bin/bash

# Used for colorizing output of echo messages
BLUE := "\\033[1\;36m"
LBLUE := "\\033[1\;34m"
LRED := "\\033[1\;31m"
YELLOW := "\\033[1\;33m"
NC := "\\033[0m" # No color/default

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
  match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
  if match:
    target, help = match.groups()
    print("%-20s %s" % (target, help))
endef

export PRINT_HELP_PYSCRIPT

help: 
	@$(PYTHON) -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

build: ## build a container
	@$(MAKE) print-status MSG="Building container"
	docker build -t devsecfranklin:model-graph-neural-net \
		--build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') . | tee .buildlog

cluster: ## Set up build env for internal/private k3s cluster
	@$(MAKE) print-status MSG="Configure cluster dev env"
	@libtoolize
	@aclocal
	@autoreconf -i
	@automake -a -c
	@$(MAKE) print-status MSG="Running your configure script"
	./configure
	@$(MAKE) print-status MSG="(⊃｡•́‿•̀｡)⊃━⭑･ﾟﾟ･*:༅｡.｡༅:*ﾟ:*:✼✿ Good things are happening! ☽༓･*˚⁺‧͙"
	./config.status
	cd cluster && make pypi && make python
	@$(MAKE) print-status MSG="Python virtual dev env is ready."	

cluster-collect: ## Build collection container for local cluster
	@$(MAKE) print-status MSG="Building collection container"
	docker buildx use franklin
	#docker buildx build --platform linux/arm/v7 -t franklin/gnn-collection:latest cluster/
	docker build -t franklin:gnn-collection \
		--build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') gnn/collection | tee .buildlog

cluster-train: ## Build training container for local cluster
	@$(MAKE) print-status MSG="Building training container"	
	docker buildx use franklin
	#docker buildx build --platform linux/arm/v7 -t franklin/gnn-training:latest cluster/
	docker build --platform linux/arm/v7 -t franklin:gnn-training \
		--build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') gnn/training | tee .buildlog

clean: ## clean up all the things
	@$(MAKE) print-status MSG="Clean up stale build artifacts"
	@for trash in aclocal.m4 _build .coverage *.egg-info .pytest_cache htmlcov .tox cluster/Makefile.in cluster/compile cluster/config.guess cluster/missing cluster/install-sh cluster/config.sub cluster/_build; do \
			if [ -f $$trash ] || [ -d $$trash ]; then \
					rm -rf $$trash ; \
			fi ; \
	done
	@find . -name '*.pyc' | xargs rm -rf
	@find . -name '__pycache__' | xargs rm -rf
	@if [ ! -d "/nix" ]; then nix-collect-garbage -d; fi
	@docker system prune -f

docker: ## do the docker stuff
	$(MAKE) print-status MSG="Building with docker-compose"
	@if [ -f /.dockerenv ]; then echo "Don't run make docker inside docker container" && exit 1; fi;
	@$(MAKE) print-status MSG="Generating dot from TF, hold tight..."
	@docker-compose build --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') model-gcn
	@docker-compose run model-gcn

print-error:
	@:$(call check_defined, MSG, Message to print)
	@echo -e "$(LRED)$(MSG)$(NC)"

print-status:
	@:$(call check_defined, MSG, Message to print)
	@echo -e "$(BLUE)$(MSG)$(NC)"

python: ## build the python env
	$(MAKE) print-status MSG="Building Python virtual environment, hold tight."
	@$(PYTHON) -m venv _build
	( \
		source _build/bin/activate; \
		$(PYTHON) -m pip install --upgrade pip; \
		$(PYTHON) -m pip install tox; \
		$(PYTHON) -m pip install --no-index --find-links=/mnt/clusterfs/pypi tox; \
		$(PYTHON) -m pip install --no-index --find-links=/mnt/clusterfs/pypi -r gnn/collection/requirements.txt --no-warn-script-location; \
		$(PYTHON) -m pip install --no-index --find-links=/mnt/clusterfs/pypi -r gnn/training/requirements.txt; \
		$(PYTHON) -m pip install --no-index --find-links=/mnt/clusterfs/pypi -r tests/requirements.txt --no-warn-script-location; \
	)
	$(MAKE) print-status MSG="Walk like an egg."
	@$(PYTHON) -m pip install -e .
