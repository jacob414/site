# Set the shell to use
SHELL := /bin/bash

# Set the name of the script to run
SCRIPT := exp-simp.el

# Find all org files in the current directory
ORG_FILES := $(wildcard *.org)

# Define a phony target to always run the script
.PHONY: all
all: $(ORG_FILES)
	emacs -Q --batch --load $(SCRIPT)

# Define a clean target to remove generated HTML files
.PHONY: clean
clean:
	rm -f *.html
