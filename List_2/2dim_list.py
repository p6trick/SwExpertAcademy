"""
2차원 list
구조
    - 1차원 list를 묶어놓은 list
    - 차원에 따라 index 선언
    - 세로의 길이(행의 갯수) , 가로의길이(열의 개수)를 필요로 한다.
    arr = [[0,1,2,3],[4,5,6,7]]

list 초기화
    - 직접 나열 : arr = [0,0,0,0,0]
    - 곱셈으로 반복 : arr = [0] * 5
    - list comprehension : [i for i in range(2,9) if i % 2 ==0]

    - brr = [[1,2,3],[1,2,3],[1,2,3]]
    - brr = [[1,2,3]] * 3
    - brr = [[1,2,3] for i in range(3)]

입력 받기
    - 3 4
    - 0 1 0 0
    - 0 0 0 0
    - 0 0 1 0   첫째줄 n행 m열 // 둘째줄 행열 데이터가 주어질 경우
"""
n,m = map(int, input().split())
mylist = [0 for _ in range(n)]
#or
mylist = [0] * n
#행크기 만큼의 빈 리스트를 생성

for i in range(n):
    mylist[i] = list(map(int, input().split()))
#입력받는 수를 띄어쓰기 기준으로 mylist에 저장
#-------------------------------------------------------------#
# append 이용
n,m = map(int, input().split())
mylist=[]
for i in range(n):
    mylist.append(list(map(int, input().split())))
#--------------------------------------------------------------#
#list comprehension 사용
n,m = map(int, input().split())
mylist = [list(map(int, input().split())) for _ in range(n)]
#--------------------------------------------------------------#
"""
2차원 list에서 원하는 데이터 위치 찾기
"""
n,m = map(int,input().split())
new_list=[]
mylist =[0 for _ in range(n)]
for i in range(n):
    mylist[i] = list(map(int,input().split()))
    for j in range(m):
        if mylist[i][j] == 1:
            new_list.append([i,j])
# 값이 1인 행렬 값을 따로 저장하는 new_list
#--------------------------------------------------------------#
n,m = map(int,input().split())
mylist = [list(map(int,input().split())) for _ in range(n)]
new_list = [(i,j) for i in range(n) for j in range(m) if mylist[i][j] == 1]
#--------------------------------------------------------------#
"""
list 순회
n x m list의 n*m개의 모든 원소를 빠짐없이 조사하는 방법

- 행 우선 순회
    - list의 행을 우선으로 조사하는 방법
- 열 우선 순회
    - list의 열부터 2중 반복문으로 구현이 가능
- 지그재그 순회
    - list의 행을 좌우로 조사하는 방법
    - -> 다음행  <-
    - 순회 방향에 따라 index값이 커지거나 작아지도록

- delta를 이용한 탐색
    - list의 한 좌표에서 네 방향의 인접 list요소를 탐색할 때 사용
    - delta = 한 좌표에서 네 방향의 좌표와 x,y의 차이를 저장한 list
    - 가장자리 원소들은 네 방향의 원소가 존재하지 않을수있으므로 Index를
      check하거나 index의 범위를 제한해야함.
"""
#--------------------------------------------------------------#
# 열 우선 순회
for j in range(len(arr[0])):
    for i in range(len(arr)):
        arr[i][j]
#--------------------------------------------------------------#
# 지그재그 순회
# n : len(arr)
# m : len(arr[0])
for i in range(len(arr)):
    for j in range(len(arr[0])):
        arr[i][j+(m-1-2*j)*(i%2)]
        #순회방향에 따라 index값이 커지거나 작아지도록
#--------------------------------------------------------------#
# delta를 이용한 네방향 탐색
#arr[0 ~ n-1][0 ~ n-1]
dx = [0,0,-1,-1] # 상하좌우
dy = [-1,-1,0,0]

for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            print(arr[testX][testY])
#--------------------------------------------------------------#
"""
전치 행렬
- 행과 열의 값이 반대인 행렬을 의미
- 행과 열을 바꾸기
"""
#--------------------------------------------------------------#
# 전치행렬
arr = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(3):
    for j in range(3):
        if i<j:
            arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
#--------------------------------------------------------------#
"""
zip()
- 동일한 개수로 이루어진 자료형들을 묶어주는 역할의 함수
- tuple로 return
- 개수가 동일하지 않으면 작은 쪽의 개수에 맞춘다.
"""
#--------------------------------------------------------------#
alpha = ['a','b','c']
index = [1,2,3]

alpha_index = list(zip(alpha,index))
print(alpha_index)
#>>> [('a',1),('b',2),('c',3)]
#--------------------------------------------------------------#
# list를 행으로 쪼개서 같은 열의 데이터끼리 묶을 수 있다.
arr = [[1,2,3],[4,5,6],[7,8,9]]
print(list(zip(*arr)))
# >>> [(1,4,7),(2,5,8),(3,6,9)]
"""
위의 결과는 전치행렬과 같다.
"""







