PROBLEM=2

.PHONY: all clean

all: euler_$(PROBLEM)

euler_$(PROBLEM):
	@echo "Solution to problem $(PROBLEM)..."
	@python solutions/euler_$(PROBLEM).py

