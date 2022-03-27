import csv
import random
import unidecode


class Application:
    # Execute the read_csv function when the class is instantiated in main.py
    def __init__(self):
        self.data = []
        self.read_csv()

    # Read the csv file, set ';' and delimiter and save the data in the self.data list
    def read_csv(self):
        csv_file = open('br-capes-bolsistas-uab.csv', 'r')
        csv_delimited = csv.DictReader(csv_file, delimiter=";")
        for row in csv_delimited:
            self.data.append(row)
        csv_file.close()

    # Ask for an input and compare it to each year column of each row the self.data
    def search_one(self):
        selected_year = input("\nInforme o ano que deseja buscar o bolsista 0: ")

        for x in self.data:
            if x['AN_REFERENCIA'] == selected_year:
                print("Nome: ", x['NM_BOLSISTA'])
                print("cpf: ", x['CPF_BOLSISTA'])
                print("Entidade de ensino: ", x['NM_ENTIDADE_ENSINO'])
                print("Valor da bolsa: R$", x['VL_BOLSISTA_PAGAMENTO'])
                break
            # Execute the function again if the year couldn't be find
            if selected_year != '2016' and selected_year != '2015' and selected_year != '2014' \
                    and selected_year != '2013':
                print("Ano não disponivel, tente novamente.")
                self.search_one()

    def search_two(self):

        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                    'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']

        encoded_name = input("\nDigite o nome a ser codificado: ").upper()
        # Remove the accents
        encoded_name = unidecode.unidecode(encoded_name)
        name_list = []
        year = ''
        school = ''
        value = ''
        # Get each char and save it in a list. Shuffle the list
        for x in self.data:
            if x["NM_BOLSISTA"].startswith(encoded_name) or encoded_name == x['NM_BOLSISTA']:
                year = x['AN_REFERENCIA']
                school = x['NM_ENTIDADE_ENSINO']
                value = x['VL_BOLSISTA_PAGAMENTO']
                for letter in x['NM_BOLSISTA']:
                    if letter != " ":
                        name_list.append(letter)
                break

        random.shuffle(name_list)

        # Encrypt the list using the alphabet list
        cryp_list = []
        for letter in name_list:
            position = alphabet.index(letter) + 1
            cryp_list.append(alphabet[position])

        cryp_string = "".join([str(item) for item in cryp_list])
        print("Dados: ")
        print("Nome: ", cryp_string)
        print("Ano: ", year)
        print("Entidade de ensino: ", school)
        print("Valor da bolsa: ", value)

    # Ask for a year in the input and compare the input with each item of the year column. If it's the same, save every
    # value in a variable and divide it by the number of elements, getting the average.
    def search_three(self):

        selected_year = input("\nSelecione o ano para consultar a media de valor das bolsas: ")

        # Save the sum of the value of each element from the selected year
        media_sum = 0
        count = 0
        for x in self.data:
            if x['AN_REFERENCIA'] == selected_year:
                media_sum += int(x['VL_BOLSISTA_PAGAMENTO'])
                count += 1
            if selected_year != '2016' and selected_year != '2015' and selected_year != '2014'\
                    and selected_year != '2013':
                print("Ano não disponivel, tente novamente.")
                self.search_three()

        media = media_sum / count
        print("Média de valor das bolsas de", selected_year, "R$", round(media, 2))

    # Go through each scholarship value of the list, and if save it if it is equal to the highest and lowest possible
    # values, storing only the three first elements
    def search_four(self):

        biggest = []
        smallest = []
        countb = 1
        counts = 1

        for x in self.data:
            if x['VL_BOLSISTA_PAGAMENTO'] == '1500' and countb <= 3:
                biggest.append(x['NM_BOLSISTA'])
                biggest.append(x['VL_BOLSISTA_PAGAMENTO'])
                countb += 1
            if x['VL_BOLSISTA_PAGAMENTO'] == '765' and counts <= 3:
                smallest.append(x['NM_BOLSISTA'])
                smallest.append(x['VL_BOLSISTA_PAGAMENTO'])
                counts += 1

        print()
        print("MAIORES VALORES:")
        count = 0
        while count < len(biggest):
            print('Nome: ', biggest[count])
            count += 1
            print('Valor da bolsa: R$', biggest[count])
            count += 1
            print()

        print()

        print("MENORES VALORES:")
        count = 0
        while count < len(smallest):
            print('Nome: ', smallest[count])
            count += 1
            print('Valor da bolsa: R$', smallest[count])
            count += 1
            print()
