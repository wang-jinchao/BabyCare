import glob
import os
IMG_PATH = '/home/wangjinchao/segnet/data/CamVid/test' #原图像的路径
MASK_PATH = '/home/wangjinchao/segnet/data/CamVid/testannot'#mask的路径，注意这里的mask值是uint8型的0和1
img_paths = glob.glob(os.path.join(IMG_PATH, '*.png'))
mask_paths = glob.glob(os.path.join(MASK_PATH,'*.png'))
img_paths.sort()
mask_paths.sort()
image_mask_pair = zip(img_paths, mask_paths)
image_mask_pair = list(image_mask_pair)
file=open('/home/wangjinchao/segnet/data/CamVid/test.txt','w') #写入一个txt文件
for image_path, mask_path in image_mask_pair:
    temp = image_path + ' ' +mask_path   #注意单引号之间有个空格
    file.write(temp +'\n')
file.close()