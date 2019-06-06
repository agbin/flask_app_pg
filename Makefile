all:

clean:
	find . -type d -name __pycache__ | xargs rm -rfv

run-debug:
	python3 app.py
