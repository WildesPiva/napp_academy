from datetime import datetime, timedelta

def calc_total_days(data):

  data = datetime.strptime(data,'%d/%m/%Y').date()

  days_7_1 = abs(data - datetime.today().date())
  
  return days_7_1.days

if __name__ == "__main__":
  dias = calc_total_days('08/07/2014')
  print(f'{dias} dias desde o 7 X 1.')
