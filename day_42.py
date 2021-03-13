""" 프린터

    문제 설명: 
        일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다.
        그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다
        이런 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다.
        이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.
        
    입출력 예:
        priorities	        location	return
        [2, 1, 3, 2]	    2  	        1
        [1, 1, 9, 1, 1, 1]	0	        5
"""

def solution(p, l):
    count=0
    a=[(i,v) for i, v in enumerate(p)]
    while True:
        i,v = a.pop(0)
        if max(p) > v:
            a.append((i,v))
        else:   
            count+=1
            p.remove(v)
            if i == l:
                return count
