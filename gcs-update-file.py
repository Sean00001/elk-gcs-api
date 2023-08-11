#將檔案從地端append到gcs
from google.cloud import storage
client = storage.Client.from_service_account_json('aib2bpoc-78af3836f1bd.json')


def update_file(bucket_name, blob_name, new_content):
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # Upload the new content
    blob.upload_from_string(new_content, content_type='text/plain')

    print(f'File {blob_name} in bucket {bucket_name} updated with new content.')

# Specify the bucket name, blob (file) name, and the new content
bucket_name = 'aib2bdata'
blob_name = 'text.txt'
new_content = 'This is the updated content.'

update_file(bucket_name, blob_name, new_content)