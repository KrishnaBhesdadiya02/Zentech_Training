# Tasks


# Stack
stack = []

def push():
    x = input("Enter an element to push into the stack:")
    stack.append(x)

def pop():
    if not stack:
        print("Stack is empty.")
    else:
        print("Poped element:",stack.pop())

def peep():
    if not stack:
        print("Stack is empty.")
    else:
        print("Peeped element:",stack[-1])

def display():
    print(stack)

while True:
    print("----------------------------------------------------")
    print("Select Stack operation that you want to perform.")
    print("\n1. Push\n2. Pop\n3. Peep\n4. Display Stack\n5. Exit")
    choice = int(input("Enter your choice:"))

    match choice:
        case 1:
            push()
        case 2:
            pop()
        case 3:
            peep()
        case 4:
            display()
        case 5:
            break
        case _:
            print("Enter valid input.")
    


# Queue
queue =[]

def enqueue():
    x = input("Enter an element to enqueue into queue:")
    queue.append(x)

def dequeue():
    if not queue:
        print("Queue is empty.")
    else:
        print("Dequeued element:",queue.pop(0))

def peek():
    if not queue:
        print("Queue is empty.")
    else:
        print("Peeked element(First joined):",queue[0])

def display():
    print(queue)
    
while True:
    print("----------------------------------------------------")
    print("Select Queue operation that you want to perform.")
    print("\n1. Enqueue\n2. Dequeue\n3. Peek\n4. Display Queue\n5. Exit")
    choice = int(input("Enter your choice:"))

    match choice:
        case 1:
            enqueue()
        case 2:
            dequeue()
        case 3:
            peek()
        case 4:
            display()
        case 5:
            break
        case _:
            print("Enter valid input.")



# Circular queue
class CircularQueue:
    
    def __init__(self,size):
        self.Capacity = size
        self.f=-1
        self.r=-1
        self.qs=0
        self.queue = [None] * self.Capacity

    def Enqueue(self,ele):
        if self.qs == self.Capacity:
            print("Queue is full.")
        else:
            self.r=(self.r+1)%self.Capacity
            self.queue[self.r] = ele
            self.qs+=1
            if self.f == -1:
                self.f = 0
            
    def Dequeue(self):
        if self.qs == 0:
            print("Queue is Empty.")
        else:
            print("Dequeued element:",self.queue[self.f])
            self.f=(self.f+1)%self.Capacity
            self.qs-=1   
            if self.qs == 0:
                self.f = -1
                self.r = -1

    def Front(self):
        if self.f == -1:
            print("Queue is empty!")
        else:
            print("Front:", self.queue[self.f])

    def Rear(self):
        if self.r == -1:
            print("Queue is empty!")
        else:
            print("Rear:", self.queue[self.r])

    def Display(self):
        if self.qs==0:
            print("Circular Queue is empty.")
        else:
            temp = self.f
            while True:
                print(self.queue[temp],end=" ")
                if temp == self.r:
                    break
                temp=(temp+1)%self.Capacity
            print()

size = int(input("Enter size of a circular queue:"))
cq = CircularQueue(size)

    
while True:
    print("------------------------------------------------------------")
    print("Select Circular Queue operation that you want to perform.")
    print("\n1. Front\n2. Rear\n3. Enqueue\n4. Dequeue\n5. Display Circular Queue\n6. Exit")
    choice = int(input("Enter your choice:"))

    match choice:
        case 1:
            cq.Front()
        case 2:
            cq.Rear()
        case 3:
            ele = int(input("Enter an element you want to enqueue:"))
            cq.Enqueue(ele)
        case 4:
            cq.Dequeue()
        case 5:
            cq.Display()
        case 6:
            break
        case _:
            print("Enter valid input.")



# Bubble Sort
def BubbleSort(arr):
	size = len(arr)
	for i in range(size):
		swapped = False
		print(arr)
		for j in range(0,size-i-1):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]
				swapped = True
		if not swapped:
			break
	print("Final Sorted Array:",arr)

arr = [5,3,8,2,9,6]
BubbleSort(arr)



# Selection Sort
def SelectionSort(arr):
    for i in range(len(arr)-1):
        small = i
        print(arr)
        for j in range(i+1,len(arr)):
            if arr[small] > arr[j]:
                small = j
        if small != i:
            arr[i],arr[small] = arr[small],arr[i]
    print("Final Sorted Array:",arr)
arr = [5,3,8,2,9,6]
SelectionSort(arr)



# Insertion Sort
def InsertionSort(arr):
    for i in range(1,len(arr)):
        print(arr)
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    print("Final Sorted Array:",arr)      
arr = [5,3,8,2,9,6]
InsertionSort(arr)



# Binary Search
arr = [40, 10, 30, 20, 50]

# selection sort
for i in range(len(arr)-1):
    small = i
    for j in range(i+1,len(arr)):
        if arr[small] > arr[j]:
            small = j
    if small != i:
        arr[i],arr[small] = arr[small],arr[i]
print("Sorted list:", arr)

target = int(input("Enter element to search: "))
low, high = 0, len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Element found at index:", mid)
        found = True
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found.") 




# Matrix multiplication
A = []
B = []

print("Enter elements of first 3x3 matrix:")
for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input(f"A[{i}][{j}]: ")))
    A.append(row)

print("Enter elements of second 3x3 matrix:")
for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input(f"B[{i}][{j}]: ")))
    B.append(row)

C = [[0] * 3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        for k in range(3):
            C[i][j] += A[i][k] * B[k][j]

print("Result:")
for row in C:
    print(*row)




# diterminent of matrix
matrix = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input(f"Enter element [{i}][{j}]: ")))
    matrix.append(row)

a, b, c = matrix[0]
d, e, f = matrix[1]
g, h, i = matrix[2]

det = (
        a * (e * i - f * h) 
        - b * (d * i - f * g) 
        + c * (d * h - e * g)
      )

print("Determinant:", det)




# Rearrange array
A = [1,3,4,2,0]
B = [None]*5
for i in range(len(A)):  
    B[A[i]]=i
print(f"Original:{A}")
print(f"Rearranged:{B}")




# pelindrome number
n = int(input("Enter a number: "))

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")




# Cow Bull
import random
digits = [str(x) for x in range(10)]
actual = "".join(random.sample(digits, 4))
cow=0
Count=0
while cow!=4:
    cow=0
    bull=0
    num = input("Enter 4 digit number:")
    
    actual_used = [False] * len(actual)
    num_used = [False] * len(num)
    
    for i in range(len(num)):
        if num[i] == actual[i]:
            cow+=1
            actual_used[i] = True
            num_used[i] = True
            
    for i in range(len(num)):
        if not num_used[i]:
            for j in range(len(actual)):
                if not actual_used[j] and num[i] == actual[j]:
                    bull += 1
                    actual_used[j] = True  # Mark it as used
                    break  # Move to the next digit in 'num'
    Count+=1
    print(f"Cows: {cow}, Bulls: {bull}")
print(f"Total Trys:{Count}")



# Factors
n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Enter a positive integer.")
else:
    factors = []

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)

            if i != n // i:
                factors.append(n // i)

    factors.sort()
    print("Factors:", factors)



# GCD & LCM 
import math

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = math.gcd(a, b)

if a == 0 or b == 0:
    lcm = 0
else:
    lcm = abs(a * b) // gcd

print("GCD:", gcd)
print("LCM:", lcm)




# ATM machine
users = {
    "1234567890123456": {
        "pin": "1234",
        "name": "Rahul",
        "bank": "ABC",
        "balance": 10000
    },
    "9876543210987654": {
        "pin": "5678",
        "name": "Priya",
        "bank": "XYZ",
        "balance": 15000
    }
}

atms = {
    "1": {"bank": "ABC", "cash": 50000},
    "2": {"bank": "XYZ", "cash": 50000}
}

TRANSACTION_LIMIT = 10000
DAILY_WITHDRAWAL_LIMIT = 20000
MAX_TRANSACTIONS = 5

while True:
    print("\nAvailable ATMs:")
    for key, atm in atms.items():
        print(key, "-", atm["bank"])

    atm_choice = input("Choose ATM (or X to exit): ")

    if atm_choice.lower() == "x":
        break

    if atm_choice not in atms:
        print("Invalid ATM.")
        continue

    atm = atms[atm_choice]
    card = input("Enter card number: ")
    pin = input("Enter PIN: ")

    user = users.get(card)

    if user is None or user["pin"] != pin:
        print("Invalid card or PIN.")
        continue

    transactions = 0
    daily_withdrawal = 0

    while True:
        print("\n1. Account Information")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Change ATM")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            print("Name:", user["name"])
            print("Bank:", user["bank"])
            print("Balance:", user["balance"])
            print("ATM cash:", atm["cash"])
            print("Transactions:", transactions)

        elif choice in ("2", "3"):
            if transactions >= MAX_TRANSACTIONS:
                print("Transaction limit reached.")
                continue

            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("Enter a valid amount.")
                continue

            if amount <= 0:
                print("Amount must be positive.")
                continue

            if amount != int(amount):
                print("Use whole-number amounts.")
                continue

            amount = int(amount)

            if amount > TRANSACTION_LIMIT:
                print("Maximum per transaction is", TRANSACTION_LIMIT)
                continue

            if choice == "2":
                fee = amount * 0.05 if atm["bank"] != user["bank"] else 0
                total = amount + fee

                if daily_withdrawal + amount > DAILY_WITHDRAWAL_LIMIT:
                    print("Daily withdrawal limit exceeded.")
                elif user["balance"] < total:
                    print("Insufficient account balance.")
                elif atm["cash"] < amount:
                    print("ATM has insufficient cash.")
                else:
                    user["balance"] -= total
                    atm["cash"] -= amount
                    daily_withdrawal += amount
                    transactions += 1
                    print("Withdrawn:", amount)
                    print("Fee:", fee)
                    print("Remaining balance:", user["balance"])

            else:
                user["balance"] += amount
                transactions += 1
                print("Deposited successfully.")

        elif choice == "4":
            break

        elif choice == "5":
            raise SystemExit

        else:
            print("Invalid choice.")




# Tic Tac Toe
def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i + 3]))
        if i < 6:
            print("--+---+--")


def winner(board, mark):
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(all(board[i] == mark for i in line)
               for line in lines)


def minimax(board, is_max):
    if winner(board, "O"):
        return 1
    if winner(board, "X"):
        return -1
    if " " not in board:
        return 0

    scores = []

    for i in range(9):
        if board[i] == " ":
            board[i] = "O" if is_max else "X"
            scores.append(minimax(board, not is_max))
            board[i] = " "

    return max(scores) if is_max else min(scores)


def computer_move(board):
    best_score = -float("inf")
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


mode = input("Enter 1 for two players, 2 for computer: ")
board = [" "] * 9
current = "X"

while True:
    print_board(board)

    if mode == "2" and current == "O":
        move = computer_move(board)
        print("Computer chooses:", move + 1)
    else:
        try:
            move = int(input(f"Player {current}, choose 1-9: ")) - 1
        except ValueError:
            print("Enter a number from 1 to 9.")
            continue

        if not 0 <= move < 9 or board[move] != " ":
            print("Invalid or occupied position.")
            continue

    board[move] = current

    if winner(board, current):
        print_board(board)
        print(current, "wins!")
        break

    if " " not in board:
        print_board(board)
        print("It's a draw!")
        break

    current = "O" if current == "X" else "X"



# --Pattern--

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
n = int(input("Enter a number:"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()


# 15 14 13 12 11 
# 10 9 8 7 
# 6 5 4 
# 3 2 
# 1 
n = int(input("Enter a number:"))
num=(n*(n+1))//2
for i in range(n,0,-1):
    for j in range(i):
        print(num,end=" ")
        num-=1
    print()



# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1 
n = int(input("Enter a number:"))
for i in range(n,0,-1):
    num=i
    for j in range(i):
        print(num,end=" ")
        num-=1
    print()



# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
n = int(input("Enter a number:"))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()



# A 
# B B 
# C C C 
# D D D D 
# E E E E E 
n = int(input("Enter a number:"))
alpha = "A"
for i in range(n):
    for j in range(i+1):
        print(alpha,end=" ")
    alpha = chr(ord(alpha) + 1)
    print()



# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
n = int(input("Enter a number:"))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()



# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 
n = int(input("Enter a number:"))
for i in range(n,0,-1):
    for j in range(i):
        print(j+1,end=" ")
    print()




#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 
n = int(input("Enter a number:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()



#         1 
#       2 3 2 
#     3 4 5 4 3 
#   4 5 6 7 6 5 4 
# 5 6 7 8 9 8 7 6 5 
n = int(input("Enter a number:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(i+1):
        print(k+i+1,end=" ")
    for l in range(i,0,-1):
        print(l+i,end=" ")
    print()



# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 
n = int(input("Enter a number:"))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()



#         1   
#       1   1   
#     1   2   1   
#   1   3   3   1   
# 1   4   6   4   1   
n = int(input("Enter a number:"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    temp=1
    print(temp,end=" "*3)
    for k in range(1,i):
        temp = (temp*(i-k))//k
        print(temp,end=" "*3)
    print()



# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
n = int(input("Enter a number:"))
num=1
for i in range(n):
    for j in range(i+1):
        print(num,end=" ")
        num+=1
    print()



# Spiral
# 1    2    3    4
# 12   13   14   5
# 11   16   15   6
# 10   9    8    7

n = int(input("Enter a number: "))
matrix = [[0] * n for _ in range(n)]

left, right = 0, n - 1
up, down = 0, n - 1
# Here up,down is indicating row; right,left is indicating column
num = 1

while num <= n**2:
    for i in range(left, right + 1):
        matrix[up][i] = num
        num += 1
    up += 1 

    for i in range(up, down + 1):
        matrix[i][right] = num
        num += 1
    right -= 1 

    for i in range(right, left - 1, -1):
        matrix[down][i] = num
        num += 1
    down -= 1

    for i in range(down, up - 1, -1):
        matrix[i][left] = num
        num += 1
    left += 1

for row in matrix:
    for element in row:
        print(f"{element:<4}", end="")
    print()


# Diamond [not in sequence based on lines like 5 line mateers but continuous number of star in each line doesn't matter.]
#   *
# * * *
#   *
n = int(input("Enter a number:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()

for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()


# Sequience diamond line 1* then 2* then 3* end so on.
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
n = int(input("Enter a number:"))
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)





# *******
# *** ***
# **   **
# *     *
n = int(input("Enter a number:"))

print("*" * (2 * n - 1))

for i in range(n - 1, 0, -1):
    stars = "*" * i
    spaces = " " * (2 * (n - i) - 1)
    print(stars + spaces + stars)



# *     *
# **   **
# *** ***
# *******
n = int(input("Enter a number:"))

for i in range(1,n):
    print("*" * i,end="")
    print(" " * (2 * (n - i) - 1),end="")
    print("*" * i)

print("*" * (2 * n - 1))



# *******
# *** ***
# **   **
# *     *
# **   **
# *** ***
# *******
n = int(input("Enter a number:"))

print("*" * (2 * n - 1))

for i in range(n - 1, 1, -1):
    print("*" * i,end="")
    print(" " * (2 * (n - i) - 1),end="")
    print("*" * i)

for i in range(1,n):
    print("*" * i,end="")
    print(" " * (2 * (n - i) - 1),end="")
    print("*" * i)

print("*" * (2 * n - 1))




#  *       *       *       
#   *     * *     * *
#    *   *   *   *   *
#     * *     * *     *
#      *       *       *       
n = int(input("Enter a number:"))

fspace=n + (n - 3)
mspace=-1
for i in range(1,n+1):
    if i==1:
        print(" "*i,end="")
        for j in range(3):
            print("*",end=" "*(n + (n - 3)))
        print()
        continue
    elif i==n:
        print(" "*(n),end="")
        for k in range(3):
            print("*",end=" "*(n + (n - 3)))
        print()
        continue
    else:
        print(" "*i,end="")
        print("*",end="")
        fspace-=2
        print(" "*fspace,end="")
        print("*",end="")
        mspace+=2
        print(" "*mspace,end="")
        print("*",end="")
        print(" "*fspace,end="")
        print("*",end="")
        print(" "*mspace,end="")
        print("*") 

print("Page title:", soup.title.get_text(strip=True)
      if soup.title else "No title")

for link in soup.find_all("a", href=True):
    print(link.get_text(strip=True), link["href"])
