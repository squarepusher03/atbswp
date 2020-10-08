# The table that's going to printed
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'mouse', 'goose']]

colWidth = []


def find_width(table):
    """Finds the maximum char width of each column.

    Args:
        table (list): The table that contains the columns.
    """
    for i in range(len(table)):
        colWidth.append(len(max(table[i], key=len)))


def print_table(table):
    """Prints the table.

    Args:
        table (list): The table that's going to be printed.
    """
    find_width(table)
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(colWidth[j])+" ", end='')
        print()


print_table(tableData)
