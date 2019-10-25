import os
import sys

dir = '/Users/wangjinchao/Desktop/ste/ll'
delpath = '/Users/wangjinchao/Desktop/ste/rr'
# for path in paths:
#     if current_file in os.listdir(path) :
print('=='*12)
ll = os.listdir(dir)
dd = os.listdir(delpath)
result = []
for i in range(len(dd)):
    if dd[i] not in ll:
        print(dd[i])
        result.append(dd[i])

print(len(result))
# x=['101082.png','101413.png','10145.png','10182.png','10273.png','10337.png','104.png','10697.png','10759.png','1076.png','10809.png','10862.png','10926.png','10980.png','20185.png','20235.png','2027.png','203.png','2035.png','2037.png','2038.png','20402.png','20424.png','2043.png','20438.png','20475.png','20494.png']
#
# for i in range(len(ll)):
#     if str(ll[i]) not in x:
#         print(ll[i])


