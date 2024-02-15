

file = "asgt_messages.txt"
counter = 0


open_file = open(file, "r")

readings = open_file.readline()
print(readings)
while readings != "":
    readings = readings.split()
    print(readings)
    length = len(readings)
    readings = open_file.readline()

open_file.close()


    # for i in range(length):
    #     if output_file_read[i] == "Simon":
    #         output_file.write(str(counter) + " Simon\n")
    #         counter += 1
