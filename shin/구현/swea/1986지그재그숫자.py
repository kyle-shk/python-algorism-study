T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    anw=0
    for i in range(1,n+1):
    
        if i % 2 ==0:
            anw-=i
        
        else:
            anw+=i
    
    print('#{} {}'.format(test_case,anw))