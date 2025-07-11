def solution(cards):
    max_w = 0
    max_h = 0
    
    # 각 명함을 순회
    for card in cards:
        # 명함 중 더 긴 쪽을 가로, 더 짧은 쪽을 세로로 설정
        w = max(card[0], card[1])
        h = min(card[0], card[1])
        
        # 가장 긴 가로, 세로 길이 구하기
        max_w = max(max_w, w)
        max_h = max(max_h, h)
        
    answer = max_w * max_h
    
    return answer



# def solution(arr):
#     n = len(arr)  # 명함의 개수
#     answer = 1000000
#     cards = [i for i in range(n)]   # 모든 명함의 번호 (0 ~ n-1)

#     # 명함이 n개라면, 최대 n/2개의 명함을 뒤집을 수 있음.
#     # ex. 명함 5개 → 2개 뒤집는 경우 = 3개 뒤집는 경우
#     for i in range(1, int(n/2) + 1):
#         # i개의 명함 뒤집는 모든 조합
#         selected_coms = itertools.combinations(cards, i)
        
#         # 각 조합 케이스별 뒤집는 명함 순서쌍의 번호 조회
#         for selected_cards in selected_coms:
#             # 각 조합 케이스별 가장 큰 w, h 구하기
#             max_w = 0
#             max_h = 0
     
#             # 명함을 뒤집으면서 지갑의 크기 구하기
#             for j in range(n):
#                 # j번째 명함을 뒤집은 경우
#                 if j in selected_cards:
#                     max_w = max(max_w, arr[j][1])
#                     max_h = max(max_h, arr[j][0])
#                 # j번째 명함을 뒤집지 않은 경우
#                 else:
#                     max_w = max(max_w, arr[j][0])
#                     max_h = max(max_h, arr[j][1])

#             # 명함 순회 끝나면 지갑의 크기 구하기
#             answer = min(answer, max_w * max_h)

#     return answer