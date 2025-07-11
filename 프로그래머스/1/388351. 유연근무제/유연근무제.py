# time에 10분을 더한 시각 구하는 함수
def plus10(time):
    time_str = str(time)
    
    hour = int(time_str[:-2])
    minute = int(time_str[-2:])
    
    minute += 10    # 분에 10 더하기
    hour += minute // 60    # 0 또는 1 증가
    minute = minute % 60    # 60 이하의 값
    
    return hour * 100 + minute


def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)  # 직원의 수
    
    # 직원 순회
    for i in range(n):
        s = schedules[i]        # 직원이 설정한 희망 시각
        deadline = plus10(s)    # 실제 데드라인 (희망 + 10분)
        flag = True             # 직원이 상품을 받을 수 있는지의 여부
        
        print(deadline)
        
        # 이벤트 시작 후 j일차 (0일차부터 시작)
        for j in range(7):
            t = timelogs[i][j]  # j일차의 실제 출근 시각
            
            # 하루 이상의 평일에 지각한 경우
            is_weekend = (startday + j) % 7 == 6 or (startday + j) % 7 == 0     
            if not is_weekend and t > deadline:
                flag = False    # 상품을 받을 수 X
                break
        
        if flag:
            answer += 1
            
    return answer