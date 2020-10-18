import math as m
import scred_P2014013364 as sA


class Player:
    def __init__(self, ch):
        self.ox = ch

    def oppCH(self, ox):  # 상대 수
        if ox == 'O':
            return 'X'
        else:
            return 'O'

    def sc_f(self, r, c, ox, b):  # 연속된 돌의 갯수를 세는 함수, 뒤가 막혀있으면 0.75점 감점.
        p = [0, 0, 0, 0]
        for i in range(2, 5):

            east = sA.inarow_Neast(ox, r, c, b.Data, i)
            if sA.inarow_Neast(ox, r, c, b.Data, i+1):
                    east = 0
            if east > 0:
                b.addMove(r, c, self.oppCH(ox))
                if sA.inarow_Nwest(self.oppCH(ox), r, c, b.Data, 2):
                    east -= 0.75
                b.addMove(r, c, ox)

            west = sA.inarow_Nwest(ox, r, c, b.Data, i)
            if sA.inarow_Nwest(ox, r, c, b.Data, i+1):
                    west = 0
            if west > 0:
                b.addMove(r, c, self.oppCH(ox))
                if sA.inarow_Neast(self.oppCH(ox), r, c, b.Data, 2):
                    west -= 0.75
                b.addMove(r, c, ox)

            north = sA.inarow_Nnorth(ox, r, c, b.Data, i)
            if sA.inarow_Nnorth(ox, r, c, b.Data, i+1):
                    north = 0
            if north > 0:
                b.addMove(r, c, self.oppCH(ox))
                if sA.inarow_Nsouth(self.oppCH(ox), r, c, b.Data, 2):
                    north -= 0.75
                b.addMove(r, c, ox)

            south = sA.inarow_Nsouth(ox, r, c, b.Data, i)
            if sA.inarow_Nsouth(ox, r, c, b.Data, i+1):
                    south = 0
            if south > 0:
                b.addMove(r, c, self.oppCH(ox))
                if sA.inarow_Nnorth(self.oppCH(ox), r, c, b.Data, 2):
                    south -= 0.75
                b.addMove(r, c, ox)

            se = sA.inarow_Nse(ox, r, c, b.Data, i)
            if sA.inarow_Nse(ox, r, c, b.Data, i+1):
                    se = 0
            if se > 0:
                b.addMove(r, c, self.oppCH(ox))
                if sA.inarow_Nnw(self.oppCH(ox), r, c, b.Data, 2):
                    se -= 0.75
                b.addMove(r, c, ox)

            ne = sA.inarow_Nne(ox, r, c, b.Data, i)
            if sA.inarow_Nne(ox, r, c, b.Data, i+1):
                    ne = 0
            if ne > 0:
                b.addMove(r, c, self.oppCH(ox))
                if sA.inarow_Nsw(self.oppCH(ox), r, c, b.Data, 2):
                    ne -= 0.75
                b.addMove(r, c, ox)

            nw = sA.inarow_Nnw(ox, r, c, b.Data, i)
            if sA.inarow_Nnw(ox, r, c, b.Data, i+1):
                    nw = 0
            if nw > 0:
                b.addMove(r, c, self.oppCH(ox))
                if sA.inarow_Nse(self.oppCH(ox), r, c, b.Data, 2):
                    nw -= 0.75
                b.addMove(r, c, ox)

            sw = sA.inarow_Nsw(ox, r, c, b.Data, i)
            if sA.inarow_Nsw(ox, r, c, b.Data, i+1):
                    sw = 0
            if sw > 0:
                b.addMove(r, c, self.oppCH(ox))
                if sA.inarow_Nne(self.oppCH(ox), r, c, b.Data, 2):
                    sw -= 0.75
                b.addMove(r, c, ox)

            p[i-2] += (east+west+north+south+sw+se+ne+nw)

        s = p[0]*3 + p[1]*10 + p[2]*100
        return s

    def scores_for(self, b):  # 점수 채점
        scores = [[0]*b.W for _ in range(b.H)]
        for r in range(b.H):
            for c in range(b.W):
                if not b.allowsMove(r, c):
                    scores[r][c] = -1
                elif b.allowsMove(r, c):
                    b.addMove(r, c, self.ox)
                    if b.winsFor(self.ox):
                        scores[r][c] += 5000*5000
                    scores[r][c] += self.sc_f(r, c, self.ox, b)*1.1
                    b.addMove(r, c, ' ')
                    scores[r][c] += (sA.Score2(self.ox, r, c, b.Data)*2.25)  # 떨어진 2수 계산
                    scores[r][c] += (sA.Limit2(self.ox, r, c, b.Data)*5.5)  # 떨어진 22수 계산
                    scores[r][c] += (sA.Score3(self.ox, r, c, b.Data)*12.5)  # 떨어진 3수 계산
                    scores[r][c] += (sA.Limit3(self.ox, r, c, b.Data)*35.5)  # 떨어진 33수 계산
                    scores[r][c] += (sA.Score4(self.ox, r, c, b.Data)*110.5)  # 떨어진 4수 계산
                    scores[r][c] += (sA.Limit4(self.ox, r, c, b.Data)*500.5)  # 떨어진 44수 계산
                    b.addMove(r, c, self.oppCH(self.ox))
                    if b.winsFor(self.oppCH(self.ox)):
                        scores[r][c] += 10000
                    scores[r][c] += self.sc_f(r, c, self.oppCH(self.ox), b)
                    b.addMove(r, c, ' ')
                    scores[r][c] += (sA.Score2(self.oppCH(self.ox), r, c, b.Data)*2)  # 상대의 떨어진 2수 계산
                    scores[r][c] += (sA.Limit2(self.oppCH(self.ox), r, c, b.Data)*5)  # 상대의 떨어진 22수 계산
                    scores[r][c] += (sA.Score3(self.oppCH(self.ox), r, c, b.Data)*11)  # 상대의 떨어진 3수 계산
                    scores[r][c] += (sA.Limit3(self.oppCH(self.ox), r, c, b.Data)*32)  # 상대의 떨어진 33수 계산
                    scores[r][c] += (sA.Score4(self.oppCH(self.ox), r, c, b.Data)*100)  # 떨어진 4수 계산
                    scores[r][c] += (sA.Limit4(self.oppCH(self.ox), r, c, b.Data)*500)  # 상대의 떨어진 44수 계산
        return scores

    def tieSelection(self, scores):
        nr = len(scores)
        nc = len(scores[0])
        max_value = max([max(i)] for i in scores)
        maxlndices = []
        for r in range(nr):
            for c in range(nc):
                if scores[r][c] == max_value[0]:
                    maxlndices += [[r, c]]

        best_n = 0
        r_center = m.floor(nr/2)
        c_center = m.floor(nc/2)

        min_distance = 100
        for n in range(len(maxlndices)):
            check_disk = abs(maxlndices[n][0] - r_center)+abs(maxlndices[n][1] - c_center)
            if min_distance > check_disk:
                min_distance = check_disk
                best_n = n
        return maxlndices[best_n]

    def nextMove(self, b):  # 컴퓨터의 수
        scores = self.scores_for(b)
        return self.tieSelection(scores)
