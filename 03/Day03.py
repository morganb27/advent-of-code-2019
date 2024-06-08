import fileinput

def manhattan_distance():
    coordinates1, _ = coordinates(WIRE1)
    coordinates2, _ = coordinates(WIRE2)
    common_coordinates = coordinates1 & coordinates2
    return min(common_coordinates, key= lambda x: (abs(x[0]) + abs(x[1])))

def manhattan_distance_part_two():
    shortest_path = float("inf")
    coordinates1, ints1 = coordinates(WIRE1)
    coordinates2, ints2 = coordinates(WIRE2)
    common_coordinates = coordinates1 & coordinates2
    for cmn in common_coordinates:
        if ints1[cmn] + ints2[cmn] < shortest_path:
            shortest_path = ints1[cmn] + ints2[cmn]
    return shortest_path


def coordinates(wire):
    x, y = 0, 0
    steps = 0
    ints = {}
    coordinates = set()
    instructions = wire.split(',')
    for instruction in instructions:
        direction, distance = instruction[0], int(instruction[1:])
        for _ in range(distance):
            if direction == 'U':
                y+=1
            elif direction == 'R':
                x+=1
            elif direction == 'D':
                y-=1
            elif direction == 'L':
                x-=1
            steps += 1
            coordinates.add((x, y))
            if (x, y) not in ints:
                ints[(x, y)] = steps
    return coordinates, ints

WIRES = [line.strip() for line in fileinput.input()]
WIRE1, WIRE2 = WIRES[0], WIRES[1]
print(manhattan_distance())
print(manhattan_distance_part_two())