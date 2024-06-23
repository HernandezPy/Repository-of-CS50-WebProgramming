
def convert(time):
    
    hours, minutes = map(int, time.split(':'))
    return hours + minutes / 60

def main():

    time = input("Enter the time in 24-hour format (HH:MM or H:MM): ").strip()

    hours = convert(time)

    if 7 <= hours <= 8:
        print("It's breakfast time.")
    elif 12 <= hours <= 13:
        print("It's lunch time.")
    elif 18 <= hours <= 19:
        print("It's dinner time.")

if __name__ == "__main__":
    main()
