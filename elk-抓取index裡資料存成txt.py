from elasticsearch import  Elasticsearch

es = Elasticsearch(hosts='http://192.168.8.22',port=9200)

print(es.info())
query = {
    "query": {
        "match_all": {}
    }
}

# 执行查询
search_result = es.search(index='user_exhibition', body=query)


print(search_result)

import json



# 將JSON寫入TXT檔案，並使用縮進進行美化
with open("test2.txt", "w") as txt_file:
    json.dump(search_result, txt_file, indent=4)
#res=es.find()
#print(res)
