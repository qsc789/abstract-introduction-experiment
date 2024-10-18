import csv
def tools(data):
    list1 = data.split(',')
    list2 = list1[4:-5]
    l1 = []
    l2 = []
    l3 = []
    for i in list2:
        val = i[4:]
        tag = i[0:4]
        if '本科' in tag:
            l1.append(val)
        elif '硕士' in tag:
            l2.append(val)
        elif '博士' in tag:
            l3.append(val)
    final_list=[l1,l2,l3]
    return final_list


if __name__ == '__main__':
    f = open("D:/data(3).csv", encoding='utf-8')
    reader = csv.reader(f)
    headers = next(reader)
    # 加字段
    new_field = '本科需求专业'
    headers.append(new_field)
    new_field = '硕士需求专业'
    headers.append(new_field)
    new_field = '博士需求专业'
    headers.append(new_field)
    # print(headers)
    # 创建一个新的CSV文件，包含新的字段
    with open('output.csv', 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(headers)  # 写入新的表头

    data_lines = f.readlines()
    # print(data_lines[0])
    data_lines.pop(0)
    for line in data_lines:
        final_list=tools(line)
        list1= final_list[0]
        list2= final_list[1]
        list3= final_list[2]
        temp_list=line.split(',')
        final_data=[temp_list[0],temp_list[1],temp_list[2],temp_list[3],temp_list[4:-5],temp_list[-5],temp_list[-4],temp_list[-3],temp_list[-2],temp_list[-1],list1,list2,list3]
        with open('output.csv', 'a', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(final_data)
