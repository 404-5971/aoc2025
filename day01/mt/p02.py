def main():
    dial: int = 50
    num_times_dial_zero: int = 0

    with open("../input.txt", "r") as file:
        lines: list[str] = file.read().strip().splitlines()

        for line in lines:
            direction: str = line[0]
            distance: int = int(line[1:])
            start_groups = dial // 100

            if direction == "L":
                dial -= distance
            else:
                dial += distance

            end_groups = dial // 100

            num_times_dial_zero += abs(end_groups - start_groups)


    print(num_times_dial_zero)


if __name__ == "__main__":
    main()

