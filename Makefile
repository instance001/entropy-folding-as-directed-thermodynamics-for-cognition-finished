## License: AGPLv3 (see LICENSE)
PY=python
VENV=.venv

.PHONY: install test pdf

install:
	$(PY) -m venv $(VENV)
	$(VENV)/Scripts/activate && pip install -U pip -r requirements.txt

test:
	$(VENV)/Scripts/activate && pytest

pdf:
	@echo "Requires pandoc + LaTeX toolchain installed locally."
	@if command -v pandoc > /dev/null; then \
		pandoc paper.md -o paper.pdf; \
	else \
		echo "pandoc not found; install pandoc to build PDF."; \
	fi
