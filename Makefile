help:
	@echo "dev  		install development packages"
	@echo "setup 		install compress_fields"
	@echo "test 		run default test suit"


dev:
	pip install -r requirements.txt


setup:
	python setup.py install


test:
	python setup.py test

