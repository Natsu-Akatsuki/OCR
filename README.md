# 广工出入库单OCR

提供将发票自动填写到出入库单的功能；本服务的OCR采用百度云API，还有一堆BUG待解决（会有错别字，会识别漏，需要后期人工校对）

## 支持的发票类型

- 支持：通用电子发票和增值税电子普通发票

<img src="https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/image-20211129171447803.png" alt="image-20211129171447803" style="zoom: 50%;" />

<img src="https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/image-20211129171534021.png" alt="image-20211129171534021" style="zoom:50%;" />

- 不支持：通用机打发票（电子）

<img src="https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/image-20211129171253041.png" alt="image-20211129171253041" style="zoom:50%;" />

## 依赖

- python-docx
- requests

- pyqt

## 使用步骤

### 获取AK和SK，设置Token

打开`update_token.py`，根据[ref](https://console.bce.baidu.com/ai/?fromai=1#/ai/ocr/app/list)，设置相应的AK和SK（如图所示）

![image-20211129104642273](https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/image-20211129104642273.png)

---

填写完后，执行`python update_token.py`在脚本所在目录生成token文件

```bash
$ python update_token.py
```

**NOTE**

需要提前注册[OCR服务](https://console.bce.baidu.com/ai/#/ai/ocr/overview/index)（百度云的该服务为免费服务，只不过有次数限制）

![image-20211129104437025](https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/image-20211129104437025.png)

---

### 执行脚本

导出的出入库单在output目录下，生成时界面或会冻结

```bash
$ python main_gui.py
```

![img](https://natsu-akatsuki.oss-cn-guangzhou.aliyuncs.com/img/使用方法.gif)