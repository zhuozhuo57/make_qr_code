# -*- coding=utf-8 -*-
import configparser
import json
import os
import time
from statistics import mean

file = os.path.dirname(os.path.abspath(__file__))
config = configparser.ConfigParser()
s = config.read(file + r'\config.ini')
filePath = config.get("Local", "logPath")
father_dir = []
child_dir = []
list_fail_image_path = []
succeed_list = []
run_time_list = []
fail_image_path_list = []
table_tr0 = ''
table_tr1 = ""
table_tr2 = ""
numfail = 1
numsucc = 9
class Template_mixin(object):
    """html报告"""
    HTML_TMPL = """
<!DOCTYPE html>
<html lang="en">
<body>
<head>
<meta charset="UTF-8">
<title>算法自动化测试报告</title>
<link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
<h2 style="font-family: Microsoft YaHei">算法自动化测试报告</h2>
<p class='attribute'><strong>测试结果 : </strong> %(value)s</p>
<style type="text/css" media="screen">
body  { font-family: Microsoft YaHei,Tahoma,arial,helvetica,sans-serif;padding: 20px;}
</style>
</head>
<table id='result_table' class="table table-condensed table-bordered table-hover">
    <colgroup>
       <col align='left' />
       <col align='right' />
       <col align='right' />
       <col align='right' />
    </colgroup>
    <tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">
        <th width="50px">序号</th>
        <th width="50px">测试时间</th>
        <th width="50px">提交代码commit_id</th>
        <th width="50px">测试数据集</th>
        <th width="50px">算法版本</th>
        <th width="50px">测试结果</th>
        <th width="50px">解码率</th>
        <th width="50px">正确率</th>
        <th width="50px">平均耗时</th>
        <th width="50px">最大耗时</th>
        <th width="50px">最小耗时</th>
        <th width="50px">扫码失败总数</th>
        <th width="50px">扫码失败文件分布</th>
    </tr>
    %(table_tr2)s
</table>

<details>
<p>%(测试图片集)s详细测试结果</p>
<table id='result_table' class="table table-condensed table-bordered table-hover">
    <tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;word-break: break-all;word-wrap: break-word; ">
        <th width="15px">id</th>
        <th width="50px">图片路径</th>
        <th width="20px">解码是否成功</th>
        <th width="15px">图片处理耗时</th>
        <th width="20px">图片解码类型</th>
        <th width="50px">图片解码内容</th>
        <th width="50px">图片原本标注信息</th>
        <th width="15px">检测坐标</th>
    </tr>
    %(table_tr3)s
</table>
</details>
</body>
</html>"""
    # 总数据
    TABLE_TMPL_TOTAL = """
        <tr class='failClass warning'>
            <td width="50px">%(序号)s</td>
            <td width="50px">%(测试时间)s</td>
            <td width="50px">%(提交代码commit_id)s</td>
            <td width="50px">%(测试数据集)s</td>
            <td width="50px">%(算法版本)s</td>
            <td width="50px">%(测试结果)s</td>
            <td width="50px">%(解码率)s</td>
            <td width="50px">%(正确率)s</td>
            <td width="50px">%(平均耗时)s</td>
            <td width="50px">%(最大耗时)s</td>
            <td width="50px">%(最小耗时)s</td>
            <td width="50px">%(扫码失败总数)s</td>
            <td width="50px">%(扫码失败文件分布)s</td>
        </tr>"""
    # case数据
    TABLE_TMPL_CASE = """
        <tr id='header_row' class="failClass warning" style="font-weight: bold;font-size: 14px;word-break: break-all;word-wrap: break-word; ">
            <td width="15px">%(id)s</td>
            <td width="50px">%(image_path)s</td>
            <td width="15px">%(succeed)s</td>
            <td width="15px">%(run_time)s</td>
            <td width="15px">%(type)s</td>
            <td width="50px" >%(result)s</td>
            <td width="50px" >%(target_result)s</td>
            <td width="50px"">%(rect_points)s</td>
        </tr>"""
html = Template_mixin()
id = 1
# 处理测试日志文件，提取json数据
with open(filePath, 'r', encoding="utf-8") as f:
    readlines = f.read()
    s = json.loads(readlines)
    # 实现数据写入
    print("date_time  is", s["date_time"])
    verison = s["version"]
    print("version is ", s["version"])
    print("dataset_path is", s["dataset_path"])
    for i in range(len(s["decode_results"])):
        print("image_path is", str(s["decode_results"][i]["image_path"]))
        print("image_name is", str(s["decode_results"][i]["image_path"]).split("/")[-1])
        succeed_value=s["decode_results"][i]["succeed"]
        print("succeed is", s["decode_results"][i]["succeed"])
        succeed_list.append(succeed_value)
        runtime=s["decode_results"][i]["run_time"]
        run_time_list.append(runtime)
        print("run_time is", s["decode_results"][i]["run_time"])
        results=s["decode_results"][i]["results"]
        sheetname_type =''
        result=''
        rect_points=''
        #对results 进行处理 results 为空type 返回空
        if(results!=[]):
            j=1
            for j in range(len(s["decode_results"][i]["results"])):
                print("type is", s["decode_results"][i]["results"][j]["type"])
                sheetname_type = s["decode_results"][i]["results"][j]["type"]
                print("sheetname_type   is", sheetname_type)
                print("sheetname_type  type is", type(sheetname_type))
                result = s["decode_results"][i]["results"][j]["result"]
                print("result is", s["decode_results"][i]["results"][j]["result"])
                rect_points = s["decode_results"][i]["results"][j]["rect_points"]
                print("rect_points is", s["decode_results"][i]["results"][j]["rect_points"])

                j+=1
        #如果succeed=false 的情况
        else :
            j=1
            for j in range(len(s["decode_results"][i]["results"])):
                sheetname_type = " "
                result = '[]'
                rect_points = '[]'
                j += 1
        if(succeed_value=='false'):
            # 返回解码失败路径
            fail_image_path = str(s["decode_results"][i]["image_path"])
            list_fail_image_path.append(fail_image_path)
            print("根据succed返回值获取 图片路径", str(s["decode_results"][i]["image_path"]))
            # 解析截取路径名称
            print("根据succed返回值获取 获取父目录",
                  str(s["decode_results"][i]["image_path"]).strip(str(s["dataset_path"])).split("/")[0:2])
            print("根据succed返回值获取 获取父目录",
                  str(s["decode_results"][i]["image_path"]).strip(str(s["dataset_path"])).split("/")[0] +
                  str(s["decode_results"][i]["image_path"]).strip(str(s["dataset_path"])).split("/")[1])
            # print("根据succed返回值获取 获取父目录", str(s["decode_results"][i]["image_path"]).split("/")[2:4])
            print("根据succed返回值获取 获取子目录",
                  str(s["decode_results"][i]["image_path"]).strip(str(s["dataset_path"])).split("/")[1])
            # 图片父目录
            father_dir.append((str(s["decode_results"][i]["image_path"]).strip(str(s["dataset_path"])).split("/")[
                                   0] + "/" +
                               str(s["decode_results"][i]["image_path"]).strip(str(s["dataset_path"])).split("/")[1]))
            print("father_dir is", father_dir)
            # 图片子目录
            child_dir.append(str(s["decode_results"][i]["image_path"]).strip(str(s["dataset_path"])).split("/")[1])
            print("child_dir is", child_dir)

        test_data = {"id": id,
                     "image_path": str(s["decode_results"][i]["image_path"]),
                     "image_name": str(s["decode_results"][i]["image_path"]).split("/")[-1],
                     "succeed": s["decode_results"][i]["succeed"],
                     "run_time": s["decode_results"][i]["run_time"],
                     "type": sheetname_type,
                     "result": result,
                     "target_result": "target_result",
                     "rect_points": rect_points}

        table_td_case = html.TABLE_TMPL_CASE % dict(id=test_data["id"], image_path=test_data["image_path"],
                                                    succeed=test_data["succeed"],
                                                    run_time=test_data["run_time"], type=test_data["type"],
                                                    result=test_data["result"],
                                                    target_result=test_data["target_result"],
                                                    rect_points=test_data["rect_points"])
        table_tr2 += table_td_case
        id+=1
        i += 1
# 计算false true 数量
succeed_false_count = succeed_list.count('false')
succeed_true_count = succeed_list.count('true')
# # 图片总数
image_total = len(s["decode_results"])
# 解码数量
Number_of_decoding = len(s["decode_results"])
# 解码率
decoding_rate = "{:.2%}".format(Number_of_decoding / image_total)
# 解码正确率
decoding_accuracy = "{:.2%}".format(succeed_true_count / Number_of_decoding)
# 解码最大耗时
run_time_max = max(run_time_list)
# 解码最小耗时
run_time_min = min(run_time_list)
# 解码平均耗时
run_time_avg = mean(run_time_list)
print("list_fail_image_path is", list_fail_image_path)
print("father_dir is", father_dir)
set(father_dir)
father_dir.sort()
print("sort  is", father_dir)
print("set(father_dir) is", set(father_dir))
print("succeed_list=succeed_list", succeed_list)
for i in range(len(set(father_dir))):
    list(set(father_dir)).sort()
    print("set(father_dir))is", list(set(father_dir)))
    print("set(father_dir))is", list(set(father_dir))[i])
    # 计算count
    father_dir.count(list(set(father_dir))[i])
    print("list(set(father_dir))[i]  count is", father_dir.count(list(set(father_dir))[i]))
    # 合并写入
    print("和并写入单行", (list(set(father_dir))[i] + ":" + str(father_dir.count(list(set(father_dir))[i]))))
    m = list(set(father_dir))[i] + ":" + str(father_dir.count(list(set(father_dir))[i]))
    fail_image_path_list.append(m)
    print("fail_image_path_list  is ", str(fail_image_path_list))
    print("fail_image_path_list  is ", str(fail_image_path_list).strip("[").strip("]").strip("'"))
    print("fail_image_path_list  is ",str(fail_image_path_list).strip("[").strip("]").strip("'").replace("', '", "\r\n"))
    i += 1
print("类型", father_dir)
print("数量", len(father_dir))
# 抽取变量
image_total = len(s["decode_results"])
Number_of_decoding = len(s["decode_results"])
decoding_rate = "{:.2%}".format(Number_of_decoding / image_total)
succeed_true_count = succeed_list.count('true')
decoding_accuracy = "{:.2%}".format(succeed_true_count / Number_of_decoding)
fail_path_total = str(fail_image_path_list).strip("[").strip("]").strip("'").replace("', '", "\r\n")
# sheetname_type=sheetname_type

# 实现html 显示


if __name__ == '__main__':

    id = 1
    test_result_data = {"序号": id,
                        "测试时间": s["date_time"],
                        "提交代码commit_id": "get_commit_id",
                        "测试数据集": s["dataset_path"],
                        "算法版本": s["version"],
                        "测试图片集": s["dataset_path"],
                        "解码率": decoding_rate,
                        "正确率": decoding_accuracy,
                        "平均耗时": run_time_avg,
                        "最大耗时": run_time_max,
                        "最小耗时": run_time_min,
                        "扫码失败总数": succeed_false_count,
                        "扫码失败文件分布": "fail_path_total",
                        "测试结果": "result_staus"}
    # 总表数据
    table_td = html.TABLE_TMPL_TOTAL % dict(序号=test_result_data['序号'],
                                            测试时间=test_result_data['测试时间'],
                                            提交代码commit_id=test_result_data['提交代码commit_id'],
                                            测试数据集=test_result_data['测试数据集'],
                                            算法版本=test_result_data["算法版本"],
                                            测试图片集=test_result_data["测试图片集"],
                                            解码率=test_result_data["解码率"],
                                            正确率=test_result_data["正确率"],
                                            平均耗时=test_result_data["平均耗时"],
                                            最大耗时=test_result_data["最大耗时"],
                                            最小耗时=test_result_data["最小耗时"],
                                            扫码失败总数=test_result_data["扫码失败总数"],
                                            扫码失败文件分布=test_result_data["扫码失败文件分布"],
                                            测试结果=test_result_data["测试结果"]
    )
    table_tr0 += table_td
    id += 1
    # 表头总数
    total_str = '共 %s，通过 %s，失败 %s' % (numfail + numsucc, numsucc, numfail)
    output = html.HTML_TMPL % dict(测试图片集=test_result_data["测试图片集"],value=total_str, table_tr=table_tr1, table_tr2=table_tr0, table_tr3=table_tr2)
    # 生成html报告
    filename = '{date}_TestReport.html'.format(date=time.strftime('%Y%m%d%H%M%S'))
    #filename = 'TestReport.html'
    print(filename)
    # 获取report的路径
    # dir= os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'report')
    dir = ('')
    filename = os.path.join(dir, filename)
    with open(filename, 'wb') as f:
        f.write(output.encode('utf8'))
