ALL_PROBLEMS=1 2 3 4 5 6 7
PROBLEM=7
FILENAME=solutions/euler_$(PROBLEM).py

.PHONY: all new problem clean

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