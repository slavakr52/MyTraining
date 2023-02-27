class Car:

    def __init__(self, brand: str, model: str, year: int, horse_power: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.horse_power = horse_power

    def __repr__(self):
        return f'Автомобиль {self.brand} {self.model}, {self.year} года выпуска, мощность {self.horse_power} л.с.'
    
    def save_car(self):
        cars_dict = {}
        cars_dict['brand'] = self.brand
        cars_dict['model'] = self.model
        cars_dict['year'] = self.year
        cars_dict['horse_power'] = self.horse_power
        
        data = []
        data.append(';'.join(cars_dict.values()))
        data = '\n'.join(data)
        with open('cars_book.txt', 'a', encoding='UTF-8') as file:
            file.write('\n')
            file.write(data)

    
def new_car_input():
    brand = input('Введите название авто: ')
    model = input('Введите модель авто: ')
    year = input('Введите год авто=: ')
    horse_power = input('Введите мощность авто (л.с.): ')
    new_car = Car(f'{brand}', f'{model}', f'{year}', f'{horse_power}')
    new_car.save_car()

new_car_input()




