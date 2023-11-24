def input_from_classificator(classificator: list, attribute_name: str):
    print("Choose " + attribute_name + "!")

    text = ""
    index = 0
    for element in classificator:
        text += str(index) + ' - ' + '"' + str(element) + '"'
        index += 1
        if index < len(classificator):
            text += ", "

    correct_input = False
    while not correct_input:
        action = input(f'{text}: ')
        try:
            action = int(action)
            if action < len(classificator):
                req_element = classificator[action]
                correct_input = True
                print(f'{attribute_name} = "{req_element}"')
            else:
                print("Incorrect answer")
        except ValueError:
            print("Incorrect answer")

    return req_element


seasons = ['summer', 'demi', 'winter', 'any']
item_classes = ['closes', 'shoes', 'accessories', 'other']
item_types = {'closes': ['pant', 'jeans', 'pullover', 'suit', 't-shirt', 'shirt', 'jacket', 'overall', 'hat', 'mittens',
                         'socks', 'underpants', 'pajamas', 'other'],
              'shoes': ['snickers', 'slippers', 'boots', 'sandals', 'clogs', 'high boots', 'rain boots', 'other'],
              'accessories': ['glasses', 'bag', 'headgear', 'other'],
              'other': ['other']}
colors = ['red', 'yellow', 'green', 'blue', 'white', 'black', 'multicolor', 'printed', 'brown', 'grey', 'pink',
          'orange', 'turquoise']
sizes = {'closes': ['98', '104', '110', '116', '98-104', '104-110', '110-116', '3T', '4T', '5T'],
         'shoes': ['25', '26', '27', '28', 'C9', 'C10', 'C11']}
brands = {'closes': ['lupilu', 'kik', 'H&M', 'C&A', 'carters', 'childrens place', 'input other'],
          'shoes': ['elefanten', 'kik', 'crocs', 'ecco', 'input other']}
