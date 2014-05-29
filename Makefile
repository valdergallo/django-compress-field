help:
	@echo "dev  		install development packages"
	@echo "setup 		install compress_fields"
	@echo "test 		run default test suit"
	@echo "test-cov  	run default test suit with coverage"
	@echo "test-pep  	run default test suit with pep8"


dev:
	pip install -r requirements.txt


setup:
	python setup.py install


test:
	py.test compress_fields


test-cov:
	py.test compress_fields --cov compress_fields --cov-report html


test-pep:
	py.test compress_fields --pep8
