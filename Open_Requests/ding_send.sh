source activate
failed=$(grep launch_status_failed /home/work/.jenkins/workspace/API自动化测试/html_report/export/prometheusData.txt | awk '{print$2}')
broken=$(grep launch_status_broken /home/work/.jenkins/workspace/API自动化测试/html_report/export/prometheusData.txt | awk '{print$2}')
if [[ $failed -eq 0 && $broken -eq 0 ]]; then
  echo 'success'
  python3 /home/work/liumiao/tmp/tyc-requests/tmp/ok_send.py
else
  python3 /home/work/liumiao/tmp/tyc-requests/tmp/dingding_jenkins.py
  python3 /home/work/liumiao/tmp/tyc-requests/tmp/feishu_send.py
  set -e
  exit 1
fi
