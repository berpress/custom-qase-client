lint:
	@pre-commit run --all-files

test:
	@pytest tests/api -q

test_ui:
	@pytest tests/ui -q
