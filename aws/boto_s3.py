import boto


s3 = boto.connect_s3()
bucket = s3.create_bucket('bepec.mysite.com')
key = bucket.new_key('dotfiles/_vimrc')
key.set_contents_from_filename('/home/miracast/.vimrc')
key.set_acl('public-read')
