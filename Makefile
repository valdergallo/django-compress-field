help:
	@echo "dev  		install development packages"
	@echo "setup 		install compress_fields"
	@echo "test 		run default test suit"
	@echo "upload 		upload packages to PyPi"


dev:
	pip install -r requirements.txt

upload:
	python setup.py build bdist_wheel --universal upload
	python setup.py build sdist --universal upload

setup:
	python setup.py install


test:
	python setup.py test
