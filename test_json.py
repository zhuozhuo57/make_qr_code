import configparser
import os
import re
import openpyxl
file = os.path.dirname(os.path.abspath(__file__))
config = configparser.ConfigParser()
#print(config)
s = config.read(file + r'\config.ini')
excelPath = config.get("Local", "ResultPath")
filePath = config.get("Local", "logPath")
data = openpyxl.load_workbook(excelPath)
sheet = data['Sheet1']
sheet.cell(1, 1).value = 'date_time'
sheet.cell(1, 2).value = "version"
sheet.cell(1, 3).value = "dataset_path"
count = 0
succeed_false_count = 0
succeed_true_count = 0
image_path_line_count=0
# sheet.cell(1, 4).value = "code_type"
with open(filePath, 'r', encoding="utf-8") as f:
    readlines = f.readlines()
    #print("readlines  is ", readlines)
    h = 0

    for s in readlines:
        #实现表的项写入
        if ('image_path' in s):
            sheet.cell(4, 1).value = 'image_path'
            data.save(excelPath)
        if ('succeed' in s):
            sheet.cell(4, 2).value = 'succeed'
            data.save(excelPath)
        if ('run_time' in s):
            sheet.cell(4, 3).value = 'run_time'
            data.save(excelPath)
        if ('results' in s):
            sheet.cell(4, 4).value = 'results'
            data.save(excelPath)
        if ('date_time' in s):
            #print("date_time is",s)
            date_time = re.findall(r'"date_time":(.*)"version":(.*),"dataset_path":(.*),',s)
            # print("date_time is" ,date_time)
            # print("date_time[0] is",date_time[0])
            # print("date_time [0][0] is",date_time[0][0])
            # print("version is",date_time[0][1])
            dataset_path=str(date_time[0][2]).strip(',').split(',')[0]
            #print("dataset_path is",dataset_path)
            # 实现提取date_time
            # print(date_time[0])
            # print(type(date_time[0]))
            # 实现date_time_value 写入
            date_time_value = date_time[0][0]
            # print("date_time_value is",date_time_value)
            # print(type((date_time[0])[0]))
            sheet.cell(2, 1).value = date_time_value
            data.save(excelPath)
            # 实现version写入
            version = date_time[0][1]
            # print("version_value is",version)
            # print(type((date_time[0])[1]))
            sheet.cell(2, 2).value = version
            data.save(excelPath)
            # 实现dataset_path写入
            dataset_path = str(date_time[0][2]).strip(',').split(',')[0]
            #print("dataset_path is", dataset_path)
            sheet.cell(2, 3).value = dataset_path
            data.save(excelPath)
        #实现decode_results 字符处理
        # print("s is",s)

            decode_results = re.findall(r'"decode_results":(.*)', s)
            print("decode_results is ",decode_results)
            print("decode_results type is ",type(decode_results))
            #字符串处理
            decode_result=str(decode_results).strip("['[{").strip("]}']")
            print("decode_result is",decode_result)
            list_decode_result=decode_result.split("},{")
            print("list_decode_result is",list_decode_result)
            for i in range(len(list_decode_result)-1):
                print("list_decode_result is",list_decode_result[i])
                print("list_decode_result is",list_decode_result[i].split(","))
                image_name=list_decode_result[i].split(",")[0].split("/")[-1].strip("\"")
                print("image_name is",image_name)
                succeed=list_decode_result[i].split(",")[1].split(":")[1].strip("\"").strip("\"")
                print("succeed is",succeed)
                run_time=list_decode_result[i].split(",")[2].split(":")[1].strip("\"").strip("\"")
                print("run_time is",run_time)
                results=list_decode_result[i].split(",")[3].split(":")[1].strip("\"").strip("\"")
                print("results is",results)
                if (succeed == 'false'):
                    succeed_false_count += 1
                    print("succeed_false_count is ", succeed_false_count)
                elif (succeed == 'true'):
                    succeed_true_count += 1
                    print("succeed_true_count is ", succeed_true_count)
                #实现数据写入
                sheet.cell(i + 5, 1).value = image_name
                data.save(excelPath)
                sheet.cell(i + 5, 2).value = succeed
                data.save(excelPath)
                sheet.cell(i + 5, 3).value = run_time
                data.save(excelPath)
                sheet.cell(i + 5, 4).value = results
                data.save(excelPath)
                i+=1

            #decode_results.remove(s2)
            #print("decode_results is",decode_results)
            # print("decode_results title is ",str(decode_results).title().split("}")[-3])
            # #中间行处理
            # print("decode_results title is ",str(decode_results).title().split("}")[-4].strip(",{"))

            #dict=
            # print("list decode_results  is ",decode_results[0])
            # print("str decode_results  is ",str(decode_results[0]).strip(","))
            # print("decode_results[0] is ",decode_results[0])
            # print("decode_results[0] is ",str(decode_results[0]).strip("{").strip("}"))
            #print("decode_results is ",decode_results)
            # print("decode_results 【0】 is ",list(str(decode_results[0]).split("{")))
            # #print("decode_results 【0】 is ",list(str(decode_results[0]).strip("[").split("{")))
            # print("decode_results 【0】 is ",list(str(decode_results[0]).strip("]").strip("[").split("{")))
            # #print("decode_results 【0】 is ",str(list(str(decode_results[0]).split("{"))).split("}"))

            # # print("decode_results[0] type is ",type(decode_results[0]))
            # print("str(decode_results[0]).split(",") is ",str(decode_results[0]).split("},"))
            # print("str(decode_results[0]).split(",") type is ",type(str(decode_results[0]).split(",")))

            # newline=str(decode_results[0])
            # #print("newline is ",newline[0])
            # print("newline is remove [-2] ",str(newline.split("}")).split("{"))
            # strings=str(newline.split(","))
            # print("strings is ",strings[0])
            # print("strings is ",strings[1])
            # print("newline is ",newline[-1])
            # print("newline is 1:-1 ",newline[1:-1])
            # print("newline is 1：-1 split ",newline[1:-1].split("},"))
            # print("newline is 1：-1 split strip ",newline[1:-1].split("},").)
            # for i in range(len(newline)-1):
            #     print("newline is 1：-1 split [0] ",newline[1:-1].split("},")[i].split("{")[1])
            #     i+=1
            # for i in range(len(newline)-1):
            #     print("newline [%s] is",i,newline[i])
            # if("image_path" in  newline ):
            #     print("newline spilt ", str(newline).split(":"))



                # i+=1
            # print("list 1 is ",str(decode_results[0]).split(",")[0])
            # print("list 1 is ",str(decode_results[0]).split(",")[15])
            # print("list -1 is ",str(decode_results[0]).split(",")[-1])
    # #实现image_name写入表中
    #         image_path_line = re.findall(r'"image_path":(.*),"succeed":(.*),"run_time":(.*),"results":(.*)',
    #                                      str(newline[0]))
    #         #print("image_path_line is", image_path_line)
            # print("image_path_line type is", type(image_path_line))
            # print("image_path_line[0]", newline[0])
            # print("image_path_line[1] is", newline[1])
            # print("image_path_line[2] is", newline[2])
            # print("image_path_line[3] is", newline[3])
            # image_path=re.findall(r'"image_path":(.*)',str(newline[0]))
            # print("image_path is", image_path)
            # print("image_path【0】 is", image_path[0])
            # print("image_path【0】 is", str(image_path[0]).split("/"))
            # print("image_path【0】 is", str(image_path[0]).split("/")[4].strip("\""))


            # sheet.cell(h + 5, 1).value = str(image_path.pop()[1:-1]).split("/")[4]
            # data.save(excelPath)
            # image_path_v=str(image_path.pop()[1:-1]).split("/")[4]
            # # print(image_path_v)
            # # print("image_path name type is", type(str(image_path.pop()[1:-1]).split("/")[4]))
            # succeed=re.findall(r'"succeed":(.*)',str(newline[1]))
            #
            # print("succeed pop is", str(succeed).split("\"")[1])
            # #print("succeed pop  type is", type(succeed.pop()[1:-1]))
            # # print("succeed is", str(succeed.pop()))
            # run_time=re.findall(r'"run_time":(.*)',str(newline[2]))
            # print("run_time is", str(run_time).split("\'")[1])
            # results=re.findall(r'"results":(.*)',str(newline[3]))
            # print("results is", str(results))
            # print("results is", str(results).split("\'")[1])
            # print("results is", str(results).split("\'")[1].strip("\}"))
            # # print("image_path_line type  is", type(image_path_line))
    # #    # 实现image_name写入表中
    #         sheet.cell(h + 5, 1).value = str(image_path[0]).split("/")[4].strip("\"")
    #         data.save(excelPath)
    #         # 实现succed写入表中
    #         succeed = succeed
    #         print("succeed is", (succeed))
    #         if (succeed == 'false'):
    #             succeed_false_count += 1
    #             print("succeed_false_count is ", succeed_false_count)
    #         elif (succeed == 'true'):
    #             succeed_true_count += 1
    #             print("succeed_true_count is ", succeed_true_count)
    #
    #         print(succeed_false_count, succeed_true_count)
    #         print(type(succeed))
    #         sheet.cell(h + 5, 2).value = str(succeed).split("\"")[1]
    #         data.save(excelPath)
    #         # 实现runtime写入表中
    #         sheet.cell(h + 5, 3).value = str(run_time).split("\'")[1]
    #         data.save(excelPath)
    #         # 实现results写入表中
    #         sheet.cell(h + 5, 4).value = str(results).split("\'")[1].strip("\}")
    #         data.save(excelPath)
    #         image_path_line_count += 1
    #         print("image_path_line_count is", image_path_line_count)
            h += 1







    #
    # # 实现统计行数及结果判断得出解码率
    #      total=["统计","图片数量（数据集所有图片）","解码数量（读取成功图片）","解码正确图片","解码失败图片","解码率（解码数量除以图片数量）","解码正确率（解码正确图除以解码数量）","最大解码耗时","最小解码耗时","平均解码耗时","解码失败类型/数量"]
    #      j=0
    #      for j in range(len(total)-1):
    #          sheet.cell(j+4, 5).value = total[j]
    #          print("total is",total[j])
    #          # sheet.cell(4, 6).value = '图片数量（数据集所有图片）'
    #          # sheet.cell(4, 7).value = '解码数量（读取成功图片）'
    #          # sheet.cell(4, 6).value = '解码正确图片'
    #          # sheet.cell(4, 6).value = '解码失败图片'
    #          # sheet.cell(4, 6).value = '解码率（解码数量除以图片数量）'
    #          # sheet.cell(4, 6).value = '解码正确率（解码正确图除以解码数量）'
    #          # sheet.cell(4, 6).value = '最大解码耗时'
    #          # sheet.cell(4, 6).value = '最小解码耗时'
    #          # sheet.cell(4, 6).value = '平均解码耗时'
    #          # sheet.cell(4, 6).value = '解码失败类型/数量'
    #          j+=1
    #      data.save(excelPath)
    #      # total_results=[""]
    #      # x="正确比对结果数量计算"
    #      # '''最大耗时'''
    #      # run_time_vlaues=[]
    #      # h=0
    #      # mmm=join(run_time)
    #      # h+=1
    #      # print("run_time_vlaues is ",str(mmm))
    #      # run_time_max=run_time.max
    #      # run_time_mix=run_time.mix
    #      # run_time_avg=run_time.avg
    #      # with open('','r',encoding="utf-8")as f:
    #      #     total_results[1] =len(f.readlines())
    #      # total_results[2]=image_path_line_count
    #      # total_results[3]=succeed_true_count
    #      # total_results[4]=succeed_false_count
    #      # total_results[5]=total_results[2]/total_results[1]
    #      # total_results[6]=x/succeed_true_count
    #      # total_results[7]=x/succeed_true_count
    #      #
    #      # if (succeed=="false"):
    #      #     succeed_false_count=i-1
    #      #     #count+=1
    #      #     print("succeed_false_count is",succeed_false_count)
    #      #     #count+=1
    #      #     #print("count is ",count,succeed_false_count)
    #      # else:
    #      #     succeed_true_count = i+1
    #      #     #count+=1
    #      #     print("succeed_true_count is", succeed_true_count)
    #      #     #count+=1
    #      #
    #      # print("succeed_false_count is", succeed_false_count)
    #      # print("succeed_true_count is", succeed_true_count)
    #      # print("count is ", succeed_true_count+ succeed_false_count)

'''            if(succeed=='false'):
                succeed_false_count+=1
                print("succeed_false_count is ", succeed_false_count)
            elif(succeed=='true'):
                succeed_true_count+=1
                print("succeed_true_count is ", succeed_true_count)
            print(succeed_false_count,succeed_true_count)'''