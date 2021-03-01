from datetime import datetime, timedelta

def future():
  current_date = datetime.today()
  return current_date + timedelta(weeks=2, days=3)

if __name__ == "__main__":
  future_date = future()
  print(f'{future_date:%d/%m/%Y %H:%M:%S}')