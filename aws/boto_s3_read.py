import boto


s3 = boto.connect_s3()
key = s3.get_bucket('bepec.mysite.com').get_key('dotfiles/_vimrc')
key.get_contents_to_filename('/home/miracast/myvimrc')
