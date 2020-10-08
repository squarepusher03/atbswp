# The table that's going to printed
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'mouse', 'goose']]

# Finds the max amount of chars in each column.
colWidth = []
for i in range(len(tableData)):
    colWidth.append(len(max(tableData[i], key=len)))

# Prints out each column.
for i in range(len(tableData[0])):
    for j in range(len(tableData)):
        print(tableData[j][i].rjust(colWidth[j])+" ", end='')
    print()
