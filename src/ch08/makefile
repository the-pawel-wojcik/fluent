mypy = ~/.local/share/nvim/mason/bin/mypy
file = messages.py
.PHONY: basic
basic:
	$(mypy) $(file)

dud:
	$(mypy) --disallow-untyped-defs $(file)

did:
	$(mypy) --disallow-incomplete-defs $(file)

test:
	$(mypy) ./test_top.py
