
def convert(time):

    hours, minutes = time.split(":")
    minute = float(minutes) / 60
    return float(hours) + minute

def main():
    time = input('What time is it? ').strip()
    hours = convert(time)

    if hours >= 7 and hours <= 8:
       print('breakfast time')
    elif hours >= 12 and hours <= 13:
       print('lunch time')
    elif hours >= 18 and hours <= 19:
       print('dinner time')
    else:
       pass

if __name__ == '__main__':
 main()
