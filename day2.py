import enum


file_name = "day2-inputs.txt"


class Directions(enum.Enum):
    UP = "up"
    DOWN = "down"
    FORWARD = "forward"


# format the input
def get_formatted_inputs(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


# return the instruction
def get_instruction(command):
    return command.split()


# Solution to part 1
def calculate_positions(values):
    horizontal_position = 0
    depth_position = 0

    for value in values:
        instruction = get_instruction(value)

        if instruction[0] == Directions.FORWARD.value:
            horizontal_position += int(instruction[1])
        elif instruction[0] == Directions.UP.value:
            depth_position -= int(instruction[1])
        elif instruction[0] == Directions.DOWN.value:
            depth_position += int(instruction[1])

    return [horizontal_position, depth_position]


# Solution for part 2
def calculate_final_positions(values):
    horizontal_position = 0
    depth_position = 0
    aim = 0

    for value in values:
        instruction = get_instruction(value)

        if instruction[0] == Directions.FORWARD.value:
            horizontal_position += int(instruction[1])
            depth_position += aim * int(instruction[1])
        elif instruction[0] == Directions.UP.value:
            aim -= int(instruction[1])
        elif instruction[0] == Directions.DOWN.value:
            aim += int(instruction[1])

    return [horizontal_position, depth_position, aim]


[horizontal_position, depth_position] = calculate_positions(
    get_formatted_inputs(file_name))

[final_horizontal_position, final_depth_position,
    final_aim] = calculate_final_positions(get_formatted_inputs(file_name))

print("Part 1")
print("---------")
print("Horizontal position: " + str(horizontal_position))
print("Depth position: " + str(depth_position))
print("Multiplied value: " + str(horizontal_position * depth_position))
print("\n")
print("Part 2")
print("---------")
print("Final horizontal position: " + str(final_horizontal_position))
print("Final depth position: " + str(final_depth_position))
print("Final aim: " + str(final_aim))
print("Multiplied value: " + str(final_horizontal_position * final_depth_position))
