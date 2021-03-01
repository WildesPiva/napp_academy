from datetime import datetime

def calc_idade(data):
  current_date = datetime.today().date()
  data_nasc = datetime.strptime(data,'%d/%m/%Y').date()

  idade = current_date.year - data_nasc.year
  happy_date = data_nasc.replace(year=current_date.year)
  dias = 365 - abs(current_date - happy_date).days

  if current_date > happy_date:
    dias = abs(happy_date - current_date).days
  else:
    idade -= 1

  return idade, dias

if __name__ == "__main__":
  idade, dias_ano_atual = calc_idade('13/11/1999')
  print(f'{idade} anos e {dias_ano_atual} dias')
