#!/bin/bash

/home/work/chenzhang/software/miniconda3/envs/py39/bin/pytest -v -s --alluredir=./allure_report_raw --clean-alluredir ./testcase/test_online_api.py
allure generate ./allure_report_raw -o ./html_report -c
