from TowerPuzzle import TowerPuzzle
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise RuntimeError("Wrong input\nRight input: {input filename} {output filename")

    input_name = sys.argv[1]
    output_name = sys.argv[2]
    input_file = open(input_name)
    size = int(input_file.readline()[:-1])
    visibility = []
    input_file.readline()
    for i in range(4):
        split_array = input_file.readline()[:-1].split(' ')
        if len(split_array) == 0:
            i -= 1
            continue
        row = []
        if split_array == ['']:
            raise RuntimeError("Wrong input: empty string")
        for number in split_array:
            row.append(int(number))
        visibility.append(row)

    field = []
    input_file.readline()
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
