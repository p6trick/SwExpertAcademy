T = int(input()) #케이스 숫자를 입력받는다.

result=[]
for test_case in range(1, T + 1):
    num = int(input()) # 카드의 장수를 입력받는다
    #띄어쓰기 없이 입력받은 숫자를 list로 만들기
    cards=[]
    for i in input():
        cards.append(int(i))
   
    # 0~9의 숫자의 장수를 저장할 리스트 생성
    num_cards = [0]*10

    for i in cards:
        num_cards[i]+=1 #각 index(카드 숫자)의 장수를 저장

    # max_num=0 #카드 장수 중에서 가장 큰 값을 저장
    # for i in num_cards:
    #     if max_num < i:
    #         max_num = i
    max_num = max(num_cards)
    
    max_val_list=[]
    seted_card = list(set(cards)) #받은 카드의 중복을 없애고
    for i in seted_card:
        if num_cards[i]==max_num: #가장 많은 장수의 카드만 리스트에 저장
            max_val_list.append(i)
    
    max_val = max(max_val_list) #그 중에서 큰 값만 저장

    result.append([max_val,max_num])
   

for i in range(T):
    a,b = result[i]
    print(f"#{i+1} {a} {b}")



