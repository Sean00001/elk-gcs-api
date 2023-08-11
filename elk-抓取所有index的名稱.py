from elasticsearch import  Elasticsearch

es = Elasticsearch(hosts='http://192.168.8.22',port=9200)

print(es.info())
query = {
    "query": {
        "match_all": {}
    }
}

# 执行查询
search_result = es.search(index='my_index', body=query, size=10000)
print("aaaa")
for hit in search_result['hits']['hits']:
    source_data = hit['_source']
    print(source_data)
#res=es.find()
#print(res)
