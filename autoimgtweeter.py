# -*- coding: utf-8 -*-
#
# external modules: python-twitter, pythonmagick
# https://code.google.com/p/python-twitter/
# http://www.imagemagick.org/
#
# TODO
# - self-posting loop
# - automated interval adjustment based on number of images



import twitter
import PythonMagick as pm
import os
from random import randint

# twitter auth
ckey = 'CONSUMER_KEY'
csec = 'CONSUMER_SECRET'
akey = 'ACCESS_TOKEN_KEY'
asec = 'ACCESS_TOKEN_SECRET'

# configuration
message = 'Image created on %s'
imageout = 'twitteroutput.jpg'
imagedir = 'C:/IMAGE/PATH'
maxd = 1280

# find random image
subdirlist = [name for name in os.listdir(imagedir) if os.path.isdir(os.path.join(imagedir,name))]
subdir = subdirlist[randint(0,len(subdirlist)-1)]
datestr = subdir[0:4]+'-'+subdir[4:6]+'-'+subdir[6:8] #assumes dir is a date in YYYYMMDD format
imagelist = [name for name in os.listdir(imagedir+'/'+subdir) if os.path.isfile(os.path.join(imagedir+'/'+subdir,name))]
image = imagelist[randint(0,len(imagelist)-1)]

# process image
img=pm.Image(pm.Blob(file(imagedir+'/'+subdir+'/'+image,'rb').read()))
img.resize('>%sx%s'%(maxd,maxd))
img.write(imageout)

# post to twitter
api = twitter.Api(consumer_key=ckey,consumer_secret=csec,access_token_key=akey,access_token_secret=asec)
api.PostMedia(message%(datestr),imageout)

# cleanup
os.remove(imageout)
