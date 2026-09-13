def on_forever():
    pass
basic.forever(on_forever)
# MakeCode micro:bit Python 코드
# microbit 모듈은 MakeCode에서 자동으로 인식됨

from microbit import *

# 변수 설정
current_velocity = 0
max_velocity = 255
max_change = 10

while True:
    # 1. 가속도값 읽기
    accel_total = accelerometer.get_x() + accelerometer.get_y() + accelerometer.get_z()
    
    # 2. 가속도에 따라 목표 속도 계산
    if accel_total < 0:
        accel_total = -accel_total
    
    accel_ratio = accel_total // 50
    if accel_ratio > 100:
        accel_ratio = 100
    
    target_velocity = max_velocity * (100 - accel_ratio) // 100
    
    # 3. 부드럽게 속도 변경
    if target_velocity > current_velocity:
        if target_velocity - current_velocity > max_change:
            current_velocity += max_change
        else:
            current_velocity = target_velocity
    else:
        if current_velocity - target_velocity > max_change:
            current_velocity -= max_change
        else:
            current_velocity = target_velocity
    
    # 4. 모터에 속도 적용 (P0 핀)
    pin0.write_analog(current_velocity)
    
    # 5. LED에 속도 표시
    display.scroll(str(current_velocity))
    
    # 대기
    sleep(100)