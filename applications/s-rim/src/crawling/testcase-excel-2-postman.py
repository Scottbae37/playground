from openpyxl import load_workbook
import json
import sys
from datetime import datetime


def main(excel_file: str) -> None:
    wb = load_workbook(excel_file)
    acc_dev_list = extract_acc_dev_info(wb)
    diag_list = extract_diag(wb)
    wb.close()

    postman_json = json.loads(
        '{ "info": { "_postman_id": "9e61393a-2e96-4548-ad39-9f9d3ea14239", "name": "pccs-testcase-server-generated", "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json" }, "item": [ { "name": "helth-check", "request": { "method": "GET", "header": [], "body": { "mode": "raw", "raw": "" }, "url": { "raw": "http://10.223.96.146:8787/", "protocol": "http", "host": [ "10", "223", "96", "146" ], "port": "8787", "path": [ "" ] } }, "response": [] }, { "name": "reset", "request": { "method": "POST", "header": [], "body": { "mode": "raw", "raw": "" }, "url": { "raw": "http://10.223.96.146:8787/reset", "protocol": "http", "host": [ "10", "223", "96", "146" ], "port": "8787", "path": [ "reset" ] } }, "response": [] } ] }')
    items: list = postman_json['item']

    for acc, mbr, dev_name, thinq, dev_id in acc_dev_list:
        for dev_name2, dev_type, diag_name in diag_list:
            if dev_name.strip() != dev_name2.strip():
                continue

            # Name
            new_item = gen_new_item_template()
            account = acc[:acc.index('@')]
            dev_id_short: str = dev_id[-1:-3:-1]
            new_item['name'] = f'계정{account}-{dev_name}-기기{dev_id_short[-1::-1]}-{diag_name}'

            # JSON body
            raw = build_raw(dev_id, diag_name, mbr, thinq)
            new_item['request']['body']['raw'] = json.dumps(raw, indent=4)

            items.append(new_item)
    to_file(postman_json)


def to_file(postman_json):
    postfix = datetime.today().strftime('%m-%d_%H:%M')
    fp = open(f"pccs-testcase-{postfix}.json", 'w')
    fp.write(json.dumps(postman_json, indent=4))
    fp.close()


def build_raw(dev_id, diag_name, mbr, thinq):
    raw = {
        'mbrNo': mbr,
        'deviceId': dev_id,
        'diagnosisType': diag_name,
        'eventTime': '12:00',
        'serverName': thinq
    }
    return raw


def gen_new_item_template():
    return {'name': 'reset', 'request': {'method': 'POST', 'header': [{
        "key": "Content-Type",
        "name": "Content-Type",
        "value": "application/json",
        "type": "text"
    }], 'body': {'mode': 'raw', 'raw': '',
                 'options': {'raw': {
                     'language': 'json'}}},
                                         'url': {'raw': 'http://10.223.96.146:8787/testcase',
                                                 'protocol': 'http',
                                                 'host': ['10', '223', '96', '146'], 'port': '8787',
                                                 'path': ['testcase']}}, 'response': []}


def extract_diag(wb):
    ws2 = wb['진단정보']
    diag_list: list = []
    for dev_name, dev_type, diag_name in ws2['A2':'C50']:
        if dev_name.value == None:
            continue
        diag_list.append((dev_name.value, dev_type.value, diag_name.value))
    return diag_list


def extract_acc_dev_info(wb):
    ws1 = wb['계정기기매핑정보']
    l: list = []
    for acc_name, mbr_no, dev_type, thinq_ver, dev_id in ws1['A2':'E50']:
        if dev_id.value == None:
            continue
        l.append((acc_name.value, mbr_no.value, dev_type.value, thinq_ver.value, dev_id.value))
    return l


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Put excel file name: ex) python testcase-excel-2-postman.py ./pccs-testcase-mapping.xlsx')
        print(sys.argv)
        exit(-1)
    main(sys.argv[1])
