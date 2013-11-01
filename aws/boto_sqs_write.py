import boto, json, uuid


sqs = boto.connect_sqs()
queue = sqs.create_queue('msg_pump')
data = json.dumps({'name': 'alex', 'age': 28})

s3 = boto.connect_s3()
bucket = s3.create_bucket('bepec.mysite.com')
key = bucket.new_key('data-%s.json' % uuid.uuid4())
key.set_contents_from_string(data)
source_handle = {'bucket': bucket.name, 'key': key.name}
message = queue.new_message(body=json.dumps(source_handle))
queue.write(message)
