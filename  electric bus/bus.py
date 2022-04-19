T = int(input()) #노선 수.
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
result=[]
for test_case in range(1, T + 1):
    K,N,M = map(int,input().split()) #k=한번 충전으로 갈수있는 정류장, N=목적지, M = 충전기 설치된 정류장 수
    charge = list(map(int,input().split()))
    
    terminal = 0
    cnt=0

    while terminal <=N:
        tmp=0
        if terminal+K >= N:
            break

        for i in range(terminal,terminal+K + 1):
            if i in charge:
                if tmp<i:
                    tmp=i
        if terminal==tmp:
            cnt=0
            break
        else:
            cnt+=1
            terminal=tmp
            

    result.append(cnt)
    
for i in range(T):
    print(f"#{i+1} {result[i]}")



