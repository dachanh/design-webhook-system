FORMAT = black app/.

install:
	pip install -r requirements.txt

format:
	$(FORMAT)