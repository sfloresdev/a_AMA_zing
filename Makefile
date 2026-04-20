
PYTHON = python3
MAIN = a_maze_ing.py
CONFIG = config.txt

# FLAKE = python3 -m flake8
# MYPY  = python3 -m mypy .


install:
	$(PYTHON) -m pip install -r requirements.txt

run:
	-$(PYTHON) $(MAIN) $(CONFIG)

debug:
	$(PYTHON) -m pdb $(MAIN) $(CONFIG)

clean:
	rm -rf __pycache__ .mypy_cache
	find . -type -d -name "__pycache__" -exec rm -rf {} +

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs


.PHONY: install run debug clean lint