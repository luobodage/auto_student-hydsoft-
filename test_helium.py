import helium as hl
import time
hl.start_chrome('https://baidu.com')

hl.write('nihao')
for i in range(40):
    time.sleep(3)
    hl.press(hl.SPACE)