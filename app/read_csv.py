import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader) #AL SER UN ITERABLE NOS PUEDE DEVOLVER LA PRIMERA FILA
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dic = {key: value for key, value in iterable}
      data.append(country_dic)
    return data
      # print(country_dic)
      # print('*****' * 5)
      # print(row)
  


if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[1])
