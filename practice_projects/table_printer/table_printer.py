# The table that's going to printed
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'mouse', 'goose']]


def find_width(table):
    """Finds the maximum char width of each column.

    Args:
        table (list): The table that contains the columns.
    """
    colWidth = []
    for i in range(len(table)):
        colWidth.append(len(max(table[i], key=len)))

    return colWidth


def print_table(table):
    """Prints the table.

    Args:
        table (list): The table that's going to be printed.
    """
    colW = find_width(table)
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(colW[j])+" ", end='')
        print()


print_table(tableData)
