def main():
    dial: int = 50
    num_times_dial_zero: int = 0

    with open("../input.txt", "r") as file:
        lines: list[str] = file.read().strip().splitlines()

        for line in lines:
            direction: str = line[0]
            line_num: int = int(line[1:])

            if direction == "L":
                dial -= line_num
                dial = dial % -100 

            elif direction == "R":
                dial += line_num
                dial = dial % 100

            if dial == 0:
                num_times_dial_zero += 1

    print(num_times_dial_zero)


if __name__ == "__main__":
    main()
