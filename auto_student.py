import time

import helium as hl

hl.start_chrome(
    'http://eln.hydsoft.net:8081/elms/web/course/browse/viewAiccCourse.action?userId=H012478&courseId=SELFM00082&typeId=1')

hl.write('chenxinyu@hydsoft.com', into='用户名/邮箱')
time.sleep(2)
hl.write('xxx', into='密码')
time.sleep(2)
hl.click('登 录')
time.sleep(2)
hl.click('2021新员工入职培训 ')
time.sleep(20)
for i in range(40):
    time.sleep(3)
    hl.press(hl.SPACE)