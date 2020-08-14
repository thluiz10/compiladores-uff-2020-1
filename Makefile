test:
	@which python
	@python -c "import tatsu"
	@python -c "import llvmlite"
	@file ./
