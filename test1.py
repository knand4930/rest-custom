
table = ["", "", "abc", "def", "ghi", "jkl","mno", "pqrs", "tuv", "wxyz", "", ""]

def data(number, current, output, n):
    if(current == n):
        print((output))

        return
 
  
    for i in range(len(table[number[current]])):
        output.append(table[number[current]][i])
        data(number, current + 1, output, n)
        output.pop()
        if(number[current] == 0 or number[current] == 1):
            return

 
def printWords(number, n):
    data(number, 0, [], n)
 
 
if __name__ == '__main__':
    number = [2, 3, 4]
    n = len(number)
    printWords(number, n)
 
