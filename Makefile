ALL_PROBLEMS=1 2 3 4 5 6 7 8 9 10 11 13 14 15 16 17 20 22 40 42 48
PROBLEM=22
FILENAME=solutions/euler_$(PROBLEM).py

.PHONY: all new problem test clean help

all:
	@for p in $(ALL_PROBLEMS) ; do \
	  echo "Solution to problem $$p..." ; \
	  python solutions/euler_$$p.py ; \
	  echo "" ; \
	done

problem:
	@echo "Solution to problem $(PROBLEM)..."
	@python $(FILENAME)

new:
	@if [ -f solutions/euler_$(PROBLEM).py ]; then \
	  echo "Problem already exists!" ; \
	else \
	  echo "Creating problem $(PROBLEM)..." ; \
	  touch $(FILENAME) ; \
	  chmod +x $(FILENAME) ; \
	fi

test:
	@PYTHONPATH=solutions python -m unittest discover -s tests -p '*_tests.py'

clean:

help:
	@echo "Use 'make <target>' where target is one of:"
	@echo "  all               to run all the problems"
	@echo "  problem           to run the current problem specified by PROBLEM"
	@echo "  new               to create a new problem specified by PROBLEM"
	@echo "  test              to execute the unit tests"
	@echo "  clean             to clean up output"