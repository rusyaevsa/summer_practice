from Organizations.GeneratePrice.Entities.CoeffMarkets import CoeffMarkets


class CoeffSuperMarket(CoeffMarkets):
    def __init__(self):
        super().__init__()

    def _init_positions(self) -> dict[str, dict[str, dict[str, float]]]:
        return {
            "milk": self.__milk_positions(),
            "bread": self.__bread_positions(),
            "grocery": self.__grocery_positions(),
            "crackers": self.__crackers_positions(),
            "chips": self.__chips_positions(),
            "lemonade": self.__lemonade_positions(),
            "washing": self.__washing_positions(),
            "soap": self.__soap_positions(),
            "dishwashing": self.__dishwashing_positions()
        }

    def __milk_positions(self) -> dict[str, dict[str, float]]:
        return {
            "Стерлядка": {"Молоко": 0.95, "Наше": 0.95, "Деревня": 0.95, "Коровино": 0.95, "Ферма": 1.0},
            "Горький": {"Молоко": 0.95, "Наше": 0.95, "Деревня": 0.95, "Коровино": 0.95, "Ферма": 1.0},
            "Столичный": {"Молоко": 0.95, "Наше": 0.95, "Деревня": 0.95, "Коровино": 0.95, "Ферма": 1.0},
            "Нева-маркет": {"Молоко": 0.95, "Наше": 0.95, "Деревня": 0.95, "Коровино": 0.95, "Ферма": 1.0},
            "Машук": {"Молоко": 0.95, "Наше": 0.95, "Деревня": 0.95, "Коровино": 0.95, "Ферма": 1.0},
            "Курортные продукты": {"Молоко": 0.95, "Наше": 0.95, "Деревня": 0.95, "Коровино": 0.95, "Ферма": 1.0},
            "Суровые продукты": {"Молоко": 0.95, "Наше": 0.95, "Деревня": 0.95, "Коровино": 0.95, "Ферма": 1.0},
            "Уралочка": {"Молоко": 0.95, "Наше": 0.95, "Деревня": 0.95, "Коровино": 0.95, "Ферма": 1.0},
            "Снежное": {"Молоко": 0.95, "Наше": 0.95, "Деревня": 0.95, "Коровино": 0.95, "Ферма": 1.0},
            "Сибирская щедрость": {"Молоко": 0.95, "Наше": 0.95, "Деревня": 0.95, "Коровино": 0.95, "Ферма": 1.0},
            "Дальневосточное море": {"Молоко": 0.95, "Наше": 0.95, "Деревня": 0.95, "Коровино": 0.95, "Ферма": 1.0},
            "Дальневосточный": {"Молоко": 0.95, "Наше": 0.95, "Деревня": 0.95, "Коровино": 0.95, "Ферма": 1.0},
            "У дома!": {"Молоко": 1.0, "Наше": 1.0, "Деревня": 1.0, "Коровино": 1.0},
            "Покупочка": {"Наше": 1.03, "Деревня": 1.03, "Коровино": 1.03, "Ферма": 1.03},
            "Дёшево!": {"Молоко": 0.9, "Наше": 0.9, "Деревня": 0.9, "Коровино": 0.9},
            "Дорого-Богато": {"Деревня": 1.2, "Коровино": 1.2, "Ферма": 1.2, "Nature": 1.2},
            "ГиперПрод": {"Молоко": 1.05, "Наше": 1.05, "Деревня": 1.05, "Коровино": 1.05, "Ферма": 1.05}
        }

    def __bread_positions(self) -> dict[str, dict[str, float]]:
        return {
            "Стерлядка": {"Просто хлеб": 0.95, "Местный": 0.95, "Деревня": 0.95, "Мельница": 0.95, "Тонус": 0.95},
            "Горький": {"Просто хлеб": 0.95, "Местный": 0.95, "Деревня": 0.95, "Мельница": 0.95, "Тонус": 0.95},
            "Столичный": {"Просто хлеб": 0.95, "Местный": 0.95, "Деревня": 0.95, "Мельница": 0.95, "Тонус": 0.95},
            "Нева-маркет": {"Просто хлеб": 0.95, "Местный": 0.95, "Деревня": 0.95, "Мельница": 0.95, "Тонус": 0.95},
            "Машук": {"Просто хлеб": 0.95, "Местный": 0.95, "Деревня": 0.95, "Мельница": 0.95, "Тонус": 0.95},
            "Курортные продукты": {"Просто хлеб": 0.95, "Местный": 0.95, "Деревня": 0.95, "Мельница": 0.95, "Тонус": 0.95},
            "Суровые продукты": {"Просто хлеб": 0.95, "Местный": 0.95, "Деревня": 0.95, "Мельница": 0.95, "Тонус": 0.95},
            "Уралочка": {"Просто хлеб": 0.95, "Местный": 0.95, "Деревня": 0.95, "Мельница": 0.95, "Тонус": 0.95},
            "Снежное": {"Просто хлеб": 0.95, "Местный": 0.95, "Деревня": 0.95, "Мельница": 0.95, "Тонус": 0.95},
            "Сибирская щедрость": {"Просто хлеб": 0.95, "Местный": 0.95, "Деревня": 0.95, "Мельница": 0.95, "Тонус": 0.95},
            "Дальневосточное море": {"Просто хлеб": 0.95, "Местный": 0.95, "Деревня": 0.95, "Мельница": 0.95, "Тонус": 0.95},
            "Дальневосточный": {"Просто хлеб": 0.95, "Местный": 0.95, "Деревня": 0.95, "Мельница": 0.95, "Тонус": 0.95},
            "У дома!": {"Просто хлеб": 1.0, "Местный": 1.0, "Деревня": 1.0, "Мельница": 1.0},
            "Покупочка": {"Местный": 1.05, "Деревня": 1.05, "Мельница": 1.05, "Тонус": 1.05},
            "Дёшево!": {"Просто хлеб": 0.8, "Местный": 0.8, "Деревня": 0.8, "Мельница": 0.8},
            "Дорого-Богато": {"Деревня": 1.2, "Мельница": 1.2, "Тонус": 1.2, "Эко": 1.2},
            "ГиперПрод": {"Просто хлеб": 1.05, "Местный": 1.05, "Деревня": 1.05, "Мельница": 1.05, "Тонус": 1.05}
        }

    def __grocery_positions(self) -> dict[str, dict[str, float]]:
        return {
            "Стерлядка": {"Гречка": 0.95, "Макароны": 0.95, "Рис": 0.95, "Чай": 0.95, "Кофе": 0.95, "Масло": 0.95},
            "Горький": {"Гречка": 0.95, "Макароны": 0.95, "Рис": 0.95, "Чай": 0.95, "Кофе": 0.95, "Масло": 0.95},
            "Столичный": {"Гречка": 0.95, "Макароны": 0.95, "Рис": 0.95, "Чай": 0.95, "Кофе": 0.95, "Масло": 0.95},
            "Нева-маркет": {"Гречка": 0.95, "Макароны": 0.95, "Рис": 0.95, "Чай": 0.95, "Кофе": 0.95, "Масло": 0.95},
            "Машук": {"Гречка": 0.95, "Макароны": 0.95, "Рис": 0.95, "Чай": 0.95, "Кофе": 0.95, "Масло": 0.95},
            "Курортные продукты": {"Гречка": 0.95, "Макароны": 0.95, "Рис": 0.95, "Чай": 0.95, "Кофе": 0.95, "Масло": 0.95},
            "Суровые продукты": {"Гречка": 0.95, "Макароны": 0.95, "Рис": 0.95, "Чай": 0.95, "Кофе": 0.95, "Масло": 0.95},
            "Уралочка": {"Гречка": 0.95, "Макароны": 0.95, "Рис": 0.95, "Чай": 0.95, "Кофе": 0.95, "Масло": 0.95},
            "Снежное": {"Гречка": 0.95, "Макароны": 0.95, "Рис": 0.95, "Чай": 0.95, "Кофе": 0.95, "Масло": 0.95},
            "Сибирская щедрость": {"Гречка": 0.95, "Макароны": 0.95, "Рис": 0.95, "Чай": 0.95, "Кофе": 0.95, "Масло": 0.95},
            "Дальневосточное море": {"Гречка": 0.95, "Макароны": 0.95, "Рис": 0.95, "Чай": 0.95, "Кофе": 0.95, "Масло": 0.95},
            "Дальневосточный": {"Гречка": 0.95, "Макароны": 0.95, "Рис": 0.95, "Чай": 0.95, "Кофе": 0.95, "Масло": 0.95},
            "У дома!": {"Гречка": 1.0, "Макароны": 1.0, "Рис": 1.0, "Чай": 1.0, "Кофе": 1.0, "Масло": 1.0},
            "Покупочка": {"Гречка": 1.01, "Макароны": 1.01, "Рис": 1.01, "Чай": 1.01, "Кофе": 1.01, "Масло": 1.01},
            "Дёшево!": {"Гречка": 0.7, "Макароны": 0.7, "Рис": 0.7, "Чай": 0.7, "Кофе": 0.7, "Масло": 0.7},
            "Дорого-Богато": {"Гречка": 1.2, "Рис": 1.2, "Чай": 1.2, "Кофе": 1.2, "Масло": 1.2},
            "ГиперПрод": {"Гречка": 1.04, "Макароны": 1.04, "Рис": 1.04, "Чай": 1.04, "Кофе": 1.04}
        }

    def __crackers_positions(self) -> dict[str, dict[str, float]]:
        return {
            "Стерлядка": {"4 корочки": 0.95, "Мягкие": 0.95, "Похрусteam": 0.95, "Хрустики": 0.95, "Suhariki": 1.0},
            "Горький": {"4 корочки": 0.95, "Мягкие": 0.95, "Похрусteam": 0.95, "Хрустики": 0.95, "Suhariki": 1.0},
            "Столичный": {"4 корочки": 0.95, "Мягкие": 0.95, "Похрусteam": 0.95, "Хрустики": 0.95, "Suhariki": 1.0},
            "Нева-маркет": {"4 корочки": 0.95, "Мягкие": 0.95, "Похрусteam": 0.95, "Хрустики": 0.95, "Suhariki": 1.0},
            "Машук": {"4 корочки": 0.95, "Мягкие": 0.95, "Похрусteam": 0.95, "Хрустики": 0.95, "Suhariki": 1.0},
            "Курортные продукты": {"4 корочки": 0.95, "Мягкие": 0.95, "Похрусteam": 0.95, "Хрустики": 0.95, "Suhariki": 1.0},
            "Суровые продукты": {"4 корочки": 0.95, "Мягкие": 0.95, "Похрусteam": 0.95, "Хрустики": 0.95, "Suhariki": 1.0},
            "Уралочка": {"4 корочки": 0.95, "Мягкие": 0.95, "Похрусteam": 0.95, "Хрустики": 0.95, "Suhariki": 1.0},
            "Снежное": {"4 корочки": 0.95, "Мягкие": 0.95, "Похрусteam": 0.95, "Хрустики": 0.95, "Suhariki": 1.0},
            "Сибирская щедрость": {"4 корочки": 0.95, "Мягкие": 0.95, "Похрусteam": 0.95, "Хрустики": 0.95, "Suhariki": 1.0},
            "Дальневосточное море": {"4 корочки": 0.95, "Мягкие": 0.95, "Похрусteam": 0.95, "Хрустики": 0.95, "Suhariki": 1.0},
            "Дальневосточный": {"4 корочки": 0.95, "Мягкие": 0.95, "Похрусteam": 0.95, "Хрустики": 0.95, "Suhariki": 1.0},
            "У дома!": {"4 корочки": 1.0, "Мягкие": 1.0, "Похрусteam": 1.0, "Хрустики": 1.0},
            "Покупочка": {"Мягкие": 1.1, "Похрусteam": 1.01, "Хрустики": 1.1, "Suhariki": 1.1},
            "Дёшево!": {"4 корочки": 0.9, "Мягкие": 0.9, "Похрусteam": 0.9},
            "Дорого-Богато": {"Похрусteam": 1.25, "Хрустики": 1.25, "Suhariki": 1.25, "Baget": 1.25},
            "ГиперПрод": {"4 корочки": 1.05, "Мягкие": 1.05, "Похрусteam": 1.05, "Хрустики": 1.05, "Suhariki": 1.05}
        }

    def __chips_positions(self) -> dict[str, dict[str, float]]:
        return {
            "Стерлядка": {"Бульба": 0.95, "Грация картошки": 0.95, "Leps": 0.95, "Potatos": 0.95, "Bringles": 0.95},
            "Горький": {"Бульба": 0.95, "Грация картошки": 0.95, "Leps": 0.95, "Potatos": 0.95, "Bringles": 0.95},
            "Столичный": {"Бульба": 0.95, "Грация картошки": 0.95, "Leps": 0.95, "Potatos": 0.95, "Bringles": 0.95},
            "Нева-маркет": {"Бульба": 0.95, "Грация картошки": 0.95, "Leps": 0.95, "Potatos": 0.95, "Bringles": 0.95},
            "Машук": {"Бульба": 0.95, "Грация картошки": 0.95, "Leps": 0.95, "Potatos": 0.95, "Bringles": 0.95},
            "Курортные продукты": {"Бульба": 0.95, "Грация картошки": 0.95, "Leps": 0.95, "Potatos": 0.95, "Bringles": 0.95},
            "Суровые продукты": {"Бульба": 0.95, "Грация картошки": 0.95, "Leps": 0.95, "Potatos": 0.95, "Bringles": 0.95},
            "Уралочка": {"Бульба": 0.95, "Грация картошки": 0.95, "Leps": 0.95, "Potatos": 0.95, "Bringles": 0.95},
            "Снежное": {"Бульба": 0.95, "Грация картошки": 0.95, "Leps": 0.95, "Potatos": 0.95, "Bringles": 0.95},
            "Сибирская щедрость": {"Бульба": 0.95, "Грация картошки": 0.95, "Leps": 0.95, "Potatos": 0.95, "Bringles": 0.95},
            "Дальневосточное море": {"Бульба": 0.95, "Грация картошки": 0.95, "Leps": 0.95, "Potatos": 0.95, "Bringles": 0.95},
            "Дальневосточный": {"Бульба": 0.95, "Грация картошки": 0.95, "Leps": 0.95, "Potatos": 0.95, "Bringles": 0.95},
            "У дома!": {"Бульба": 1.0, "Грация картошки": 1.0, "Leps": 1.0, "Potatos": 1.0},
            "Покупочка": {"Грация картошки": 1.05, "Leps": 1.05, "Potatos": 1.05, "Bringles": 1.05},
            "Дёшево!": {"Бульба": 0.8, "Грация картошки": 0.8, "Leps": 0.8, "Potatos": 0.8},
            "Дорого-Богато": {"Leps": 1.2, "Potatos": 1.2, "Bringles": 1.2, "VIP Chips": 1.2},
            "ГиперПрод": {"Бульба": 1.05, "Грация картошки": 1.05, "Leps": 1.05, "Potatos": 1.05, "Bringles": 1.05}
        }

    def __lemonade_positions(self) -> dict[str, dict[str, float]]:
        return {
            "Стерлядка": {"Чувака": 0.95, "Подарочный": 0.95, "Белоголовка": 0.95, "КМВ": 0.95, "Phanta": 0.95, "7down": 0.95},
            "Горький": {"Чувака": 0.95, "Подарочный": 0.95, "Белоголовка": 0.95, "КМВ": 0.95, "Phanta": 0.95, "7down": 0.95},
            "Столичный": {"Чувака": 0.95, "Подарочный": 0.95, "Белоголовка": 0.95, "КМВ": 0.95, "Phanta": 0.95, "7down": 0.95},
            "Нева-маркет": {"Чувака": 0.95, "Подарочный": 0.95, "Белоголовка": 0.95, "КМВ": 0.95, "Phanta": 0.95, "7down": 0.95},
            "Машук": {"Чувака": 0.95, "Подарочный": 0.95, "Белоголовка": 0.95, "КМВ": 0.95, "Phanta": 0.95, "7down": 0.95},
            "Курортные продукты": {"Чувака": 0.95, "Подарочный": 0.95, "Белоголовка": 0.95, "КМВ": 0.95, "Phanta": 0.95, "7down": 0.95},
            "Суровые продукты": {"Чувака": 0.95, "Подарочный": 0.95, "Белоголовка": 0.95, "КМВ": 0.95, "Phanta": 0.95, "7down": 0.95},
            "Уралочка": {"Чувака": 0.95, "Подарочный": 0.95, "Белоголовка": 0.95, "КМВ": 0.95, "Phanta": 0.95, "7down": 0.95},
            "Снежное": {"Чувака": 0.95, "Подарочный": 0.95, "Белоголовка": 0.95, "КМВ": 0.95, "Phanta": 0.95, "7down": 0.95},
            "Сибирская щедрость": {"Чувака": 0.95, "Подарочный": 0.95, "Белоголовка": 0.95, "КМВ": 0.95, "Phanta": 0.95, "7down": 0.95},
            "Дальневосточное море": {"Чувака": 0.95, "Подарочный": 0.95, "Белоголовка": 0.95, "КМВ": 0.95, "Phanta": 0.95, "7down": 0.95},
            "Дальневосточный": {"Чувака": 0.95, "Подарочный": 0.95, "Белоголовка": 0.95, "КМВ": 0.95, "Phanta": 0.95, "7down": 0.95},
            "У дома!": {"Чувака": 1.0, "Подарочный": 1.0, "Белоголовка": 1.0, "КМВ": 1.0, "Phanta": 1.0, "7down": 1.0},
            "Покупочка": {"Чувака": 1.05, "Подарочный": 1.05, "Белоголовка": 1.05, "КМВ": 1.05, "Phanta": 1.05, "7down": 1.05},
            "Дёшево!": {"Чувака": 0.7, "Подарочный": 0.7, "Белоголовка": 0.7, "КМВ": 0.7, "Phanta": 0.7, "7down": 0.7},
            "Дорого-Богато": {"Чувака": 1.2, "Белоголовка": 1.2, "КМВ": 1.2, "Phanta": 1.2, "7down": 1.2},
            "ГиперПрод": {"Чувака": 1.04, "Подарочный": 1.04, "Белоголовка": 1.04, "КМВ": 1.04, "Phanta": 1.04}
        }

    def __washing_positions(self) -> dict[str, dict[str, float]]:
        return {
            "Стерлядка": {"Зайчик": 0.95, "Стирка++": 0.95, "Мерсил": 0.95, "Гайд": 0.95, "Purity": 1.0},
            "Горький": {"Зайчик": 0.95, "Стирка++": 0.95, "Мерсил": 0.95, "Гайд": 0.95, "Purity": 1.0},
            "Столичный": {"Зайчик": 0.95, "Стирка++": 0.95, "Мерсил": 0.95, "Гайд": 0.95, "Purity": 1.0},
            "Нева-маркет": {"Зайчик": 0.95, "Стирка++": 0.95, "Мерсил": 0.95, "Гайд": 0.95, "Purity": 1.0},
            "Машук": {"Зайчик": 0.95, "Стирка++": 0.95, "Мерсил": 0.95, "Гайд": 0.95, "Purity": 1.0},
            "Курортные продукты": {"Зайчик": 0.95, "Стирка++": 0.95, "Мерсил": 0.95, "Гайд": 0.95, "Purity": 1.0},
            "Суровые продукты": {"Зайчик": 0.95, "Стирка++": 0.95, "Мерсил": 0.95, "Гайд": 0.95, "Purity": 1.0},
            "Уралочка": {"Зайчик": 0.95, "Стирка++": 0.95, "Мерсил": 0.95, "Гайд": 0.95, "Purity": 1.0},
            "Снежное": {"Зайчик": 0.95, "Стирка++": 0.95, "Мерсил": 0.95, "Гайд": 0.95, "Purity": 1.0},
            "Сибирская щедрость": {"Зайчик": 0.95, "Стирка++": 0.95, "Мерсил": 0.95, "Гайд": 0.95, "Purity": 1.0},
            "Дальневосточное море": {"Зайчик": 0.95, "Стирка++": 0.95, "Мерсил": 0.95, "Гайд": 0.95, "Purity": 1.0},
            "Дальневосточный": {"Зайчик": 0.95, "Стирка++": 0.95, "Мерсил": 0.95, "Гайд": 0.95, "Purity": 1.0},
            "У дома!": {"Зайчик": 1.0, "Стирка++": 1.0, "Мерсил": 1.0, "Гайд": 1.0},
            "Покупочка": {"Стирка++": 1.03, "Мерсил": 1.03, "Гайд": 1.03, "Purity": 1.03},
            "Дёшево!": {"Зайчик": 0.9, "Стирка++": 0.9, "Мерсил": 0.9, "Гайд": 0.9},
            "Дорого-Богато": {"Мерсил": 1.2, "Гайд": 1.2, "Purity": 1.2, "Cleanliness": 1.2},
            "ГиперПрод": {"Зайчик": 1.05, "Стирка++": 1.05, "Мерсил": 1.05, "Гайд": 1.05, "Purity": 1.05}
        }

    def __soap_positions(self) -> dict[str, dict[str, float]]:
        return {
            "Стерлядка": {"Хозяйственное": 0.95, "Душистое": 0.95, "Лав": 0.95, "Зелёная линия": 0.95, "Tenderness": 0.95},
            "Горький": {"Хозяйственное": 0.95, "Душистое": 0.95, "Лав": 0.95, "Зелёная линия": 0.95, "Tenderness": 0.95},
            "Столичный": {"Хозяйственное": 0.95, "Душистое": 0.95, "Лав": 0.95, "Зелёная линия": 0.95, "Tenderness": 0.95},
            "Нева-маркет": {"Хозяйственное": 0.95, "Душистое": 0.95, "Лав": 0.95, "Зелёная линия": 0.95, "Tenderness": 0.95},
            "Машук": {"Хозяйственное": 0.95, "Душистое": 0.95, "Лав": 0.95, "Зелёная линия": 0.95, "Tenderness": 0.95},
            "Курортные продукты": {"Хозяйственное": 0.95, "Душистое": 0.95, "Лав": 0.95, "Зелёная линия": 0.95, "Tenderness": 0.95},
            "Суровые продукты": {"Хозяйственное": 0.95, "Душистое": 0.95, "Лав": 0.95, "Зелёная линия": 0.95, "Tenderness": 0.95},
            "Уралочка": {"Хозяйственное": 0.95, "Душистое": 0.95, "Лав": 0.95, "Зелёная линия": 0.95, "Tenderness": 0.95},
            "Снежное": {"Хозяйственное": 0.95, "Душистое": 0.95, "Лав": 0.95, "Зелёная линия": 0.95, "Tenderness": 0.95},
            "Сибирская щедрость": {"Хозяйственное": 0.95, "Душистое": 0.95, "Лав": 0.95, "Зелёная линия": 0.95, "Tenderness": 0.95},
            "Дальневосточное море": {"Хозяйственное": 0.95, "Душистое": 0.95, "Лав": 0.95, "Зелёная линия": 0.95, "Tenderness": 0.95},
            "Дальневосточный": {"Хозяйственное": 0.95, "Душистое": 0.95, "Лав": 0.95, "Зелёная линия": 0.95, "Tenderness": 0.95},
            "У дома!": {"Хозяйственное": 1.0, "Душистое": 1.0, "Лав": 1.0, "Зелёная линия": 1.0},
            "Покупочка": {"Душистое": 1.05, "Лав": 1.05, "Зелёная линия": 1.05, "Tenderness": 1.05},
            "Дёшево!": {"Хозяйственное": 0.8, "Душистое": 0.8, "Лав": 0.8, "Зелёная линия": 0.8},
            "Дорого-Богато": {"Лав": 1.2, "Зелёная линия": 1.2, "Tenderness": 1.2, "Lovely": 1.2},
            "ГиперПрод": {"Хозяйственное": 1.05, "Душистое": 1.05, "Лав": 1.05, "Зелёная линия": 1.05, "Tenderness": 1.05}
        }

    def __dishwashing_positions(self) -> dict[str, dict[str, float]]:
        return {
            "Стерлядка": {"Чистюля": 0.95, "Тарелочкин": 0.95, "Perry": 0.95, "OAS": 0.95, "Shine": 0.95, "Brilliant": 0.95},
            "Горький": {"Чистюля": 0.95, "Тарелочкин": 0.95, "Perry": 0.95, "OAS": 0.95, "Shine": 0.95, "Brilliant": 0.95},
            "Столичный": {"Чистюля": 0.95, "Тарелочкин": 0.95, "Perry": 0.95, "OAS": 0.95, "Shine": 0.95, "Brilliant": 0.95},
            "Нева-маркет": {"Чистюля": 0.95, "Тарелочкин": 0.95, "Perry": 0.95, "OAS": 0.95, "Shine": 0.95, "Brilliant": 0.95},
            "Машук": {"Чистюля": 0.95, "Тарелочкин": 0.95, "Perry": 0.95, "OAS": 0.95, "Shine": 0.95, "Brilliant": 0.95},
            "Курортные продукты": {"Чистюля": 0.95, "Тарелочкин": 0.95, "Perry": 0.95, "OAS": 0.95, "Shine": 0.95, "Brilliant": 0.95},
            "Суровые продукты": {"Чистюля": 0.95, "Тарелочкин": 0.95, "Perry": 0.95, "OAS": 0.95, "Shine": 0.95, "Brilliant": 0.95},
            "Уралочка": {"Чистюля": 0.95, "Тарелочкин": 0.95, "Perry": 0.95, "OAS": 0.95, "Shine": 0.95, "Brilliant": 0.95},
            "Снежное": {"Чистюля": 0.95, "Тарелочкин": 0.95, "Perry": 0.95, "OAS": 0.95, "Shine": 0.95, "Brilliant": 0.95},
            "Сибирская щедрость": {"Чистюля": 0.95, "Тарелочкин": 0.95, "Perry": 0.95, "OAS": 0.95, "Shine": 0.95, "Brilliant": 0.95},
            "Дальневосточное море": {"Чистюля": 0.95, "Тарелочкин": 0.95, "Perry": 0.95, "OAS": 0.95, "Shine": 0.95, "Brilliant": 0.95},
            "Дальневосточный": {"Чистюля": 0.95, "Тарелочкин": 0.95, "Perry": 0.95, "OAS": 0.95, "Shine": 0.95, "Brilliant": 0.95},
            "У дома!": {"Чистюля": 1.0, "Тарелочкин": 1.0, "Perry": 1.0, "OAS": 1.0, "Shine": 1.0, "Brilliant": 1.0},
            "Покупочка": {"Чистюля": 1.05, "Тарелочкин": 1.05, "Perry": 1.05, "OAS": 1.05, "Shine": 1.05, "Brilliant": 1.05},
            "Дёшево!": {"Чистюля": 0.7, "Тарелочкин": 0.7, "Perry": 0.7, "OAS": 0.7, "Shine": 0.7, "Brilliant": 0.7},
            "Дорого-Богато": {"Чистюля": 1.2, "Perry": 1.2, "OAS": 1.2, "Shine": 1.2, "Brilliant": 1.2},
            "ГиперПрод": {"Чистюля": 1.04, "Тарелочкин": 1.04, "Perry": 1.04, "OAS": 1.04, "Shine": 1.04}
        }
