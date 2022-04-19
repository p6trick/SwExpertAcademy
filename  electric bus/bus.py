# T = int(input()) #노선 수.
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# result=[]
# for test_case in range(1, T + 1):
#     K,N,M = map(int,input().split()) #k=한번 충전으로 갈수있는 정류장, N=목적지, M = 충전기 설치된 정류장 수
#     charge = list(map(int,input().split()))
    
#     terminal = 0
#     cnt=0
#     while terminal <= N:
#         fringe={}
#         for i in range(1,K+1):
#             fringe[terminal+i]=0

#         tmp_list=[]

#         for i in fringe:
#             if i in charge:
#                 fringe[i]=1
#             else:
#                 fringe[i]=0

#         for i in (terminal+K,terminal-K):
#             tmp = fringe.pop(i)
#             if tmp == 1:
#                 break
#         terminal=tmp_list.rfind(1)
#         cnt+=1
#     result.append(cnt)

# for i in range(T):
#     print(f"#{i+1} {result[i]}")

f={1:0,2:1,3:0}
print(f.pop(3))

