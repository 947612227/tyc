source activate
pytest -v -s --alluredir=/home/work/.jenkins/workspace/API自动化测试/allure_report --clean-alluredir testcase/test_online_api.py
allure generate /home/work/.jenkins/workspace/API自动化测试/allure_report/ -o /home/work/.jenkins/workspace/API自动化测试/html_report -c
