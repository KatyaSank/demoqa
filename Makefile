test:
	pytest -n 3 --reruns 2 --count=1
	pytest --alluredir=my_allure_results
	allure serve .\my_allure_results\
#	pytest tests\test_accordian.py --alluredir=my_allure_results
