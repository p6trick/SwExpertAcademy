# N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력

T = int(input()) # 테스트 케이스 수 입력.

result=[]
for i in range(T): # T번 반복
    N,M = map(int,input().split()) # N과 M을 띄어쓰기 기준으로 입력받기

    num_list = list(map(int,input().split())) # 띄어쓰기 기준으로 숫자를 입력받고 리스트로 저장

    min_sum=float('inf')
    for i in range(N-M+1): #슬라이딩 수
        tmp_sum=0
        for j in range(i,i+M):
            tmp_sum+=num_list[j]
        if tmp_sum < min_sum:
            min_sum = tmp_sum
    
    max_sum=0
    for i in range(N-M+1): #슬라이딩 수
        tmp_sum=0
        for j in range(i,i+M):
            tmp_sum+=num_list[j]
        if tmp_sum > max_sum:
            max_sum = tmp_sum
    
    
    sub_result = max_sum - min_sum
    result.append(sub_result)

for i in range(T):
    print(f"#{i+1} {result[i]}")

