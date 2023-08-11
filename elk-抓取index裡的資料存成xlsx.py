#這隻程式用來抓取elasticsearch某個index裡的所有資料，將資料載下來並存到xlsx檔
import pandas as pd
from elasticsearch import Elasticsearch

# 连接到Elasticsearch
es = Elasticsearch(["http://192.168.8.22:9200"])

# 执行查询
query = {
    "query": {
        "match_all": {}  # 你的查询条件
    },
    "size": 10000  # 要下载的数据量
}

index_name = "user_exhibition"  # 替换为实际的索引名称

response = es.search(index=index_name, body=query, scroll="1m")
scroll_id = response["_scroll_id"]

# 获取滚动数据
data = []

while True:
    scroll_size = len(response["hits"]["hits"])
    
    for hit in response["hits"]["hits"]:
        data.append(hit["_source"])
    
    if scroll_size == 0:
        break
    
    response = es.scroll(scroll_id=scroll_id, scroll="1m")
    scroll_id = response["_scroll_id"]

# 将数据导出为Excel
#print(data)
df = pd.DataFrame(data)
excel_file = "out.xlsx"  # 输出文件名
df.to_excel(excel_file, index=False)
