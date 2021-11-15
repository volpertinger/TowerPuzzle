from TowerPuzzle import TowerPuzzle
import sys

if __name__ == '__main__':
    # visibility = [[2, 1, 2, 3], [2, 3, 3, 1], [1, 2, 3, 2], [2, 2, 1, 4]]
    # visibility = [[2, 2, 1, 4], [3, 2, 1, 2], [2, 3, 3, 1], [2, 3, 2, 1]]
    # visibility = [[1, 3, 3, 2, 2], [1, 4, 2, 3, 2], [3, 1, 2, 2, 2], [2, 2, 1, 3, 3]]
    # visibility = [[2, 1, 3, 3, 2], [2, 3, 1, 3, 3], [2, 2, 1, 2, 3], [4, 1, 4, 2, 2]]
    # visibility = [[3, 2, 5, 3, 1, 2], [3, 2, 4, 1, 2, 4], [3, 3, 2, 1, 4, 2], [2, 3, 1, 3, 3, 2]]
    # field = [[0, 4, 2, 0, 0, 0], [0, 0, 4, 0, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
    #         [0, 1, 0, 0, 0, 5]]
    # field = TowerPuzzle.get_field_from_array(field)
    # ss = TowerPuzzle(visibility, field)
    # ss.solve()
    # print(str(ss))

    if len(sys.argv) != 3:
        raise RuntimeError("Wrong input\nRight input: {input filename} {output filename")

    input_name = sys.argv[1]
    output_name = sys.argv[2]
    input_file = open(input_name)
    size = int(input_file.readline()[:-1])
    visibility = []
    for i in range(size):
        split_array = input_file.readline()[:-1].split(' ')
        row = []
        if split_array == ['']:
            raise RuntimeError("Wrong input: empty string")
        for number in split_array:
            row.append(int(number))
        visibility.append(row)

    field = []
    for i in range(size):
        split_array = input_file.readline()[:-1].split(' ')
        row = []
        if split_array == [''] and field != []:
            raise RuntimeError("Wrong input: empty string")
        if split_array == ['']:
            break
        for number in split_array:
            row.append(int(number))
        field.append(row)

    input_file.close()
    field = TowerPuzzle.get_field_from_array(field)

    if field:
        tower_puzzle = TowerPuzzle(visibility, field)
        tower_puzzle.solve()
        output = open(output_name, 'w')
        output.write(tower_puzzle.get_field_string())
        output.close()

    else:
        tower_puzzle = TowerPuzzle(visibility)
        tower_puzzle.solve()
        output = open(output_name, 'w')
        output.write(tower_puzzle.get_field_string())
        output.close()
