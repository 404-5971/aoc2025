def main():
    dial: int = 50
    num_times_dial_zero: int = 0
    with open("../input.txt", "r") as file:
        lines: list[str] = [line.strip() for line in file.readlines()]
        for line in lines:
            if line.startswith("L"):
                line = line[1:]
                for i in range(int(line)):
                    dial -= 1
                    if dial < 0:
                        dial = 99
            elif line.startswith("R"):
                line = line[1:]
                for i in range(int(line)):
                    dial += 1
                    if dial > 99:
                        dial = 0
            if dial == 0:
                num_times_dial_zero += 1

    print(num_times_dial_zero)


if __name__ == "__main__":
    main()
