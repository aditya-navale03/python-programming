import sys
import os
import platform

def beep():
    system = platform.system().lower()
    if system == "windows":
        import winsound
        winsound.Beep(1000, 500)  # Beep at 1000 Hz for 500 milliseconds
    elif system in ["linux", "darwin"]:  # Linux or macOS
        sys.stdout.write('\a')
        sys.stdout.flush()

# Example usage
beep()

number = int(input("Enter the number: "))

def logic():
    for i in range(1, 11):
        table = number * i
        print("{} X {} = {}".format(number, i, table))
        beep()  # Adding beep after each line

# Call the logic function
logic()
