T = int(input()) #노선 수.
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
result=[]
for test_case in range(1, T + 1):
    K,N,M = map(int,input().split()) #k=한번 충전으로 갈수있는 정류장, N=목적지, M = 충전기 설치된 정류장 수
    charge = list(map(int,input().split()))
    
    terminal = 0 #버스가 이동한 터미널 초기화/
    cnt=0 # 충전한 횟수/

    while terminal <=N: # 현재 정류장이 목적지보다 작으면 계속 반복
        tmp=0 # 크기 비교를 위한 변수
        if terminal+K >= N: #현재 정류장에서 한번에 갈 수 있는 정류장의 개수를 더해서 목적지보다 멀리 갈 수 있다면 반복문 탈출
            break

        for i in range(terminal,terminal+K + 1): # 현재 터미널~현재터미널+한번에 갈 수 있는 터미널
            if i in charge: # 갈수있는 터미널 중에 충전소가 있으면
                if tmp<i: # 그 충전소 터미널이 현재 정류장보다 크면
                    tmp=i # 저장
        if terminal==tmp: # 만약에 갈 수 있는 충전소 정류장이 저번 loop와 같다면
            cnt=0 # 현재 loop에 갈 수 있는 정류장이 없다는 뜻으로 cnt 초기화
            break #반복문 탈출
        else: # loop에 갈 수 있는 새로운 충전소가 있다면
            cnt+=1 #충전한 횟수 증가
            terminal=tmp #ternimal 이동
            

    result.append(cnt) # 하나의 루트가 끝나면 cnt 를 결과 리스트에 추가
    
for i in range(T): # 모든 루트를 다 돌고 각 루트마다 충전횟수를 출력
    print(f"#{i+1} {result[i]}")



