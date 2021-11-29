"""
# 注意 access token 会过期，一段时间后需要更新，获取方式可参考：https://cloud.baidu.com/doc/OCR/s/1k3h7y3db
"""
from PyQt5.QtCore import QObject
import requests
import base64
import numpy as np
from pathlib import Path
import time


class OCRAPI(QObject):
    """
    调用百度AI的发票OCR检测
    :docs: https://ai.baidu.com/ai-doc/OCR/wkibizyjk
    """

    def __init__(self):

        super().__init__()
        self.file_dict = {'.pdf': 'pdf', '.jpg': 'img', '.png': 'img', '.jpeg': 'img', '.bmp': 'img'}

        self.request_url_list = ["https://aip.baidubce.com/rest/2.0/ocr/v1/invoice",
                                 "https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice"]

    def gui_2_api(self, ocr_file_names, check_type):
        invoice_ids = ""
        invoice_dates = ""
        amount_in_figuers = 0
        obj_infos = []

        for file_name in ocr_file_names:
            # 发票类型(0:机打发票,1:增值税发票)
            result = self.run(file_name, self.file_dict[Path(file_name).suffix], check_type)
            if isinstance(result, str):
                return result
            else:
                invoice_id, invoice_date, amount_in_figuer, obj_info = result
                invoice_ids += invoice_id + '\n'
                invoice_dates += invoice_date + '\n'
                amount_in_figuers += float(amount_in_figuer)
                obj_infos.extend(obj_info)
            # limit is 10 rps
            time.sleep(0.10)

        result_dict = {"invoice_nums": invoice_ids.strip(),
                       "invoice_dates": invoice_dates.strip(),
                       "amount_in_figuers": str(amount_in_figuers),
                       "obj_infos": obj_infos
                       }
        return result_dict

    def run(self, file_name, file_type='img', check_type=0):
        '''
        提取发票信息
        :param file_name:
        :param file_type: 文件类型(pdf,img)
        :param check_type: 发票类型(0:机打发票,1:增值税发票)
        :return:
        '''

        request_url = self.request_url_list[check_type]

        # 二进制方式打开图片文件
        if file_type == "img":
            with open(file_name, 'rb') as f:
                img = base64.b64encode(f.read())
            params = {"image": img}
        else:
            with open(file_name, 'rb') as f:
                pdf_file = base64.b64encode(f.read())
            params = {"pdf_file": pdf_file}

        with open("token") as fp:
            token = fp.readline().strip()

        request_url = request_url + "?access_token=" + token

        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)

        try:
            ocr_result_dict = response.json()["words_result"]
        except KeyError:
            return response.json()['error_msg']

        # 物品名称
        commodity_name = [i['word'] for i in ocr_result_dict["CommodityName"]]
        # 物品件数
        commodity_num = [i['word'] for i in ocr_result_dict["CommodityNum"]]
        # 物品单位
        if len(ocr_result_dict["CommodityUnit"]) == 0:
            commodity_unit = ['']
        else:
            commodity_unit = [i['word'] for i in ocr_result_dict["CommodityUnit"]]
        # 单个物品金额（不含税）
        commodity_amount = [i['word'] for i in ocr_result_dict["CommodityAmount"]]

        # 增值税发票
        if check_type == 1:
            # 单个物品税款
            commodity_tax = []
            for i in ocr_result_dict["CommodityTax"]:
                if i['word'] == "***":
                    i['word'] = 0
                commodity_tax.append(i['word'])
            # 单个物体总价（含税）
            commodity_amount_with_tax = np.asarray(commodity_amount, dtype=np.float32) \
                                        + np.asarray(commodity_tax, dtype=np.float32)
        elif check_type == 0:
            commodity_amount_with_tax = commodity_amount

        # 单个物体单价（含税）
        commodity_price = np.asarray(commodity_amount_with_tax, dtype=np.float32) \
                          / np.asarray(commodity_num, dtype=np.float32)
        commodity_price[np.isinf(commodity_price)] = 0
        commodity_price = list(commodity_price)

        # 发票号
        invoice_num = ocr_result_dict["InvoiceNum"]
        invoice_date = ocr_result_dict["InvoiceDate"]
        amount_in_figuers = ocr_result_dict['AmountInFiguers']

        commodity_num = np.int_(np.asarray(commodity_num, dtype=np.float32)).astype(str).tolist()
        obj_info = list(zip(commodity_name, commodity_unit,
                            commodity_price, commodity_num, list(commodity_amount_with_tax)))

        return invoice_num, invoice_date, amount_in_figuers, obj_info


if __name__ == '__main__':
    ocrapi = OCRAPI()
    # result = ocrapi.run(file_name='print_type.jpg', file_type="img", check_type=0)
    # result = ocrapi.run(file_name='1.jpg', file_type="img", check_type=1)
    # if result is None:
    #     print("there is something wrong in OCR")
