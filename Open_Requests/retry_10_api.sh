source activate
pytest -v -s --alluredir=/home/work/liumiao/tmp/retry_10_api/allure_report --clean-alluredir /home/work/liumiao/tmp/retry_10_api/TYC-requests/testcase/test_online_api.py
allure generate /home/work/liumiao/tmp/retry_10_api/allure_report -o /home/work/liumiao/tmp/retry_10_api/html_report -c
