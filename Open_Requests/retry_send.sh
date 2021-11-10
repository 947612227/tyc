source activate
failed=$(grep ./html_report/export/prometheusData.txt | awk '{print$2}')
broken=$(grep ./html_report/export/prometheusData.txt | awk '{print$2}')
if [[ $failed -eq 0 && $broken -eq 0 ]]; then
  echo 'success'
  python3 ./retry_ok_send.py
else
  python3 ./retry_feishu_send.py
  set -e
  exit 1
fi
