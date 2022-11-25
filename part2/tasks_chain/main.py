# У вас есть список городов towns.
# Нужно написать функцию get_ids, 
# которая получит города только из Московской области,
# отсортирует их по названию и вернет список id. 
# На вход функция принимает список объектов towns, 
# на выходе функция должна возвращать список чисел (id) 

class Town:
    def __init__(self, id, name, region):
        self.id = id
        self.name = name
        self.region = region

    def __repr__(self):
        return f'{self.region} - {self.name}'


towns = [Town(1, 'Балашиха', 'МО'), Town(2, 'Химки', 'МО'), Town(3, 'Тула', 'Тульская область')]


def get_ids(towns):
    filter_mo = filter(lambda x: x.region == 'МО', towns)
    sorted_name = sorted(filter_mo, key=lambda x: x.name)
    map_id = map(lambda x: x.id, sorted_name)
    return list(map_id)

if __name__ == "__main__":
    print(get_ids(towns))
