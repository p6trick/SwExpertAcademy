"""
부분 집합

합 :
유한개의 정수로 이루어진 집합이 있을 때, 이 집합의 부분 집합 중에서
그 집합의 원소를 모두 더한 값이 0이 되는 경우가 있는지
{-7,-3,-2,5,8}
-3,-2,5 부분집합이고 합은 0

완전검색
모든 부분집합을 구한 후
각 부분 집합의 합을 계산

부분집합의 수
총 개수?
2^n : 공집합을 포함


"""
#------------------------------------------------------#
# 부분집합 생성을 위한 bit list 생성
# list 각 원소를 포함할지 말지를 결정하는 list
# 4개 원소를 가진 list가 있을 때 모든 경우의 수를 출력
# 0000 0001 ~ 1110 1111 까지
# 포함할지 말지
bit=[0,0,0,0]

for i in range(2):
    bit[0]=i
    for j in range(2):
        bit[1]=j
        for k in range(2):
            bit[2]=k
            for l in range(2):
                bit[3]=l
                print(bit)
#------------------------------------------------------#
"""
비트 연산자
2진수의 연산을 수행하는 연산자
& : 모두 1일때만 1
| : 하나라도 1이면 1
<< : 비트 열을 왼쪽 혹은 오른쪽으로 이동시킴
>>
"""
#------------------------------------------------------#
# 좀 더 효율적인 부분집합 생성
arr = [1,2,3,4]
n = len(arr) #n : 원소의 개수

for i in range(1<<n): # 1<<n 부분 집합의 개수 : 2^n
    for j in range(n): # 원소의 수 만큼 비트를 비교함
        if i&(1<<j): # i의 j번째 비트가 1이면 j번째 원소 출력 // for j부터 bit matrix를 생성하는 문장
            print(arr[j],end=',')
    print()


