clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name __pycache__ -exec rm -rf {} +
	find . -name '*.orig' -exec rm -f {} +
	find . -name '*.rej' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '*.bak' -exec rm -f {} +
	find . -name '*.swp' -exec rm -f {} +
	find . -name '*.swo' -exec rm -f {} +
	find . -name '.DS_Store' -exec rm -f {} +
	rm -rf _build/*
	rm -rf docs/*

autobuild: clean
	python3 -m sphinx_autobuild . docs
