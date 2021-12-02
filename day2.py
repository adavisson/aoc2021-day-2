import enum


file_name = "day2-inputs.txt"


class Directions(enum.Enum):
    UP = "up"
    DOWN = "down"
    FORWARD = "forward"


def get_formatted_inputs(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def get_instruction(command):
    return command.split()


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


[horizontal_position, depth_position] = calculate_positions(
    get_formatted_inputs(file_name))

print("Horizontal position: " + str(horizontal_position))
print("Depth position: " + str(depth_position))
print("Multiplied value: " + str(horizontal_position * depth_position))
