def convert_date(date_str):
    # Define month mapping
   MONTHS = {
       'January': '01',
       'February': '02',
       'March': '03',
       'April': '04',
       'May': '05',
       'June': '06',
       'July': '07',
       'August': '08',
       'September': '09',
       'October': '10',
       'November': '11',
       'December': '12'
   }
   # Try to split the date by slashes
   try:
        month, day, year = date_str.split('/')
        month = month.zfill(2)  # ensure the month has two digits
        day = day.zfill(2)  # ensure the day has two digits
   except ValueError:
       # if slashes are not present, try splitting by spaces
        raise ValueError('Date format is incorrect')
   return f'{year}-{month}-{day}'


def main():
    date_str = input('Date: ')
    try:
        formatted_date = convert_date(date_str)
        print('ISO 8601 formatted date:', formatted_date)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
