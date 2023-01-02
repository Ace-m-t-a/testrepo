tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]



def printTable(lst):
    colWidths = [0] * len(tableData)
    for x in range(len(lst) + 1):
        for y in range(len(lst)):
                print(lst[y][x], end=" ")
        print()

printTable(tableData)