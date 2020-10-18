
def print2d( A ):
    """ 2D 배열을 출력,
        입력: A, 2D 리스트
        츨력: None (없음)
    """
    NR = len(A)
    NC = len(A[0])

    for r in range(NR): # NR == 행 개수
        print('{} |'.format(r%10),end='')   # 행마다 행번호 표시, int와 str의 결합
        for c in range(NC):  # NC == 열 개수
            print(A[r][c]+'|',end=''),   # str와 str의 결합
        print()

    print('-'*(2*NC+3))   # str의 반복
    print('   ',end='')   # 세칸 띄어쓰기
    for c in range(NC):   # NR == 행 개수
        print('{} '.format(c%10),end='')
    print()              # 다음 출력을 위해



    '''
    for r in range(NR): # NR == 행 개수
        for c in range(NC):  # NC == 열 개수
            print(A[r][c],end=''),
        print()
    '''




    return None  # 돌려주는 값이 없으면 굳이 없어도 됨.

'''
A = [ ['X',' ','O'], ['O','X','O'] ]
print2d(A)
'''

def createA( NR, NC, s ):
    """ 문자열 s를 받아서 2D 배열로 바꾸기
        1행부터 채워나감
    """
    A = []
    for r in range(NR):
        newrow = []
        for c in range(NC):
            newrow += [ s[0] ] # add that char
            s = s[1:]   # get rid of that first char
        A += [newrow]
    return A
'''
A = [ ['X',' ','O'], ['O','X','O'] ]
newA = createA( 2, 3, 'X OOXO')
print(A == newA)

print2d(newA)

newB = createA( 2, 3, 'X OOX')
'''

def inarow_3east(ch, r_start, c_start, A):
    NR = len(A)                     # 행 개수
    NC = len(A[0])                  # 열 개수
    if r_start >= NR or c_start >= NC:
        return False
    elif c_start >= NC - 3+1:
        return False
    else:
        B = []
        for m in range(3):
            B += A[r_start][c_start+m]
        if B == [ch]*3:
            return True
        else:
            return False




def inarow_3south(ch, r_start, c_start, A):
    NR = len(A)
    NC = len(A[0])
    if r_start >= NR or c_start >= NC:
        return False
    elif r_start >= NR - 3+1:
        return False
    else:
        B = []
        for m in range(3):
            B += A[r_start+m][c_start]
        if B == [ch]*3:
            return True
        else:
            return False

def inarow_3se(ch, r_start, c_start, A):
    NR = len(A)
    NC = len(A[0])
    if r_start >= NR or c_start >= NC:
        return False
    elif c_start >= NC -3+1 or r_start >= NR -3+1:
        return False
    else:
        B = []
        for m in range(3):
            B += A[r_start+m][c_start+m]
        if B == [ch]*3:
            return True
        else:
            return False

def inarow_3ne(ch, r_start, c_start, A):
    NR = len(A)
    NC = len(A[0])
    if r_start >= NR or c_start >= NC:
        return False
    elif c_start >= NC -3+1 or r_start  <= 3-2:
        return False
    else:
        B = []
        for m in range(3):
            B += A[r_start-m][c_start+m]
        if B == [ch]*3:
            return True
        else:
            return False
'''
# tests of inarow_3east
A = createA( 3, 4, 'XXOXXXOOOOOO')
print2d(A)
print("inarow_3east('X',0,0,A): False ==", inarow_3east('X',0,0,A))
print("inarow_3east('O',2,1,A):  True ==", inarow_3east('O',2,1,A))
print("inarow_3east('X',2,1,A): False ==", inarow_3east('X',2,1,A))
print("inarow_3east('O',2,2,A): False ==", inarow_3east('O',2,2,A))

# tests of inarow_3south
A = createA( 4, 4, 'XXOXXXOXXOO OOOX')
# print2d(A)
print("inarow_3south('X',0,0,A):    True ==", inarow_3south('X',0,0,A))
print("inarow_3south('O',2,2,A):   False ==", inarow_3south('O',2,2,A))
print("inarow_3south('X',1,3,A):   False ==", inarow_3south('X',1,3,A))
print("inarow_3south('O',42,42,A): False ==", inarow_3south('O',42,42,A))

# tests of inarow_3se
A = createA( 4, 4, 'XOOXXXOXX XOOOOX')
# print2d(A)
print("inarow_3se('X',1,1,A):  True ==", inarow_3se('X',1,1,A))
print("inarow_3se('X',1,0,A): False ==", inarow_3se('X',1,0,A))
print("inarow_3se('O',0,1,A):  True ==", inarow_3se('O',0,1,A))
print("inarow_3se('X',2,2,A): False ==", inarow_3se('X',2,2,A))

# tests of inarow_3ne
A = createA( 4, 4, 'XOXXXXOXXOXOOOOX')
# print2d(A)
print("inarow_3ne('X',2,0,A):  True ==", inarow_3ne('X',2,0,A))
print("inarow_3ne('O',3,0,A):  True ==", inarow_3ne('O',3,0,A))
print("inarow_3ne('O',3,1,A): False ==", inarow_3ne('O',3,1,A))
print("inarow_3ne('X',3,3,A): False ==", inarow_3ne('X',3,3,A))
'''

def inarow_Neast(ch, r_start, c_start, A, N):
    NR = len(A)
    NC = len(A[0])
    if r_start >= NR or c_start >= NC:
        return False
    elif c_start >= NC - N+1:
        return False
    else:
        B = []
        for m in range(N):
            B += A[r_start][c_start+m]
        if B == [ch]*N:
            return True
        else:
            return False

def inarow_Nsouth(ch, r_start, c_start, A,N):
    NR = len(A)
    NC = len(A[0])
    if r_start >= NR or c_start >= NC:
        return False
    elif r_start >= NR - N+1:
        return False
    else:
        B = []
        for m in range(N):
            B += A[r_start+m][c_start]
        if B == [ch]*N:
            return True
        else:
            return False

def inarow_Nse(ch, r_start, c_start, A,N):
    NR = len(A)
    NC = len(A[0])
    if r_start >= NR or c_start >= NC:
        return False
    elif c_start >= NC -N+1 or r_start >= NR -N+1:
        return False
    else:
        B = []
        for m in range(N):
            B += A[r_start+m][c_start+m]
        if B == [ch]*N:
            return True
        else:
            return False

def inarow_Nne(ch, r_start, c_start, A, N):
    NR = len(A)
    NC = len(A[0])
    if r_start >= NR or c_start >= NC:
        return False
    elif c_start >= NC -N+1 or r_start  <= N-2:
        return False
    else:
        B = []
        for m in range(N):
            B += A[r_start-m][c_start+m]
        if B == [ch]*N:
            return True
        else:
            return False
'''
#tests of inarow_Neast
A = createA( 5, 5, 'XXOXXXOOOOOOXXXX XXXOOOOO')
print2d(A)
print("inarow_Neast('O',1,1,A,4):  True ==", inarow_Neast('O',1,1,A,4))
print("inarow_Neast('O',1,3,A,2):  True ==", inarow_Neast('O',1,3,A,2))
print("inarow_Neast('X',3,2,A,4): False ==", inarow_Neast('X',3,2,A,4))
print("inarow_Neast('O',4,0,A,5):  True ==", inarow_Neast('O',4,0,A,5))

#tests of inarow_Nsouth
A = createA( 5, 5, 'XXOXXXOOOOOOXXXXOXXXOOOXO')
print2d(A)
print ("inarow_Nsouth('X',0,0,A,5): False ==", inarow_Nsouth('X',0,0,A,5))
print ("inarow_Nsouth('O',1,1,A,4):  True ==", inarow_Nsouth('O',1,1,A,4))
print ("inarow_Nsouth('O',0,1,A,6): False ==", inarow_Nsouth('O',0,1,A,6))
print ("inarow_Nsouth('X',4,3,A,1):  True ==", inarow_Nsouth('X',4,3,A,1))

#tests of inarow_Nse
A = createA( 5, 5, 'XOO XXXOXOOOXXXXOXXXOOOXX' )
print2d(A)
print("inarow_Nse('X',1,1,A,4):  True ==", inarow_Nse('X',1,1,A,4))
print("inarow_Nse('O',0,1,A,3): False ==", inarow_Nse('O',0,1,A,3))
print("inarow_Nse('O',0,1,A,2):  True ==", inarow_Nse('O',0,1,A,2))
print("inarow_Nse('X',3,0,A,2): False ==", inarow_Nse('X',3,0,A,2))

#tests of inarow_Nne
A = createA( 5, 5, 'XOO XXXOXOOOXOXXXOXXXOOXX' )
print2d(A)
print("inarow_Nne('X',4,0,A,5):  True ==", inarow_Nne('X',4,0,A,5))
print("inarow_Nne('O',4,1,A,4):  True ==", inarow_Nne('O',4,1,A,4))
print("inarow_Nne('O',2,0,A,2): False ==", inarow_Nne('O',2,0,A,2))
print("inarow_Nne('X',0,3,A,1): False ==", inarow_Nne('X',0,3,A,1))
'''
