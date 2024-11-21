
def convert(time):

    hours, minutes = time.split(":")
    minute = float(minutes) / 60
    return float(hours) + minute

def main():
    time = input('What time is it? ').strip()
    hours = convert(time)

    if 7 <= 8:
       print('breakfast time')
    elif 8 >= 12 <= 13:
       print('lunch time')
    elif 18 <= 19:
       print('dinner time')
    else:
       pass

if __name__ == '__main__':
 main()
