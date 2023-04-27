def main():
    num = int(input("Enter a number to generate multiplication table: "))

    output = ""

    format = int(input("Enter the desired the table format (1 for single, 2 for up to): "))

    if format not in [1, 2]:
        print("Invalid response.")
        return

    if format == 1:
        for j in range(1, 11):
            output += str(num) + " x " + str(j) + " = " + str(num * j) + "\n"

        output += "\n"
    else:
        for i in range(1, num + 1):
            for j in range(1, 11):
                output += str(i) + " x " + str(j) + " = " + str(i * j) + "\n"

            output += "\n"

    print(output)

    save_file = input("Do you want to save the table to a file? (y, n): ")

    save_file = save_file.lower()

    if save_file not in ["y", "n"]:
        print("Invalid response.")
        return

    file_name = input("Enter the desired file name: ")

    if save_file == "y":
        file = open(f'{file_name}.txt', 'w')

        file.write(output)
        file.close()
    else:
        return

if __name__ == "__main__":
    main()
