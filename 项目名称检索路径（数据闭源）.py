# import pandas as pd
# import jieba
# from pymysql import Connection
#
# # 定义函数来切分词汇，过滤掉无用词汇
# def cut_words(text):
#     list1 = jieba.lcut(text)
#     stopwords = ['大','小','上','下','与','的','、','和','及','中','（','）','“','”','（',' ','并','与','及其',
#                  '：','-','可','全','一种','实现','—','化','设备','多','侧','用户','基于','需求','测',
#                  '在','站','用','用于','新一代','特性','能力','形式','研制','线路','运','大型','换','综合','智','提升',
#                  '调度','面向','宽','网','调','微','方案','电','方法','库','建立','高性能','型','定',
#                  '相','法','物','式','变','一次','度','不','~','物质','厂','圈','长','问题','部件','研发','》','《','平台',
#                  '----','对','年','带','/','后','稳定','等','标准','整合','新','(','组','台','关系','器',
#                  '为','以','主','#','1','现有','重大']
#     filtered_list = [word for word in list1 if word not in stopwords]
#     return filtered_list
#
# # 读取 CSV 文件
# data = pd.read_csv("D:\汇总表 _to_stud.csv")
#
# # 连接数据库
# conn = Connection(
#     host="localhost",
#     port=3306,
#     user="root",
#     password="Lc20050612."
# )
#
# # 选择数据库
# conn.select_db("experiment")
# cursor = conn.cursor()
#
# # 定义要插入数据的起始行和列
# start_row = 3  # 对应第四行（0基索引）
# start_col_idx = 11  # 对应L列是第12列（0基索引）
#
# # 遍历 CSV 文件中的每一行，提取路径并查询数据库
# for idx, line in enumerate(data.values):
#     list1 = cut_words(line[1])  # 提取关键词
#
#     # 生成查询语句
#     query = "SELECT C1 FROM demo WHERE "
#     conditions = ["C2 LIKE '%{}%'".format(item) for item in list1]
#     query += " AND ".join(conditions)
#
#     # 执行查询并获取结果
#     cursor.execute(query)
#     res = cursor.fetchall()
#
#     # 如果有结果，选择匹配数量最多的结果
#     if res:
#         max_match_result = max(res, key=lambda x: len(x))
#         data.iloc[idx + start_row, start_col_idx] = str(max_match_result)
#     n = len(res)  # 假设每个拆分后的字段包含5个字符
#
#     # 创建一个新的DataFrame来存储拆分后的数据
#     new_columns = [f'匹配文件名{i}' for i in range(1, n + 1)]
#     new_data = pd.DataFrame(columns=new_columns)
#
#     # 遍历每一行数据，拆分文本字段并添加到新的DataFrame中
#
#     split_text = [res[i] for i in range(0, len(res))]
#     new_row = pd.Series(split_text, index=new_columns)
#     new_data = new_data.append(new_row)
#
#     # 保存拆分后的数据到新的CSV文件
#     new_data.to_csv('C:/Users/l1361/Desktop/汇总表 _to_stud1.csv', index=False)
#
#
#
# # 关闭数据库连接
# conn.close()
#
# print("处理完成，结果已保存至 CSV 文件。")
import pandas as pd
import jieba
from pymysql import Connection

# 定义函数来切分词汇，过滤掉无用词汇
def cut_words(text):
    list1 = jieba.lcut(text)
    stopwords = ['大','小','上','下','与','的','、','和','及','中','（','）','“','”','（',' ','并','与','及其',
                 '：','-','可','全','一种','实现','—','化','设备','多','侧','用户','基于','需求','测',
                 '在','站','用','用于','新一代','特性','能力','形式','研制','线路','运','大型','换','综合','智','提升',
                 '调度','面向','宽','网','调','微','方案','电','方法','库','建立','高性能','型','定',
                 '相','法','物','式','变','一次','度','不','~','物质','厂','圈','长','问题','部件','研发','》','《','平台',
                 '----','对','年','带','/','后','稳定','等','标准','整合','新','(','组','台','关系','器',
                 '为','以','主','#','1','现有','重大']
    filtered_list = [word for word in list1 if word not in stopwords]
    return filtered_list

# 读取 CSV 文件
data = pd.read_csv("C:/Users/l1361/Desktop/汇总表 _to_stud.csv")
data.drop(0)
# 连接数据库
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="Lc20050612."
)

# 选择数据库
conn.select_db("experiment")
cursor = conn.cursor()

# 定义要插入数据的起始行和列
start_row = 1  # 对应第二行（0基索引）
start_col_idx = 11  # 对应L列是第12列（0基索引）


# 遍历 CSV 文件中的每一行，提取路径并查询数据库
for idx, line in enumerate(data.values):
    list1 = cut_words(line[1])  # 提取关键词
    # print(list1)
    # 生成查询语句
    query = "SELECT C1 FROM demo WHERE "
    conditions = ["C2 LIKE '%{}%'".format(item) for item in list1]
    query += " AND ".join(conditions)

    # 执行查询并获取结果
    cursor.execute(query)
    res = cursor.fetchall()

    n = len(res)
    # 重命名拆分后的字段
    for i in range(1, n+1):
        data.iloc[idx + start_row, start_col_idx+i-1] = str(res[i-1])


# 保存修改后的 CSV 文件
data.to_csv("C:/Users/l1361/Desktop/汇总表 _to_stud.csv", index=False)

# 关闭数据库连接
conn.close()

print("处理完成，结果已保存至 CSV 文件。")
