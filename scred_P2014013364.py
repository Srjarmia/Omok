def Limit2_Neast(ch, r_start, c_start, A):
    NC = len(A[0])
    if (c_start+3) >= NC:
        return False
    else:
        B = [A[r_start][c_start+(m+1)] for m in range(2)]
        if B == [ch, ' ']:
            B += A[r_start][c_start+3]
            if B == [ch, ' ', ch]:
                return False
            elif ((c_start-1) >= 0) & (A[r_start][c_start-1] == ' '):
                if ((c_start-2) >= 0) & (A[r_start][c_start-2] == ch):
                    return False
                return True
        B += A[r_start][c_start+3]
        if B == [' ', ch, ' ']:
            if ((c_start-1) >= 0) & (A[r_start][c_start-1] == ' '):
                if ((c_start-2) >= 0) & (A[r_start][c_start-2] == ch):
                    return False
                return True
    return False


def Limit2_Nwest(ch, r_start, c_start, A):
    NC = len(A[0])
    if (c_start-3) < 0:
        return False
    else:
        B = [A[r_start][c_start-(m+1)] for m in range(2)]
        if B == [ch, ' ']:
            B += A[r_start][c_start-3]
            if B == [ch, ' ', ch]:
                return False
            elif (c_start+1) < NC:
                if A[r_start][c_start+1] == ' ':
                    if (c_start+2) < NC:
                        if A[r_start][c_start+2] == ch:
                            return False
                    return True
        B += A[r_start][c_start-3]
        if B == [' ', ch, ' ']:
            if (c_start+1) < NC:
                if A[r_start][c_start+1] == ' ':
                    if (c_start+2) < NC:
                        if A[r_start][c_start+2] == ch:
                            return False
                    return True
    return False


def Limit2_Nsouth(ch, r_start, c_start, A):
    NR = len(A)
    if (r_start+3) >= NR:
        return False
    else:
        B = [A[r_start+(m+1)][c_start] for m in range(2)]
        if B == [ch, ' ']:
            B += A[r_start+3][c_start]
            if B == [ch, ' ', ch]:
                return False
            elif ((r_start-1) >= 0) & (A[r_start-1][c_start] == ' '):
                if ((r_start-2) >= 0) & (A[r_start-2][c_start] == ch):
                    return False
                return True
        B += A[r_start+3][c_start]
        if B == [' ', ch, ' ']:
            if ((r_start-1) >= 0) & (A[r_start-1][c_start] == ' '):
                if ((r_start-2) >= 0) & (A[r_start-2][c_start] == ch):
                    return False
                return True
    return False


def Limit2_Nnorth(ch, r_start, c_start, A):
    NR = len(A)
    if (r_start-3) < 0:
        return False
    else:
        B = [A[r_start-(m+1)][c_start] for m in range(2)]
        if B == [ch, ' ']:
            B += A[r_start-3][c_start]
            if B == [ch, ' ', ch]:
                return False
            elif (r_start+1) < NR:
                if A[r_start+1][c_start] == ' ':
                    if (r_start+2)<NR:
                        if A[r_start+2][c_start] == ch:
                            return False
                    return True
        B += A[r_start-3][c_start]
        if B == [' ', ch, ' ']:
            if (r_start+1) < NR:
                if A[r_start+1][c_start] == ' ':
                    if (r_start+2) < NR:
                        if A[r_start+2][c_start] == ch:
                            return False
                    return True
    return False


def Limit2_Nse(ch, r_start, c_start, A):
    NR = len(A)
    NC = len(A[0])
    if ((r_start+3) >= NR) | ((c_start+3) >= NC):
        return False
    else:
        B = [A[r_start+(m+1)][c_start+(m+1)] for m in range(2)]
        if B == [ch, ' ']:
            B += A[r_start+3][c_start+3]
            if B == [ch, ' ', ch]:
                return False
            elif (((r_start-1) >= 0) & ((c_start-1) >= 0)) & (A[r_start-1][c_start-1] == ' '):
                if (((r_start-2) >= 0) & ((c_start-2) >= 0)) & (A[r_start-2][c_start-2] == ch):
                    return False
                return True
        B += A[r_start+3][c_start+3]
        if B == [' ', ch, ' ']:
            if (((r_start-1) >= 0) & ((c_start-1) >= 0)) & (A[r_start-1][c_start-1] == ' '):
                if (((r_start-2) >= 0) & ((c_start-2) >= 0)) & (A[r_start-2][c_start-2] == ch):
                    return False
                return True
    return False


def Limit2_Nne(ch, r_start, c_start, A):
    NR = len(A)
    NC = len(A[0])
    if ((r_start-3) < 0) | ((c_start+3) >= NC):
        return False
    else:
        B = [A[r_start-(m+1)][c_start+(m+1)] for m in range(2)]
        if B == [ch, ' ']:
            B += A[r_start-3][c_start+3]
            if B == [ch, ' ', ch]:
                return False
            elif ((r_start+1) < NR) & ((c_start-1) >= 0):
                if A[r_start+1][c_start-1] == ' ':
                    if ((r_start+2) < NR) & ((c_start-2) >= 0):
                        if A[r_start+2][c_start-2] == ch:
                            return False
                    return True
        B += A[r_start-3][c_start+3]
        if B == [' ', ch, ' ']:
            if ((r_start+1) < NR) & ((c_start-1) >= 0):
                if A[r_start+1][c_start-1] == ' ':
                    if ((r_start+2)<NR)&((c_start-2) >= 0):
                        if A[r_start+2][c_start-2] == ch:
                            return False
                    return True
    return False


def Limit2_Nnw(ch, r_start, c_start, A):
    NR = len(A)
    NC = len(A[0])
    if ((r_start-3)<0) | ((c_start-3)<0):
        return False
    else:
        B = [A[r_start-(m+1)][c_start-(m+1)] for m in range(2)]
        if B == [ch, ' ']:
            B += A[r_start-3][c_start-3]
            if B == [ch, ' ', ch]:
                return False
            elif ((r_start+1) < NR) & ((c_start+1) < NC):
                if A[r_start+1][c_start+1] == ' ':
                    if ((r_start+2) < NR) & ((c_start+2) < NC):
                        if A[r_start+2][c_start+2] == ch:
                            return False
                    return True
        B += A[r_start-3][c_start-3]
        if B == [' ', ch, ' ']:
            if ((r_start+1) < NR) & ((c_start+1) < NC):
                if A[r_start+1][c_start+1] == ' ':
                    if ((r_start+2) < NR) & ((c_start+2) < NC):
                        if A[r_start+2][c_start+2] == ch:
                            return False
                    return True
    return False


def Limit2_Nsw(ch, r_start, c_start, A):
    NR = len(A)
    NC = len(A[0])
    if ((r_start+3) >= NR) | ((c_start-3) < 0):
        return False
    else:
        B = [A[r_start+(m+1)][c_start-(m+1)] for m in range(2)]
        if B == [ch, ' ']:
            B += A[r_start+3][c_start-3]
            if B == [ch, ' ', ch]:
                return False
            elif ((r_start-1) >= 0) & ((c_start+1) < NC):
                if A[r_start-1][c_start+1] == ' ':
                    if ((r_start-2) >= 0) & ((c_start+2) < NC):
                        if A[r_start-2][c_start+2] == ch:
                            return False
                    return True
        B += A[r_start+3][c_start-3]
        if B == [' ', ch, ' ']:
            if ((r_start-1) >= 0) & ((c_start+1) < NC):
                if A[r_start-1][c_start+1] == ' ':
                    if ((r_start-2) >= 0) & ((c_start+2) < NC):
                        if A[r_start-2][c_start+2] == ch:
                            return False
                    return True
    return False


def Limit2(ch, r_start, c_start, A):
    P = Limit2_Neast(ch, r_start, c_start, A)\
      + Limit2_Nwest(ch, r_start, c_start, A)\
      + Limit2_Nsouth(ch, r_start, c_start, A)\
      + Limit2_Nnorth(ch, r_start, c_start, A)\
      + Limit2_Nse(ch, r_start, c_start, A)\
      + Limit2_Nne(ch, r_start, c_start, A)\
      + Limit2_Nnw(ch, r_start, c_start, A)\
      + Limit2_Nsw(ch, r_start, c_start, A)
    if P >= 2:
        return True
    else:
        return False


def Score2(ch, r_start, c_start, A):
    P = Limit2_Neast(ch, r_start, c_start, A)\
      + Limit2_Nwest(ch, r_start, c_start, A)\
      + Limit2_Nsouth(ch, r_start, c_start, A)\
      + Limit2_Nnorth(ch, r_start, c_start, A)\
      + Limit2_Nse(ch, r_start, c_start, A)\
      + Limit2_Nne(ch, r_start, c_start, A)\
      + Limit2_Nnw(ch, r_start, c_start, A)\
      + Limit2_Nsw(ch, r_start, c_start, A)
    if P == 1:
        return True
    else:
        return False


def Limit3_Neast(ch, r_start, c_start, A):
    NC = len(A[0])
    if (c_start+4) >= NC:
        return False
    else:
        B = [A[r_start][c_start+(m+1)] for m in range(3)]
        if B == [ch, ch, ' ']:
            B += A[r_start][c_start+4]
            if B == [ch, ch, ' ', ch]:
                return False
            elif ((c_start-1) >= 0) & (A[r_start][c_start-1] == ' '):
                if ((c_start-2) >= 0) & (A[r_start][c_start-2] == ch):
                    return False
                return True
        B += A[r_start][c_start+4]
        if (B == [ch, ' ', ch, ' ']) | (B == [' ', ch, ch, ' ']):
            if ((c_start-1) >= 0) & (A[r_start][c_start-1] == ' '):
                if ((c_start-2) >= 0) & (A[r_start][c_start-2] == ch):
                    return False
                return True
    return False


def Limit3_Nwest(ch, r_start, c_start, A):
    NC = len(A[0])
    if (c_start-4) < 0:
        return False
    else:
        B = [A[r_start][c_start-(m+1)] for m in range(3)]
        if B == [ch, ch, ' ']:
            B += A[r_start][c_start-4]
            if B == [ch, ch, ' ', ch]:
                return False
            elif (c_start+1) < NC:
                if A[r_start][c_start+1] == ' ':
                    if (c_start+2) < NC:
                        if A[r_start][c_start+2] == ch:
                            return False
                    return True
        B += A[r_start][c_start-4]
        if (B == [ch, ' ', ch, ' ']) | (B == [' ', ch, ch, ' ']):
            if (c_start+1) < NC:
                if A[r_start][c_start+1] == ' ':
                    if (c_start+2) < NC:
                        if A[r_start][c_start+2] == ch:
                            return False
                    return True
    return False


def Limit3_Nsouth(ch, r_start, c_start, A):
    NR = len(A)
    if (r_start+4) >= NR:
        return False
    else:
        B=[A[r_start+(m+1)][c_start] for m in range(3)]
        if B == [ch, ch, ' ']:
            B += A[r_start+4][c_start]
            if B == [ch, ch, ' ', ch]:
                return False
            elif ((r_start-1) >= 0) & (A[r_start-1][c_start] == ' '):
                if ((r_start-2) >= 0) & (A[r_start-2][c_start] == ch):
                    return False
                return True
        B += A[r_start+4][c_start]
        if (B == [ch, ' ', ch, ' ']) | (B == [' ', ch, ch, ' ']):
            if ((r_start-1) >= 0) & (A[r_start-1][c_start] == ' '):
                if ((r_start-2) >= 0) & (A[r_start-2][c_start] == ch):
                    return False
                return True
    return False


def Limit3_Nnorth(ch, r_start, c_start, A):
    NR = len(A)
    if (r_start-4) < 0:
        return False
    else:
        B = [A[r_start-(m+1)][c_start] for m in range(3)]
        if B == [ch, ch, ' ']:
            B += A[r_start-4][c_start]
            if B == [ch, ch, ' ', ch]:
                return False
            elif (r_start+1) < NR:
                if A[r_start+1][c_start] == ' ':
                    if (r_start+2)<NR:
                        if A[r_start+2][c_start] == ch:
                            return False
                    return True
        B += A[r_start-4][c_start]
        if (B == [ch, ' ', ch, ' ']) | (B == [' ', ch, ch, ' ']):
            if (r_start+1) < NR:
                if A[r_start+1][c_start] == ' ':
                    if (r_start+2) < NR:
                        if A[r_start+2][c_start] == ch:
                            return False
                    return True
    return False


def Limit3_Nse(ch, r_start, c_start, A):
    NR = len(A)
    NC = len(A[0])
    if ((r_start+4) >= NR) | ((c_start+4) >= NC):
        return False
    else:
        B = [A[r_start+(m+1)][c_start+(m+1)] for m in range(3)]
        if B == [ch, ch, ' ']:
            B += A[r_start+4][c_start+4]
            if B == [ch, ch, ' ', ch]:
                return False
            elif (((r_start-1) >= 0) & ((c_start-1) >= 0)) & (A[r_start-1][c_start-1] == ' '):
                if (((r_start-2) >= 0) & ((c_start-2) >= 0)) & (A[r_start-2][c_start-2] == ch):
                    return False
                return True
        B += A[r_start+4][c_start+4]
        if (B == [ch, ' ', ch, ' ']) | (B == [' ', ch, ch, ' ']):
            if (((r_start-1) >= 0) & ((c_start-1) >= 0)) & (A[r_start-1][c_start-1] == ' '):
                if (((r_start-2) >= 0) & ((c_start-2) >= 0)) & (A[r_start-2][c_start-2] == ch):
                    return False
                return True
    return False


def Limit3_Nne(ch, r_start, c_start, A):
    NR = len(A)
    NC = len(A[0])
    if ((r_start-4) < 0) | ((c_start+4) >= NC):
        return False
    else:
        B = [A[r_start-(m+1)][c_start+(m+1)] for m in range(3)]
        if B == [ch, ch, ' ']:
            B += A[r_start-4][c_start+4]
            if B == [ch, ch, ' ', ch]:
                return False
            elif ((r_start+1) < NR) & ((c_start-1) >= 0):
                if A[r_start+1][c_start-1] == ' ':
                    if ((r_start+2) < NR) & ((c_start-2) >= 0):
                        if A[r_start+2][c_start-2] == ch:
                            return False
                    return True
        B += A[r_start-4][c_start+4]
        if (B == [ch, ' ', ch, ' ']) | (B == [' ', ch, ch, ' ']):
            if ((r_start+1) < NR) & ((c_start-1) >= 0):
                if A[r_start+1][c_start-1] == ' ':
                    if ((r_start+2)<NR)&((c_start-2) >= 0):
                        if A[r_start+2][c_start-2] == ch:
                            return False
                    return True
    return False


def Limit3_Nnw(ch, r_start, c_start, A):
    NR = len(A)
    NC = len(A[0])
    if ((r_start-4)<0) | ((c_start-4)<0):
        return False
    else:
        B = [A[r_start-(m+1)][c_start-(m+1)] for m in range(3)]
        if B == [ch, ch, ' ']:
            B += A[r_start-4][c_start-4]
            if B == [ch, ch, ' ', ch]:
                return False
            elif ((r_start+1) < NR) & ((c_start+1) < NC):
                if A[r_start+1][c_start+1] == ' ':
                    if ((r_start+2) < NR) & ((c_start+2) < NC):
                        if A[r_start+2][c_start+2] == ch:
                            return False
                    return True
        B += A[r_start-4][c_start-4]
        if (B == [ch, ' ', ch, ' ']) | (B == [' ', ch, ch, ' ']):
            if ((r_start+1) < NR) & ((c_start+1) < NC):
                if A[r_start+1][c_start+1] == ' ':
                    if ((r_start+2) < NR) & ((c_start+2) < NC):
                        if A[r_start+2][c_start+2] == ch:
                            return False
                    return True
    return False


def Limit3_Nsw(ch, r_start, c_start, A):
    NR = len(A)
    NC = len(A[0])
    if ((r_start+4) >= NR) | ((c_start-4) < 0):
        return False
    else:
        B = [A[r_start+(m+1)][c_start-(m+1)] for m in range(3)]
        if B == [ch, ch, ' ']:
            B += A[r_start+4][c_start-4]
            if B == [ch, ch, ' ', ch]:
                return False
            elif ((r_start-1) >= 0) & ((c_start+1) < NC):
                if A[r_start-1][c_start+1] == ' ':
                    if ((r_start-2) >= 0) & ((c_start+2) < NC):
                        if A[r_start-2][c_start+2] == ch:
                            return False
                    return True
        B += A[r_start+4][c_start-4]
        if (B == [ch, ' ', ch, ' ']) | (B == [' ', ch, ch, ' ']):
            if ((r_start-1) >= 0) & ((c_start+1) < NC):
                if A[r_start-1][c_start+1] == ' ':
                    if ((r_start-2) >= 0) & ((c_start+2) < NC):
                        if A[r_start-2][c_start+2] == ch:
                            return False
                    return True
    return False


def Limit3_Nmew(ch, r_start, c_start, A):
    NC = len(A[0])
    if ((c_start+2) >= NC) | ((c_start-2) < 0):
        return False
    else:
        B = [A[r_start][(c_start-2)+m] for m in range(5)]
        if (B == [' ', ch, ' ', ch, ' ']) | (B == [' ', ch, ' ', ' ', ch]) | (B == [ch, ' ', ' ', ch, ' ']):
            if ((c_start+3) < NC) & ((c_start-3) >= 0):
                if (A[r_start][c_start-3] == ch) | (A[r_start][c_start+3] == ch):
                    return False
                elif (A[r_start][c_start-3] != ' ') & (A[r_start][c_start+3] != ' '):
                    return False
                elif (A[r_start][c_start-2] == ch) & (A[r_start][c_start-3] != ' '):
                    return False
                elif (A[r_start][c_start+2] == ch) & (A[r_start][c_start+3] != ' '):
                    return False
            elif ((c_start+3) >= NC) & ((c_start-3) >= 0):
                if A[r_start][c_start-3] != ' ':
                    return False
            elif ((c_start-3) < 0) & ((c_start+3) < NC):
                if A[r_start][c_start+3] != ' ':
                    return False
            return True
    return False


def Limit3_Nmsn(ch, r_start, c_start, A):
    NR = len(A)
    NC = len(A[0])
    if ((r_start+2) >= NR) | ((r_start-2) < 0):
        return False
    else:
        B = [A[(r_start-2)+m][c_start] for m in range(5)]
        if (B == [' ', ch, ' ', ch, ' ']) | (B == [' ', ch, ' ', ' ', ch]) | (B == [ch, ' ', ' ', ch, ' ']):
            if ((r_start+3) < NC) & ((r_start-3) >= 0):
                if (A[r_start-3][c_start] == ch) | (A[r_start+3][c_start] == ch):
                    return False
                elif (A[r_start-3][c_start] != ' ') & (A[r_start+3][c_start] != ' '):
                    return False
                elif (A[r_start-2][c_start] == ch) & (A[r_start-3][c_start] != ' '):
                    return False
                elif (A[r_start+2][c_start] == ch) & (A[r_start+3][c_start] != ' '):
                    return False
            elif ((r_start+3) >= NC) & ((r_start-3) >= 0):
                if A[r_start-3][c_start] != ' ':
                    return False
            elif ((r_start-3) < 0) & ((r_start+3) < NC):
                if A[r_start+3][c_start] != ' ':
                    return False
            return True
    return False


def Limit3_Nmcross1(ch, r_start, c_start, A):
    NR = len(A)
    NC = len(A[0])
    if ((r_start+2) >= NR) | ((r_start-2) < 0) | ((c_start+2) >= NC) | ((c_start-2) < 0):
        return False
    else:
        B = [A[(r_start-2)+m][(c_start-2)+m] for m in range(5)]
        if (B == [' ', ch, ' ', ch, ' ']) | (B == [' ', ch, ' ', ' ', ch]) | (B == [ch, ' ', ' ', ch, ' ']):
            if ((r_start+3) < NR) & ((r_start-3) >= 0) & ((c_start+3) < NC) & ((c_start-3) >= 0):
                if (A[r_start-3][c_start-3] == ch) | (A[r_start+3][c_start+3] == ch):
                    return False
                elif (A[r_start-3][c_start-3] != ' ') & (A[r_start+3][c_start+3] != ' '):
                    return False
                elif (A[r_start-2][c_start-2] == ch) & (A[r_start-3][c_start-3] != ' '):
                    return False
                elif (A[r_start+2][c_start+2] == ch) & (A[r_start+3][c_start+3] != ' '):
                    return False
            elif (((r_start+3) >= NR) & ((r_start-3) >= 0)) | (((c_start+3) >= NC) & ((c_start-3) >= 0)):
                if A[r_start-3][c_start-3] != ' ':
                    return False
            elif (((r_start-3)<0) & ((r_start+3) < NR)) | (((c_start-3) < 0) & ((c_start+3) < NC)):
                if A[r_start+3][c_start+3] != ' ':
                    return False
            return True
    return False


def Limit3_Nmcross2(ch, r_start, c_start, A):
    NR = len(A)
    NC = len(A[0])
    if ((r_start+2) >= NR) | ((r_start-2) < 0) | ((c_start+2) >= NC) | ((c_start-2) < 0):
        return False
    else:
        B = [A[(r_start+2)-m][(c_start-2)+m] for m in range(5)]
        if (B == [' ', ch, ' ', ch, ' ']) | (B == [' ', ch, ' ', ' ', ch]) | (B == [ch, ' ', ' ', ch, ' ']):
            if ((r_start+3) < NR) & ((r_start-3) >= 0) & ((c_start+3) < NC) & ((c_start-3) >= 0):
                if (A[r_start+3][c_start-3] == ch) | (A[r_start-3][c_start+3] == ch):
                    return False
                elif (A[r_start+3][c_start-3] != ' ') & (A[r_start-3][c_start+3] != ' '):
                    return False
                elif (A[r_start+2][c_start-2] == ch) & (A[r_start+3][c_start-3] != ' '):
                    return False
                elif (A[r_start-2][c_start+2] == ch) & (A[r_start-3][c_start+3] != ' '):
                    return False
            elif (((r_start+3) >= NR) & ((r_start-3) >= 0)) | (((c_start-3) < 0)&((c_start+3) < NC)):
                if A[r_start-3][c_start+3] != ' ':
                    return False
            elif (((r_start-3) < 0) & ((r_start+3) < NR)) | (((c_start+3) >= NC) & ((c_start-3) >= 0)):
                if A[r_start+3][c_start-3] != ' ':
                    return False
            return True
    return False


def Limit3(ch, r_start, c_start, A):
    P = Limit3_Neast(ch, r_start, c_start, A)\
      + Limit3_Nwest(ch, r_start, c_start, A)\
      + Limit3_Nsouth(ch, r_start, c_start, A)\
      + Limit3_Nnorth(ch, r_start, c_start, A)\
      + Limit3_Nse(ch, r_start, c_start, A)\
      + Limit3_Nne(ch, r_start, c_start, A)\
      + Limit3_Nnw(ch, r_start, c_start, A)\
      + Limit3_Nsw(ch, r_start, c_start, A)\
      + Limit3_Nmew(ch, r_start, c_start, A)\
      + Limit3_Nmsn(ch, r_start, c_start, A)\
      + Limit3_Nmcross1(ch, r_start, c_start, A)\
      + Limit3_Nmcross2(ch, r_start, c_start, A)
    if P >= 2:
        return True
    else:
        return False


def Score3(ch, r_start, c_start, A):
    P = Limit3_Neast(ch, r_start, c_start, A)\
      + Limit3_Nwest(ch, r_start, c_start, A)\
      + Limit3_Nsouth(ch, r_start, c_start, A)\
      + Limit3_Nnorth(ch, r_start, c_start, A)\
      + Limit3_Nse(ch, r_start, c_start, A)\
      + Limit3_Nne(ch, r_start, c_start, A)\
      + Limit3_Nnw(ch, r_start, c_start, A)\
      + Limit3_Nsw(ch, r_start, c_start, A)\
      + Limit3_Nmew(ch, r_start, c_start, A)\
      + Limit3_Nmsn(ch, r_start, c_start, A)\
      + Limit3_Nmcross1(ch, r_start, c_start, A)\
      + Limit3_Nmcross2(ch, r_start, c_start, A)
    if P == 1:
        return True
    else:
        return False


def Limit4_Neast(ch, r_start, c_start, A):
    NC = len(A[0])
    if (c_start+5) >= NC:
        return False
    else:
        B = [A[r_start][c_start+(m+1)] for m in range(4)]
        if B == [ch, ch, ch, ' ']:
            B += A[r_start][c_start+5]
            if B == [ch, ch, ch, ' ', ch]:
                return False
            elif ((c_start-1) >= 0) & (A[r_start][c_start-1] == ' '):
                if ((c_start-2) >= 0) & (A[r_start][c_start-2] == ch):
                    return False
                return True
        B += A[r_start][c_start+5]
        if (B == [ch, ch, ' ', ch, ' ']) | (B == [ch, ' ', ch, ch, ' ']) | (B == [' ', ch, ch, ch, ' ']):
            if ((c_start-1) >= 0) & (A[r_start][c_start-1] == ' '):
                if ((c_start-2) >= 0) & (A[r_start][c_start-2] == ch):
                    return False
                return True
    return False


def Limit4_Nwest(ch, r_start, c_start, A):
    NC = len(A[0])
    if (c_start-5) < 0:
        return False
    else:
        B = [A[r_start][c_start-(m+1)] for m in range(4)]
        if B == [ch, ch, ch, ' ']:
            B += A[r_start][c_start-5]
            if B == [ch, ch, ch, ' ', ch]:
                return False
            elif (c_start+1) < NC:
                if A[r_start][c_start+1] == ' ':
                    if (c_start+2) < NC:
                        if A[r_start][c_start+2] == ch:
                            return False
                    return True
        B += A[r_start][c_start-5]
        if (B == [ch, ch, ' ', ch, ' ']) | (B == [ch, ' ', ch, ch, ' ']) | (B == [' ', ch, ch, ch, ' ']):
            if (c_start+1) < NC:
                if A[r_start][c_start+1] == ' ':
                    if (c_start+2) < NC:
                        if A[r_start][c_start+2] == ch:
                            return False
                    return True
    return False


def Limit4_Nsouth(ch, r_start, c_start, A):
    NR = len(A)
    if (r_start+5) >= NR:
        return False
    else:
        B=[A[r_start+(m+1)][c_start] for m in range(4)]
        if B == [ch, ch, ch, ' ']:
            B += A[r_start+5][c_start]
            if B == [ch, ch, ch, ' ', ch]:
                return False
            elif ((r_start-1) >= 0) & (A[r_start-1][c_start] == ' '):
                if ((r_start-2) >= 0) & (A[r_start-2][c_start] == ch):
                    return False
                return True
        B += A[r_start+5][c_start]
        if (B == [ch, ch, ' ', ch, ' ']) | (B == [ch, ' ', ch, ch, ' ']) | (B == [' ', ch, ch, ch, ' ']):
            if ((r_start-1) >= 0) & (A[r_start-1][c_start] == ' '):
                if ((r_start-2) >= 0) & (A[r_start-2][c_start] == ch):
                    return False
                return True
    return False


def Limit4_Nnorth(ch, r_start, c_start, A):
    NR = len(A)
    if (r_start-5) < 0:
        return False
    else:
        B = [A[r_start-(m+1)][c_start] for m in range(4)]
        if B == [ch, ch, ch, ' ']:
            B += A[r_start-5][c_start]
            if B == [ch, ch, ch, ' ', ch]:
                return False
            elif (r_start+1) < NR:
                if A[r_start+1][c_start] == ' ':
                    if (r_start+2)<NR:
                        if A[r_start+2][c_start] == ch:
                            return False
                    return True
        B += A[r_start-5][c_start]
        if (B == [ch, ch, ' ', ch, ' ']) | (B == [ch, ' ', ch, ch, ' ']) | (B == [' ', ch, ch, ch, ' ']):
            if (r_start+1) < NR:
                if A[r_start+1][c_start] == ' ':
                    if (r_start+2) < NR:
                        if A[r_start+2][c_start] == ch:
                            return False
                    return True
    return False


def Limit4_Nse(ch, r_start, c_start, A):
    NR = len(A)
    NC = len(A[0])
    if ((r_start+5) >= NR) | ((c_start+5) >= NC):
        return False
    else:
        B = [A[r_start+(m+1)][c_start+(m+1)] for m in range(4)]
        if B == [ch, ch, ch, ' ']:
            B += A[r_start+5][c_start+5]
            if B == [ch, ch, ch, ' ', ch]:
                return False
            elif (((r_start-1) >= 0) & ((c_start-1) >= 0)) & (A[r_start-1][c_start-1] == ' '):
                if (((r_start-2) >= 0) & ((c_start-2) >= 0)) & (A[r_start-2][c_start-2] == ch):
                    return False
                return True
        B += A[r_start+5][c_start+5]
        if (B == [ch, ch, ' ', ch, ' ']) | (B == [ch, ' ', ch, ch, ' ']) | (B == [' ', ch, ch, ch, ' ']):
            if (((r_start-1) >= 0) & ((c_start-1) >= 0)) & (A[r_start-1][c_start-1] == ' '):
                if (((r_start-2) >= 0) & ((c_start-2) >= 0)) & (A[r_start-2][c_start-2] == ch):
                    return False
                return True
    return False


def Limit4_Nne(ch, r_start, c_start, A):
    NR = len(A)
    NC = len(A[0])
    if ((r_start-5) < 0) | ((c_start+5) >= NC):
        return False
    else:
        B = [A[r_start-(m+1)][c_start+(m+1)] for m in range(4)]
        if B == [ch, ch, ch, ' ']:
            B += A[r_start-5][c_start+5]
            if B == [ch, ch, ch, ' ', ch]:
                return False
            elif ((r_start+1) < NR) & ((c_start-1) >= 0):
                if A[r_start+1][c_start-1] == ' ':
                    if ((r_start+2) < NR) & ((c_start-2) >= 0):
                        if A[r_start+2][c_start-2] == ch:
                            return False
                    return True
        B += A[r_start-5][c_start+5]
        if (B == [ch, ch, ' ', ch, ' ']) | (B == [ch, ' ', ch, ch, ' ']) | (B == [' ', ch, ch, ch, ' ']):
            if ((r_start+1) < NR) & ((c_start-1) >= 0):
                if A[r_start+1][c_start-1] == ' ':
                    if ((r_start+2)<NR)&((c_start-2) >= 0):
                        if A[r_start+2][c_start-2] == ch:
                            return False
                    return True
    return False


def Limit4_Nnw(ch, r_start, c_start, A):
    NR = len(A)
    NC = len(A[0])
    if ((r_start-5)<0) | ((c_start-5)<0):
        return False
    else:
        B = [A[r_start-(m+1)][c_start-(m+1)] for m in range(4)]
        if B == [ch, ch, ch, ' ']:
            B += A[r_start-5][c_start-5]
            if B == [ch, ch, ch, ' ', ch]:
                return False
            elif ((r_start+1) < NR) & ((c_start+1) < NC):
                if A[r_start+1][c_start+1] == ' ':
                    if ((r_start+2) < NR) & ((c_start+2) < NC):
                        if A[r_start+2][c_start+2] == ch:
                            return False
                    return True
        B += A[r_start-5][c_start-5]
        if (B == [ch, ch, ' ', ch, ' ']) | (B == [ch, ' ', ch, ch, ' ']) | (B == [' ', ch, ch, ch, ' ']):
            if ((r_start+1) < NR) & ((c_start+1) < NC):
                if A[r_start+1][c_start+1] == ' ':
                    if ((r_start+2) < NR) & ((c_start+2) < NC):
                        if A[r_start+2][c_start+2] == ch:
                            return False
                    return True
    return False


def Limit4_Nsw(ch, r_start, c_start, A):
    NR = len(A)
    NC = len(A[0])
    if ((r_start+5) >= NR) | ((c_start-5) < 0):
        return False
    else:
        B = [A[r_start+(m+1)][c_start-(m+1)] for m in range(4)]
        if B == [ch, ch, ch, ' ']:
            B += A[r_start+5][c_start-5]
            if B == [ch, ch, ch, ' ', ch]:
                return False
            elif ((r_start-1) >= 0) & ((c_start+1) < NC):
                if A[r_start-1][c_start+1] == ' ':
                    if ((r_start-2) >= 0) & ((c_start+2) < NC):
                        if A[r_start-2][c_start+2] == ch:
                            return False
                    return True
        B += A[r_start+5][c_start-5]
        if (B == [ch, ch, ' ', ch, ' ']) | (B == [ch, ' ', ch, ch, ' ']) | (B == [' ', ch, ch, ch, ' ']):
            if ((r_start-1) >= 0) & ((c_start+1) < NC):
                if A[r_start-1][c_start+1] == ' ':
                    if ((r_start-2) >= 0) & ((c_start+2) < NC):
                        if A[r_start-2][c_start+2] == ch:
                            return False
                    return True
    return False


def Limit4_Nmew(ch, r_start, c_start, A):
    NC = len(A[0])
    if ((c_start+3) >= NC) | ((c_start-2) < 0):
        return False
    else:
        b = [A[r_start][(c_start-2)+m] for m in range(6)]
        if (b == [' ', ch, ' ', ch, ch, ' ']) | (b == [' ', ch, ' ', ch, ' ', ch]) | (b == [' ', ch, ' ', ' ', ch, ch]) | (b == [ch, ' ', ' ', ch, ch, ' ']):
            if ((c_start+4) < NC) & ((c_start-3) >= 0):
                if (A[r_start][c_start-3] == ch) | (A[r_start][c_start+4] == ch):
                    return False
            return True
    if ((c_start+2) >= NC) | ((c_start-3) < 0):
        return False
    else:
        c = [A[r_start][(c_start-3)+m] for m in range(6)]
        if (c == [' ', ch, ch, ' ', ch, ' ']) | (c == [ch, ' ', ch, ' ', ch, ' ']) | (c == [ch, ch, ' ', ' ', ch, ' ']) | (c == [' ', ch, ch, ' ', ' ', ch]):
            if ((c_start+3) < NC) & ((c_start-4) >= 0):
                if (A[r_start][c_start-4] == ch) | (A[r_start][c_start+3] == ch):
                    return False
            return True
    return False


def Limit4_Nmsn(ch, r_start, c_start, A):
    NR = len(A)
    NC = len(A[0])
    if ((r_start+3) >= NR) | ((r_start-2) < 0):
        return False
    else:
        b = [A[(r_start-2)+m][c_start] for m in range(6)]
        if (b == [' ', ch, ' ', ch, ch, ' ']) | (b == [' ', ch, ' ', ch, ' ', ch]) | (b == [' ', ch, ' ', ' ', ch, ch]) | (b == [ch, ' ', ' ', ch, ch, ' ']):
            if ((r_start+4) < NC) & ((r_start-3) >= 0):
                if (A[r_start-3][c_start] == ch) | (A[r_start+4][c_start] == ch):
                    return False
            return True
    if ((r_start+2) >= NR) | ((r_start-3) < 0):
        return False
    else:
        c = [A[(r_start-3)+m][c_start] for m in range(6)]
        if (c == [' ', ch, ch, ' ', ch, ' ']) | (c == [ch, ' ', ch, ' ', ch, ' ']) | (c == [ch, ch, ' ', ' ', ch, ' ']) | (c == [' ', ch, ch, ' ', ' ', ch]):
            if ((r_start+3) < NC) & ((r_start-4) >= 0):
                if (A[r_start-4][c_start] == ch) | (A[r_start+3][c_start] == ch):
                    return False
            return True
    return False


def Limit4_Nmcross1(ch, r_start, c_start, A):
    NR = len(A)
    NC = len(A[0])
    if ((r_start+3) >= NR) | ((r_start-2) < 0) | ((c_start+3) >= NC) | ((c_start-2) < 0):
        return False
    else:
        b = [A[(r_start-2)+m][(c_start-2)+m] for m in range(6)]
        if (b == [' ', ch, ' ', ch, ch, ' ']) | (b == [' ', ch, ' ', ch, ' ', ch]) | (b == [' ', ch, ' ', ' ', ch, ch]) | (b == [ch, ' ', ' ', ch, ch, ' ']):
            if ((r_start+4) < NR) & ((r_start-3) >= 0) & ((c_start+4) < NC) & ((c_start-3) >= 0):
                if (A[r_start-3][c_start-3] == ch) | (A[r_start+4][c_start+4] == ch):
                    return False
            return True
    if ((r_start+2) >= NR) | ((r_start-3) < 0) | ((c_start+2) >= NC) | ((c_start-3) < 0):
        return False
    else:
        c = [A[(r_start-3)+m][(c_start-3)+m] for m in range(6)]
        if (c == [' ', ch, ch, ' ', ch, ' ']) | (c == [ch, ' ', ch, ' ', ch, ' ']) | (c == [ch, ch, ' ', ' ', ch, ' ']) | (c == [' ', ch, ch, ' ', ' ', ch]):
            if ((r_start+3) < NR) & ((r_start-4) >= 0) & ((c_start+3) < NC) & ((c_start-4) >= 0):
                if (A[r_start-4][c_start-4] == ch) | (A[r_start+3][c_start+3] == ch):
                    return False
            return True
    return False


def Limit4_Nmcross2(ch, r_start, c_start, A):
    NR = len(A)
    NC = len(A[0])
    if ((r_start+2) >= NR) | ((r_start-3) < 0) | ((c_start+3) >= NC) | ((c_start-2) < 0):
        return False
    else:
        b = [A[(r_start+2)-m][(c_start-2)+m] for m in range(6)]
        if (b == [' ', ch, ' ', ch, ch, ' ']) | (b == [' ', ch, ' ', ch, ' ', ch]) | (b == [' ', ch, ' ', ' ', ch, ch]) | (b == [ch, ' ', ' ', ch, ch, ' ']):
            if ((r_start+3) < NR) & ((r_start-4) >= 0) & ((c_start+4) < NC) & ((c_start-3) >= 0):
                if (A[r_start+3][c_start-3] == ch) | (A[r_start-4][c_start+4] == ch):
                    return False
            return True
    if ((r_start+3) >= NR) | ((r_start-2) < 0) | ((c_start+2) >= NC) | ((c_start-3) < 0):
        return False
    else:
        c = [A[(r_start+3)-m][(c_start-3)+m] for m in range(6)]
        if (c == [' ', ch, ch, ' ', ch, ' ']) | (c == [ch, ' ', ch, ' ', ch, ' ']) | (c == [ch, ch, ' ', ' ', ch, ' ']) | (c == [' ', ch, ch, ' ', ' ', ch]):
            if ((r_start+4) < NR) & ((r_start-3) >= 0) & ((c_start+3) < NC) & ((c_start-4) >= 0):
                if (A[r_start+4][c_start-4] == ch) | (A[r_start-3][c_start+3] == ch):
                    return False
            return True
    return False


def Limit4(ch, r_start, c_start, A):
    p = Limit4_Neast(ch, r_start, c_start, A)\
      + Limit4_Nwest(ch, r_start, c_start, A)\
      + Limit4_Nsouth(ch, r_start, c_start, A)\
      + Limit4_Nnorth(ch, r_start, c_start, A)\
      + Limit4_Nse(ch, r_start, c_start, A)\
      + Limit4_Nne(ch, r_start, c_start, A)\
      + Limit4_Nnw(ch, r_start, c_start, A)\
      + Limit4_Nsw(ch, r_start, c_start, A)\
      + Limit4_Nmew(ch, r_start, c_start, A)\
      + Limit4_Nmsn(ch, r_start, c_start, A)\
      + Limit4_Nmcross1(ch, r_start, c_start, A)\
      + Limit4_Nmcross2(ch, r_start, c_start, A)
    if p >= 2:
        return True
    else:
        return False


def Score4(ch, r_start, c_start, A):
    p = Limit4_Neast(ch, r_start, c_start, A)\
      + Limit4_Nwest(ch, r_start, c_start, A)\
      + Limit4_Nsouth(ch, r_start, c_start, A)\
      + Limit4_Nnorth(ch, r_start, c_start, A)\
      + Limit4_Nse(ch, r_start, c_start, A)\
      + Limit4_Nne(ch, r_start, c_start, A)\
      + Limit4_Nnw(ch, r_start, c_start, A)\
      + Limit4_Nsw(ch, r_start, c_start, A)\
      + Limit4_Nmew(ch, r_start, c_start, A)\
      + Limit4_Nmsn(ch, r_start, c_start, A)\
      + Limit4_Nmcross1(ch, r_start, c_start, A)\
      + Limit4_Nmcross2(ch, r_start, c_start, A)
    if p == 1:
        return True
    else:
        return False


def inarow_Neast(ch, r_start, c_start, A, N):
    NR = len(A)
    NC = len(A[0])
    if (r_start < 0) | (c_start < 0) | (r_start >= NR) | (c_start >= NC):
        return False
    elif (c_start+(N-1)) >= NC:
        return False
    else:
        B = [A[r_start][c_start+m] for m in range(N)]
        if B == [ch]*N:
            if (c_start+N) < NC:
                if A[r_start][c_start+N] != ' ':
                    return 0.5
                else: return 1
            else: return 0.5
        else: return False


def inarow_Nwest(ch, r_start, c_start, A, N):
    NR = len(A)
    NC = len(A[0])
    if (r_start < 0) | (c_start < 0) | (r_start >= NR) | (c_start >= NC):
        return False
    elif (c_start-(N-1)) < 0:
        return False
    else:
        B = [A[r_start][c_start-m] for m in range(N)]
        if B == [ch]*N:
            if (c_start-N) >= 0:
                if A[r_start][c_start-N] != ' ':
                    return 0.25
                else: return 1
            else: return 0.25
        else: return False


def inarow_Nsouth(ch, r_start, c_start, A, N):
    NR = len(A)
    NC = len(A[0])
    if (r_start < 0) | (c_start < 0) | (r_start >= NR) | (c_start >= NC):
        return False
    elif (r_start+(N-1)) >= NR:
        return False
    else:
        B = [A[r_start+m][c_start] for m in range(N)]
        if B == [ch]*N:
            if (r_start+N) < NR:
                if A[r_start+N][c_start] != ' ':
                    return 0.25
                else: return 1
            else: return 0.25
        else: return False


def inarow_Nnorth(ch, r_start, c_start, A, N):
    NR = len(A)
    NC = len(A[0])
    if (r_start < 0) | (c_start < 0) | (r_start >= NR) | (c_start >= NC):
        return False
    elif (r_start-(N-1)) < 0:
        return False
    else:
        B = [A[r_start-m][c_start] for m in range(N)]
        if B == [ch]*N:
            if (r_start-N) >= 0:
                if A[r_start-N][c_start] != ' ':
                    return 0.25
                else: return 1
            else: return 0.25
        else: return False


def inarow_Nse(ch,r_start,c_start,A,N):
    NR=len(A)
    NC=len(A[0])
    if ((r_start<0)|(c_start<0)|(r_start>=NR)|(c_start>=NC)):
        return False
    elif ((r_start+(N-1))>=NR)|((c_start+(N-1))>=NC):
        return False
    else:
        B=[A[r_start+m][c_start+m] for m in range(N)]
        if B == [ch]*N:
            if ((r_start+N)<NR)&((c_start+N)<NC):
                if A[r_start+N][c_start+N] != ' ':
                    return 0.25
                else: return 1
            else: return 0.25
        else: return False


def inarow_Nne(ch, r_start, c_start, A, N):
    NR = len(A)
    NC = len(A[0])
    if (r_start < 0) | (c_start < 0) | (r_start >= NR) | (c_start >= NC):
        return False
    elif ((r_start-(N-1)) < 0) | ((c_start+(N-1)) >= NC):
        return False
    else:
        B = [A[r_start-m][c_start+m] for m in range(N)]
        if B == [ch]*N:
            if ((r_start-N) >= 0) & ((c_start+N) < NC):
                if A[r_start-N][c_start+N] != ' ':
                    return 0.25
                else: return 1
            else: return 0.25
        else: return False


def inarow_Nnw(ch, r_start, c_start, A, N):
    NR = len(A)
    NC = len(A[0])
    if (r_start < 0) | (c_start < 0) | (r_start >= NR) | (c_start >= NC):
        return False
    elif ((r_start-(N-1)) < 0) | ((c_start-(N-1)) < 0):
        return False
    else:
        B = [A[r_start-m][c_start-m] for m in range(N)]
        if B == [ch]*N:
            if ((r_start-N) >= 0) & ((c_start-N) >= 0):
                if A[r_start-N][c_start-N] != ' ':
                    return 0.25
                else: return 1
            else: return 0.25
        else: return False


def inarow_Nsw(ch, r_start, c_start, A, N):
    NR = len(A)
    NC = len(A[0])
    if (r_start < 0) | (c_start < 0) | (r_start >= NR) | (c_start >= NC):
        return False
    elif ((r_start+(N-1)) >= NR) | ((c_start-(N-1)) < 0):
        return False
    else:
        B = [A[r_start+m][c_start-m] for m in range(N)]
        if B == [ch]*N:
            if ((r_start+N) < NR) & ((c_start-N) >= 0):
                if A[r_start+N][c_start-N] != ' ':
                    return 0.25
                else: return 1
            else: return 0.25
        else: return False
