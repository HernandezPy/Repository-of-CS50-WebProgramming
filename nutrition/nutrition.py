fruits_calories = {

    'Apple': 130,
    'Avocado': 50,
    'Bananas': 110,
    'Cantaloupe': 50,
    'Grapefruit': 60,
    'Grapes': 90,
    'Honeydew Melon': 50,
    'Kiwifruit': 90,
    'Lemon': 15,
    'Nectarine': 60,
    'Orenge': 80,
    'Peach': 60,
    'Pear': 100,
    'Plums': 70,
    'Strawberries': 50,
    'Sweet Cherries': 100,
    'Tangerine': 50,
    'Watermelon': 80

  }

def main():
    fruit = input('Item: ').strip().title()
    if fruit in fruits_calories:
         print(f'Calories: {fruits_calories[fruit]}')
    else:
        pass

if __name__ == '__main__':
 main()

