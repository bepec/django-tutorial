import boto, json


sqs = boto.connect_sqs()
queue = sqs.get_queue('msg_pump')
message = queue.read()

if message:
    source_handle = json.loads(message.get_body())
    s3 = boto.connect_s3()
    bucket = s3.get_bucket(source_handle['bucket'])
    key = bucket.get_key(source_handle['key'])
    data = json.loads(key.get_contents_as_string())
    print data
    queue.delete_message(message)
