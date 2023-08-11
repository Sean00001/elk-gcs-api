#將本機端資料上傳到gcs，資料會直接覆蓋不會append
from google.cloud import storage

# 设置您的凭据路径
credentials_path = 'aib2bpoc-78af3836f1bd.json'

# 初始化 GCS 客户端
client = storage.Client.from_service_account_json(credentials_path)

# 指定 GCS 存储桶和对象名称
bucket_name = 'aib2bdata'
object_name = 'rrr'

# 上传本地文件到 GCS
local_file_path = 'test2.txt'
bucket = client.bucket(bucket_name)
blob = bucket.blob(object_name)
blob.upload_from_filename(local_file_patupdateh)

print(f'File {local_file_path} uploaded to {object_name} in {bucket_name}')