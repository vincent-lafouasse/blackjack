all:
	python main.py

beautiful:
	black main.py

edit:
	nvim main.py

predit:
	make beautiful
	make edit

graph:
	pyreverse -o png main.py
