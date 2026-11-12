
print("1. Character Count")
print("2. Character Stuffing")
print("3. Bit Stuffing")

choice = int(input("Enter choice: "))
data = input("Enter data: ")

frame = ""

if choice == 1:
    frame = str(len(data)) + data

elif choice == 2:
    frame = "F"

    for ch in data:
        if ch == 'F' or ch == 'E':
            frame += 'E'

        frame += ch

    frame += "F"

elif choice == 3:
    frame = "01111110"
    count = 0

    for bit in data:
        frame += bit

        if bit == '1':
            count += 1

            if count == 5:
                frame += '0'
                count = 0
        else:
            count = 0

    frame += "01111110"

else:
    print("Invalid choice")
    exit()

print("Framed Data:", frame)
