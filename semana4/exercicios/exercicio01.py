from datetime import datetime

def calc_total_days(data):

  data_nasc = datetime.strptime(data,'%d/%m/%Y').date()

  days_alive = abs(data_nasc - datetime.today().date())
  
  return days_alive.days

if __name__ == "__main__":
  
  dias = calc_total_days('13/11/1999')
  
  print(f'{dias} dias totais de vida.')
