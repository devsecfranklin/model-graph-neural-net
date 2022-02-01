.PHONY: docs src tests

PY39 := $(shell command -v /mnt/clusterfs/usr/bin/python3 2> /dev/null)
ifndef PY39
    PY39 := $(shell command -v python 2> /dev/null)
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
	@$(PY39) -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

build: ## build a container
	$(MAKE) print-status MSG="Building container"
	docker build -t frank378:model-graph-neural-net \
		--build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') . | tee .buildlog

clean: ## clean up all the things
	@$(MAKE) print-status MSG="Clean up stale build artifacts"
	@for trash in _build .coverage *.egg-info .pytest_cache htmlcov .tox; do \
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
	@$(PY39) -m venv _build 
	. _build/bin/activate
	@$(PY39) -m pip install --upgrade pip
	@$(PY39) -m pip install tox
	@$(PY39) -m pip install -r src/requirements.txt --no-warn-script-location
	@$(PY39) -m pip install -r tests/requirements-test.txt --no-warn-script-location
