#rename#
import os

IMAGE_PATH = os.path.join(os.getcwd())
#FILE_PATH = os.getcwd()
#fileList = os.getcwd()
fileList = os.listdir(IMAGE_PATH)

for im_name in fileList:
 if im_name.endswith('_cubefront.png'):
   orig=im_name
   replace = im_name[:-13] + 'posz.png'
   os.rename(orig,replace)
 if im_name.endswith('_cubeback.png'):
   orig=im_name
   replace = im_name[:-12] + 'negz.png'
   os.rename(orig,replace)
 if im_name.endswith('_cubetop.png'):
   orig=im_name
   replace = im_name[:-11] + 'posy.png'
   os.rename(orig,replace)
 if im_name.endswith('_cubebottom.png'):
   orig=im_name
   replace = im_name[:-14] + 'negy.png'
   os.rename(orig,replace)
 if im_name.endswith('_cubeleft.png'):
   orig=im_name
   replace = im_name[:-12] + 'negx.png'
   os.rename(orig,replace)
 if im_name.endswith('_cuberight.png'):
   orig=im_name
   replace = im_name[:-13] + 'posx.png'
   os.rename(orig,replace)
 