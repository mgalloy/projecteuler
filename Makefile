ALL_PROBLEMS=1 2 3
PROBLEM=3

.PHONY: all problem clean

all:
	@for p in $(ALL_PROBLEMS) ; do \
	  echo "Solution to problem $$p..." ; \
	  python solutions/euler_$$p.py ; \
	  echo "" ; \
	done

problem:
	@echo "Solution to problem $(PROBLEM)..."
	@python solutions/euler_$(PROBLEM).py

