# -*- coding: utf-8 -*-
# external modules: pythonmagick
# http://www.imagemagick.org/

import PythonMagick as pm
import os

# configuration
diri = 'Z:/inputdir'
diro = 'J:/outputdir'
maxd = 1280

#setup
try:
    os.stat(diro)
except:
    os.mkdir(diro)

# process images
subdirlist = [name for name in os.listdir(diri) if os.path.isdir(os.path.join(diri,name))]
for subdir in subdirlist:
    imagelist = [name for name in os.listdir(diri+'/'+subdir) if os.path.isfile(os.path.join(diri+'/'+subdir,name))]
    for image in imagelist:
        img=pm.Image(pm.Blob(file(diri+'/'+subdir+'/'+image,'rb').read()))
        size = img.size()
        if size.height()>maxd or size.width()>maxd:
            img.resize('>%sx%s'%(maxd,maxd))
        try:
            os.stat(diro+'/'+subdir)
        except:
            os.mkdir(diro+'/'+subdir)
        img.write(diro+'/'+subdir+'/'+image)
