.PHONY: collect build all
collect:
	python3 scripts/collect.py
build:
	python3 scripts/build.py
all: collect build
