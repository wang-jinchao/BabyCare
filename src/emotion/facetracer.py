#!/usr/bin/env python
"""A simple script to display information about faces from the facetracer dataset.
This is useful for quickly seeing all the relevant data for a given face id.
It also shows how easy it is to parse the data for your own applications.

Note that fiducial point locations are RELATIVE TO THE CROP RECTANGLE.

You can use 'grep' on the output to just show particular fields.

Dataset webpage: http://www.cs.columbia.edu/CAVE/databases/facetracer/
"""
import os
import urllib.request
def cbk(a,b,c):
    '''回调函数
    @a:已经下载的数据块
    @b:数据块的大小
    @c:远程文件的大小
    '''
    per=100.0*a*b/c
    if per>100:
        per=100
    print('%.2f%%' % per)

USAGE = '''FaceTracer dataset explorer, v1.0'
Usage: %s <face id>
'''

FIELDS = 'face_id crop_width crop_height crop_x0 crop_y0 yaw pitch roll left_eye_x0 left_eye_y0 left_eye_x1 left_eye_y1 right_eye_x0 right_eye_y0 right_eye_x1 right_eye_y1 mouth_x0 mouth_y0 mouth_x1 mouth_y1'.split()

def getLinesById(id, fname):
	"""Returns the lines split by '\t' where the first element is the given id"""
	lines = (l.strip().split('\t') for l in open(fname) if not l.startswith('#'))
	ret = [l for l in lines if int(l[0]) == int(id)]
	return ret

def fix(s):
	"""Fixes a string by replacing _ with spaces and putting it in title case"""
	return s.replace('_', ' ').title()

if __name__ == '__main__':
	import sys
	# if len(sys.argv) < 2:
	# 	print(USAGE % (sys.argv[0]))
	# 	sys.exit()
	# id = sys.argv[1]
	xx = [11601, 11637, 11638, 11640, 11641, 11642, 11643, 11644, 11646, 11647, 11648, 11649, 11650, 11651, 11652, 11688, 11703, 11739, 11748, 11789, 11795, 11798, 11806, 12239, 12268, 12280, 12332, 12335, 12337, 12338, 12340, 12503, 12504, 12507, 12508, 12509, 12511, 12836, 12870, 12964, 12971, 12973, 12976, 12977, 12980, 13000, 13144, 13363, 13453, 13480, 13481, 13482, 13489, 13491, 13493, 13631, 13633, 13734, 13735, 13736, 13737, 13738, 13739, 13788, 13791, 14001, 14096, 14097, 14098, 14099, 14102, 14103, 14104, 14105, 14106, 14107, 14108, 14109, 14110, 14111, 14195, 14198, 14200, 14201, 14202, 14203, 14205, 14266, 14290, 14291, 14292, 14293, 14294, 14321, 14453, 14470, 14471, 14472, 14473, 14474, 14507, 14509, 14524, 14533, 14541, 14566, 14567, 14570, 14571, 14591, 14605, 14606, 14607, 14608, 14617, 14630, 14690, 14691, 14700, 14703, 14704, 14705, 14706, 14710, 14711, 14712, 14713, 14714, 14715, 14723, 14746, 14747, 14775, 14788, 14791, 14792, 14793, 14802, 14812, 14813, 14828, 14839, 14851, 14852, 14855, 14856, 14859, 14863, 14864, 14865, 14867, 14868, 14869, 14870, 14872, 14878, 14881, 14882, 14884, 14885, 14886, 14888, 14890, 14891, 14894, 14895, 14896, 14897, 14899, 14901, 14904, 14908, 14910, 14911, 14913, 14914, 14915, 14916, 14917, 14928, 14931, 14933, 14934, 14935, 14937, 14939, 14940, 14941, 14942, 14944, 14945, 14949, 14951, 14952, 14953, 14954, 14958, 14961, 14962, 14964]
	for id in range(len(xx)):
		try:
			stats = getLinesById(xx[id], 'facestats.txt')[0]
			# for f, s in zip(FIELDS, stats):
			# 	print('%s: %s' % (fix(f), s))
			urls = getLinesById(xx[id], 'faceindex.txt')[0]
			imgurl, pageurl = urls[1:]
			print(str(xx[id])+'=='*8)
			# print('Image URL:', imgurl)
			# print('Page URL:', pageurl)
			# attrs = getLinesById(id, 'facelabels.txt')
			# for fid, attr, label in attrs:
			# 	print('%s: %s' % (fix(attr), fix(label)))
			dir=os.path.abspath('./base')  
			work_path=os.path.join(dir,str(xx[id])+imgurl[-4:])  
			urllib.request.urlretrieve(imgurl,work_path,cbk)  
		except IndexError:
			continue
		except ValueError:
			continue
		except urllib.error.HTTPError:
			continue
		except urllib.error.URLError:
			continue

