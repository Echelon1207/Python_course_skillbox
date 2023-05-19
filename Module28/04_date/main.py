class Date:

    @classmethod
    def from_string(cls,str_data):
        data = str_data.split('-')
        return f'День: {data[0]} Месяц: {data[1]} Год: {data[2]}'

    @classmethod
    def is_date_valid(cls,str_data):
        data = str_data.split('-')
        if int(data[0]) <= 0 or int(data[0]) > 31 or len(data[0]) != 2:
            return False
        elif int(data[1]) <= 0 or int(data[1]) > 12 or len(data[1]) != 2:
            return False
        elif int(data[2]) <= 0 or len(data[2]) != 4:
            return False
        return True


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
