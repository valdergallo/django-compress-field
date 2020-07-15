help:
	@echo "dev  		install development packages"
	@echo "setup 		install compress_fields"
	@echo "test 		run default test suit"
	@echo "upload 		upload packages to PyPi"


dev:
	pip install -r requirements.txt

upload: export DJANGO_SETTINGS_MODULE=django_test_settings
upload:
	python setup.py build bdist_wheel
	python setup.py build sdist
	pip install twine
	twine upload dist/*

setup:
	python setup.py install


test:
	python setup.py test
