'''
경상대학교 정보통신공학과 2017년 2학기 파이썬 프로그래밍. 오목 프로젝트 코드.
작성일시: 2017년 12월 13일
작성자: 조교수 김성환
https://www.cs.hmc.edu/csforall/index.html 의 자료를 참고하였음.
'''

import Lec_Omok1 as Lec1
import P2014013364 as P1
import P2019Winner as P2
from tkinter import *
import time
window = Tk()

class Board():
    def __init__(self, width, height,win_N, window):
        self.W = width        #오목판의 세로줄 수
        self.H = height       #오목판의 가로줄 수
        self.boundary = 30    #오목판의 가장자리 너비
        self.canvas_width = 700      #오목판의 너비
        self.canvas_height = 700     #오목판의 높이
        self.canvas = Canvas(window, width=self.canvas_width, height = self.canvas_height, bg='#CC6600')
        self.Win_Number = win_N
        self.Data = [ [' ']*self.W for row in range(self.H) ]
        self.P1_ox = 'X'
        self.P2_ox = 'O'
        self.turn = 'X'   # 어떤 문자를 둘 차례인지 기록, 'X'부터 시작.

    # canvas를 초기화하는 메서드
    def initial_canvas(self):
        print('Initializing')
        b.canvas.delete('all')
        H = self.H
        W = self.W
        line_width = self.canvas_width-2*self.boundary
        line_height = self.canvas_height-2*self.boundary
        b_bndry = self.boundary
        gap_H = line_width/(H-1)
        gap_W = line_height/(W-1)
        for a in range(W):
            self.canvas.create_line(b_bndry+gap_W*a,b_bndry,b_bndry+gap_W*a,b_bndry+line_height)
        for a in range(H):
            self.canvas.create_line(b_bndry,b_bndry+gap_H*a,b_bndry+line_width,b_bndry+gap_H*a)
        self.canvas.pack()
        return

    def addMove(self, row, col, ch):
        self.Data[row][col] = ch

    def addMove_New(self, row, col, ch):
        H = self.H
        W = self.W
        line_width = self.canvas_width-2*self.boundary
        line_height = self.canvas_height-2*self.boundary
        b_bndry = self.boundary
        gap_H= line_width/(H-1)
        gap_W = line_height/(W-1)
        radius = gap_W/2*0.75
        self.Data[row][col] = ch
        if ch == 'X':
            self.canvas.create_oval(b_bndry + gap_W*col - radius, b_bndry + gap_H*row - radius, b_bndry + gap_W*col+radius , b_bndry+ gap_H*row+radius, fill='black')
        else:
            self.canvas.create_oval(b_bndry + gap_W*col - radius, b_bndry + gap_H*row - radius, b_bndry + gap_W*col+radius , b_bndry+ gap_H*row+radius, fill='white')

    def clear(self):
        for row in range(self.H):
            for col in range(self.W):
                self.Data[row][col] = ' '

    def allowsMove(self,row,col):
        if col < 0 or  col >= self.W or row <0 or row >= self.H:
            return False
        elif self.Data[row][col] != ' ':
            return False
        else:
            return True

    def isFull(self):
        temp = 0
        flag = False
        for r in range(self.H):
            for c in range(self.W):
                if self.Data[r][c] == ' ':
                    temp += 1
        if temp == 0:
            return True
        else:
            return False

    def setBoard(self, moveList):
        nextCh = 'X'   # 'X' 부터 둔다고 가정
        for colList in moveList:
            self.addMove(colList[0],colList[1], nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'

    # 6목 이상일 경우 이기지 못한 것으로 간주하는 기능을 추가
    def winsFor(self, ox):
        for row in range(self.H):
            for col in range(self.W):
                if Lec1.inarow_Neast(ox,row,col,self.Data,self.Win_Number):
                    if (col-1<0 or self.Data[row ][col-1] != ox ) and (col+self.Win_Number>=self.W or self.Data[row][col+self.Win_Number]!= ox):
                        return True
                if Lec1.inarow_Nsouth(ox,row,col,self.Data,self.Win_Number):
                    if (row-1 < 0 or self.Data[row-1][col] != ox ) and (row+self.Win_Number>=self.H or self.Data[row+self.Win_Number][col]!= ox ):
                       return True
                if Lec1.inarow_Nse(ox,row,col,self.Data,self.Win_Number):
                    if (row-1<0 or col-1<0 or self.Data[row-1][col-1] != ox ) and (row+self.Win_Number >=self.H or col+self.Win_Number>=self.W or self.Data[row+self.Win_Number][col+self.Win_Number] != ox ):
                        return True
                if Lec1.inarow_Nne(ox,row,col,self.Data,self.Win_Number):
                    if (row+1 >= self.H or col-1 <0 or self.Data[row+1][col-1] != ox ) and (row-self.Win_Number<0 or col+self.Win_Number>=self.W or self.Data[row-self.Win_Number][col+self.Win_Number] != ox ):
                        return True
        return False

    # hostGame()은 삭제

    def playGame(self):
        time.sleep(1)  #1초 간격으로 착점 좌표를 가져옴

        '''오목판 원본이 훼손되지 않도록 nextMove()에 self 대신 b_test를 넘겨준다.
           Board 클래스를 정의할 때, Board 클래스의 인스턴스를 생성할 수 있음!'''
        b_test = Board(self.W, self.H, self.Win_Number, window)
        b_test.Data = [self.Data[row][:] for row in range(self.H)]     # 현재 Board의 Data를 b_test.Data에 복사함.

        if self.turn == 'X':
            if p1.ox == 'human':
                flag = False
                while flag == False:
                    try:
                        users = eval(input('X\'s choice:'))
                        flag = self.allowsMove(users[0], users[1])
                    except SyntaxError:
                        flag = False
            else:
                users = p1.nextMove(b_test)
                while self.allowsMove(users[0],users[1]) == False:
                   users = p1.nextMove(b_test)

            self.addMove_New(users[0],users[1],self.turn)
            Lec1.print2d(self.Data)
            if self.winsFor(self.P1_ox) == True:
                print('X wins—Congratulations!')
                return
            elif self.isFull() == True:
                print('Board is Full!')
                return
            self.turn = 'O'
        else:
            if p2.ox == 'human':
                flag = False
                while flag == False:
                    try:
                        users = eval(input('O\'s choice:'))
                        flag = self.allowsMove(users[0], users[1])
                    except SyntaxError:
                        flag = False
            else:
                users = p2.nextMove(b_test)
                while self.allowsMove(users[0],users[1]) == False:
                    users = p2.nextMove(b_test)

            self.addMove_New(users[0],users[1],self.turn)
            Lec1.print2d(self.Data)
            if self.winsFor(self.P2_ox) == True:
                print('O wins—Congratulations!')
                return
            elif self.isFull() == True:
                print('Board is Full!')
                return
            self.turn = 'X'
        # 50msec 마다 self.playGame 메서드를 호출함. 일종의 재귀용법임.
        window.after(50, self.playGame)

b = Board(19, 19, 5, window)
p1 = P1.Player('X')
#p1 = P.Player('human')
p2 = P2.Player('O')
#p2 = P2.Player('human')
b.initial_canvas()

def process(master):
    b.clear()
    b.initial_canvas()
    b.playGame()   # playGame()에 인자를 넘겨주지 않음.

#파일 실행 후 스페이스 바 누르면 게임 시작
window.bind("<space>", process)
window.mainloop()
