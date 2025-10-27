import tkinter as tk
import random

class SudokuGame:

    def __init__(self):
        self.window = tk.Tk()
        self.difficulties = {1:45, 2:35, 3:30, 4:25, 5:17}
        self.difficulty = 1

        self.window.columnconfigure([i for i in range(9)], minsize=30, weight=1)
        self.window.rowconfigure([i for i in range(11)], minsize=30, weight=1)
        self.buttons()
        self.new_sudoku()
        self.window.mainloop()

    def new_sudoku(self):
        self.sudoku = self.random_sudoku()
        for line in self.sudoku:
            print(line)
        self.empty_spaces()
        self.display_sudoku()

    def empty_spaces(self):
        for i in range(81-self.difficulties[self.difficulty]):
            while True:
                r = random.randint(0,8)
                c = random.randint(0,8)
                if self.sudoku[r][c] == 0:
                    continue
                else:
                    self.sudoku[r][c] = 0
                    break


    def check_sudoku(self):
        # Update Sudoku
        for box in self.boxes:
            if box[0].get() != "":
                box[0].delete(1,tk.END)
                try:
                    number = int(box[0].get())
                    self.sudoku[box[1]][box[2]] = number
                    box[0]["background"] = "white"
                except:
                    box[0]["background"] = "red"
                    box[0].delete(0)
            else:
                box[0]["background"] = "white"

        self.lines = True
        self.columns = True
        self.blocks = True

        # Check lines
        for line in self.sudoku:
            if 0 in line:
                self.lines = False
            if sorted(line) != [1,2,3,4,5,6,7,8,9] and 0 not in line:
                self.lines = False
                doubles = []
                for n in set(line):
                    if line.count(n) > 1:
                        doubles.append(n)
                for box in self.boxes:
                    if box[1] == self.sudoku.index(line) and self.sudoku[box[1]][box[2]] in set(doubles):
                        box[0]["background"] = "red"
            

        # Check columns
        for i in range(9):
            column = []
            for line in self.sudoku:
                column.append(line[i])
            
            if sorted(column) != [1,2,3,4,5,6,7,8,9] and 0 not in column:
                self.columns = False
                doubles = []
                for n in set(column):
                    if column.count(n) > 1:
                        doubles.append(n)
                for box in self.boxes:
                    if box[2] == i and self.sudoku[box[1]][box[2]] in set(doubles):
                        box[0]["background"] = "red"

        # Check blocks
        guiblocks = []
        for c in range(3):
            for b in range(3):
                guiblock = []
                for i in range(b*3, b*3+3):
                    for j in range(c*3,c*3+3):
                        for box in self.boxes:
                            if box[1] == j and box[2] == i:
                                guiblock.append(box)
                guiblocks.append(guiblock)

        squares = [[self.sudoku[0][0:3], self.sudoku[1][0:3], self.sudoku[2][0:3]],
                [self.sudoku[0][3:6], self.sudoku[1][3:6], self.sudoku[2][3:6]],
                [self.sudoku[0][6:], self.sudoku[1][6:], self.sudoku[2][6:]],
                [self.sudoku[3][0:3], self.sudoku[4][0:3], self.sudoku[5][0:3]],
                [self.sudoku[3][3:6], self.sudoku[4][3:6], self.sudoku[5][3:6]],
                [self.sudoku[3][6:], self.sudoku[4][6:], self.sudoku[5][6:]],
                [self.sudoku[6][0:3], self.sudoku[7][0:3], self.sudoku[8][0:3]],
                [self.sudoku[6][3:6], self.sudoku[7][3:6], self.sudoku[8][3:6]],
                [self.sudoku[6][6:], self.sudoku[7][6:], self.sudoku[8][6:]]]
        for block in squares:
            numbers = []
            for i in block:
                for j in i:
                    numbers.append(j)
            if sorted(numbers) != [1,2,3,4,5,6,7,8,9] and 0 not in numbers:
                self.blocks = False
                for box in guiblocks[squares.index(block)]:
                    box[0]["background"] = "red"
        
        if self.lines == True and self.columns == True and self.blocks == True:
            for i in self.given:
                i[0]["background"] = "green"

            for i in self.boxes:
                i[0]["background"] = "green"
        
        for box in self.boxes:
            if box[0].get() == "":
                box[0]["background"] = "white"

        
    def toggle_difficulty(self):
        self.difficulty += 1
        if self.difficulty > len(self.difficulties):
            self.difficulty = 1
        self.btn_difficulty["text"] = f"DIFFICULTY: {self.difficulty}"

    def display_sudoku(self):
        self.boxes = []
        self.given = []
        for r in range(9):
            for c in range(9):
                if self.sudoku[r][c] == 0:
                    tbox = tk.Entry(width=1, justify="center")
                    tbox.grid(row=r+1, column=c, sticky="nsew")
                    self.boxes.append((tbox, r, c))
                else:
                    label = tk.Label(text=self.sudoku[r][c], relief=tk.RAISED, borderwidth=1)
                    label.grid(row=r+1, column=c, sticky="nsew")
                    self.given.append((label, r, c))

    def buttons(self):
        btn_new = tk.Button(text="NEW SUDOKU", command=self.new_sudoku)
        btn_new.grid(row=0, column=0, sticky="nsew",columnspan=3)
        self.btn_difficulty = tk.Button(text=f"DIFFICULTY: {self.difficulty}", command=self.toggle_difficulty)
        self.btn_difficulty.grid(row=0, column=3, sticky="nsew", columnspan=3)
        btn_quit = tk.Button(text="QUIT", bg="red", command=self.kill)
        btn_quit.grid(row=0,column=6, sticky="nsew",columnspan=3)
        btn_check = tk.Button(text= "CHECK", bg="green", command=self.check_sudoku)
        btn_check.grid(row=10,column=0,sticky="nsew",columnspan=9)

    def kill(self):
        self.window.destroy()

    def random_sudoku(self):
        base  = 3
        side  = base*base

        # pattern for a baseline valid solution
        def pattern(r,c): return (base*(r%base)+r//base+c)%side

        # randomize rows, columns and numbers (of valid base pattern)
        def shuffle(s): return random.sample(s,len(s)) 
        rBase = range(base) 
        rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
        cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
        nums  = shuffle(range(1,base*base+1))

        # produce board using randomized baseline pattern
        sudoku = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

        return sudoku

    
game = SudokuGame()