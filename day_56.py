""" 방문길이

    문제 설명: 
        게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.
        U: 위쪽으로 한 칸 가기
        D: 아래쪽으로 한 칸 가기
        R: 오른쪽으로 한 칸 가기
        L: 왼쪽으로 한 칸 가기
        캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다.
        좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.
        명령어가 매개변수 dirs로 주어질 때, 게임 캐릭터가 처음 걸어본 길의 길이를 구하여 return 하는 solution 함수를 완성해 주세요.
            
    입출력 예:
        dirs	        answer
        "ULURRDLLU"	    7
        "LULLLLLLU"	    7
"""

def solution(dirs):
    a=[]
    cx,cy,nx,ny=0,0,0,0
    for i in dirs:
        if i=="U" and ny<5:
            ny+=1
            a.append(((cx,cy),(nx,ny)))
            a.append(((nx,ny),(cx,cy)))
        if i=="D" and -5<ny:
            ny-=1
            a.append(((cx,cy),(nx,ny)))  
            a.append(((nx,ny),(cx,cy)))
        if i=="R" and nx<5:
            nx+=1
            a.append(((cx,cy),(nx,ny)))
            a.append(((nx,ny),(cx,cy)))
        if i=="L" and -5<nx:
            nx-=1
            a.append(((cx,cy),(nx,ny)))
            a.append(((nx,ny),(cx,cy)))
        cx,cy=nx,ny
    return len(set(a))//2