init:
	pip install -r requirements.txt

test:
	python3 -m unittest tests.unitTests1
	python3 -m unittest tests.unitTests2
