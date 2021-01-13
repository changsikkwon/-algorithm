""" 약수의 합

    문제 설명: 
        정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
    
    제한사항:
        n은 0 이상 3000이하인 정수입니다.

    입출력 예:
        n	return
        12	28
        5	6
"""

def solution(n):
    return sum([i for i in range(1, n+1) if n%i==0])