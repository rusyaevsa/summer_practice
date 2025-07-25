from Organizations.GeneratePrice.Entities.CoeffMarkets import CoeffMarkets


class CoeffPharmacyMarket(CoeffMarkets):
    def __init__(self):
        super().__init__()

    def _init_positions(self) -> dict[str, dict[str, dict[str, float]]]:
        return {
            "biologically_active": self.__biologically_active_positions(),
            "from_colds": self.__from_colds_positions(),
            "etc": self.__etc_positions()
        }

    def __biologically_active_positions(self) -> dict[str, dict[str, float]]:
        return {
            "Здоровье": {"Витаминки": 0.95, "Озверин": 0.95, "Витамин D": 0.95, "D3-формула": 0.95, "Ногтерост": 1.0},
            "Гиппократ": {"Витаминки": 0.95, "Озверин": 0.95, "Витамин D": 0.95, "D3-формула": 0.95, "Ногтерост": 1.0},
            "Кремлёвская": {"Витаминки": 0.95, "Озверин": 0.95, "Витамин D": 0.95, "D3-формула": 0.95, "Ногтерост": 1.0},
            "Аптеки у дома": {"Витаминки": 0.95, "Озверин": 0.95, "Витамин D": 0.95, "D3-формула": 0.95, "Ногтерост": 1.0},
            "Кавказское долголетие": {"Витаминки": 0.95, "Озверин": 0.95, "Витамин D": 0.95, "D3-формула": 0.95, "Ногтерост": 1.0},
            "Крымская здравница": {"Витаминки": 0.95, "Озверин": 0.95, "Витамин D": 0.95, "D3-формула": 0.95, "Ногтерост": 1.0},
            "Здравствуйте!": {"Витаминки": 0.95, "Озверин": 0.95, "Витамин D": 0.95, "D3-формула": 0.95, "Ногтерост": 1.0},
            "Богатырь": {"Витаминки": 0.95, "Озверин": 0.95, "Витамин D": 0.95, "D3-формула": 0.95, "Ногтерост": 1.0},
            "Кедр": {"Витаминки": 0.95, "Озверин": 0.95, "Витамин D": 0.95, "D3-формула": 0.95, "Ногтерост": 1.0},
            "Сибирь": {"Витаминки": 0.95, "Озверин": 0.95, "Витамин D": 0.95, "D3-формула": 0.95, "Ногтерост": 1.0},
            "Омега": {"Витаминки": 0.95, "Озверин": 0.95, "Витамин D": 0.95, "D3-формула": 0.95, "Ногтерост": 1.0},
            "Будь Здоров!": {"Витаминки": 0.95, "Озверин": 0.95, "Витамин D": 0.95, "D3-формула": 0.95, "Ногтерост": 1.0},
            "Молодость": {"Витаминки": 1.0, "Озверин": 1.0, "Витамин D": 1.0, "D3-формула": 1.0},
            "Таблетница": {"Озверин": 1.05, "Витамин D": 1.2, "D3-формула": 1.1, "Ногтерост": 1.1},
            "Аспирин": {"Витаминки": 0.9, "Озверин": 0.9, "Витамин D": 1.03},
            "36 и 6": {"Витамин D": 1.25, "D3-формула": 1.25, "Ногтерост": 1.25, "Волосила": 1.25},
            "120 на 80": {"Витаминки": 1.1, "Озверин": 1.1, "Витамин D": 1.05, "D3-формула": 1.05, "Ногтерост": 1.05}
        }

    def __from_colds_positions(self) -> dict[str, dict[str, float]]:
        return {
            "Здоровье": {"Мукалтин": 0.95, "Кашлевит": 0.95, "Ингасол": 0.95, "Ринофолт": 0.95, "Амперин": 0.95},
            "Гиппократ": {"Мукалтин": 0.95, "Кашлевит": 0.95, "Ингасол": 0.95, "Ринофолт": 0.95, "Амперин": 0.95},
            "Кремлёвская": {"Мукалтин": 0.95, "Кашлевит": 0.95, "Ингасол": 0.95, "Ринофолт": 0.95, "Амперин": 0.95},
            "Аптеки у дома": {"Мукалтин": 0.95, "Кашлевит": 0.95, "Ингасол": 0.95, "Ринофолт": 0.95, "Амперин": 0.95},
            "Кавказское долголетие": {"Мукалтин": 0.95, "Кашлевит": 0.95, "Ингасол": 0.95, "Ринофолт": 0.95, "Амперин": 0.95},
            "Крымская здравница": {"Мукалтин": 0.95, "Кашлевит": 0.95, "Ингасол": 0.95, "Ринофолт": 0.95, "Амперин": 0.95},
            "Здравствуйте!": {"Мукалтин": 0.95, "Кашлевит": 0.95, "Ингасол": 0.95, "Ринофолт": 0.95, "Амперин": 0.95},
            "Богатырь": {"Мукалтин": 0.95, "Кашлевит": 0.95, "Ингасол": 0.95, "Ринофолт": 0.95, "Амперин": 0.95},
            "Кедр": {"Мукалтин": 0.95, "Кашлевит": 0.95, "Ингасол": 0.95, "Ринофолт": 0.95, "Амперин": 0.95},
            "Сибирь": {"Мукалтин": 0.95, "Кашлевит": 0.95, "Ингасол": 0.95, "Ринофолт": 0.95, "Амперин": 0.95},
            "Омега": {"Мукалтин": 0.95, "Кашлевит": 0.95, "Ингасол": 0.95, "Ринофолт": 0.95, "Амперин": 0.95},
            "Будь Здоров!": {"Мукалтин": 0.95, "Кашлевит": 0.95, "Ингасол": 0.95, "Ринофолт": 0.95, "Амперин": 0.95},
            "Молодость": {"Мукалтин": 1.0, "Кашлевит": 1.0, "Ингасол": 1.0, "Ринофолт": 1.0},
            "Таблетница": {"Кашлевит": 1.05, "Ингасол": 1.05, "Ринофолт": 1.05, "Амперин": 1.05},
            "Аспирин": {"Мукалтин": 0.8, "Кашлевит": 0.8, "Ингасол": 0.8, "Ринофолт": 0.8},
            "36 и 6": {"Ингасол": 1.2, "Ринофолт": 1.2, "Амперин": 1.2, "Кинза": 1.2},
            "120 на 80": {"Мукалтин": 1.05, "Кашлевит": 1.05, "Ингасол": 1.05, "Ринофолт": 1.05, "Амперин": 1.05}
        }

    def __etc_positions(self) -> dict[str, dict[str, float]]:
        return {
            "Здоровье": {"Вкуснетта": 0.95, "Итифен": 0.95, "Семирол": 0.95, "Носорин": 0.95, "Плесс": 0.95, "Имбафорт": 0.95},
            "Гиппократ": {"Вкуснетта": 0.95, "Итифен": 0.95, "Семирол": 0.95, "Носорин": 0.95, "Плесс": 0.95, "Имбафорт": 0.95},
            "Кремлёвская": {"Вкуснетта": 0.95, "Итифен": 0.95, "Семирол": 0.95, "Носорин": 0.95, "Плесс": 0.95, "Имбафорт": 0.95},
            "Аптеки у дома": {"Вкуснетта": 0.95, "Итифен": 0.95, "Семирол": 0.95, "Носорин": 0.95, "Плесс": 0.95, "Имбафорт": 0.95},
            "Кавказское долголетие": {"Вкуснетта": 0.95, "Итифен": 0.95, "Семирол": 0.95, "Носорин": 0.95, "Плесс": 0.95, "Имбафорт": 0.95},
            "Крымская здравница": {"Вкуснетта": 0.95, "Итифен": 0.95, "Семирол": 0.95, "Носорин": 0.95, "Плесс": 0.95, "Имбафорт": 0.95},
            "Здравствуйте!": {"Вкуснетта": 0.95, "Итифен": 0.95, "Семирол": 0.95, "Носорин": 0.95, "Плесс": 0.95, "Имбафорт": 0.95},
            "Богатырь": {"Вкуснетта": 0.95, "Итифен": 0.95, "Семирол": 0.95, "Носорин": 0.95, "Плесс": 0.95, "Имбафорт": 0.95},
            "Кедр": {"Вкуснетта": 0.95, "Итифен": 0.95, "Семирол": 0.95, "Носорин": 0.95, "Плесс": 0.95, "Имбафорт": 0.95},
            "Сибирь": {"Вкуснетта": 0.95, "Итифен": 0.95, "Семирол": 0.95, "Носорин": 0.95, "Плесс": 0.95, "Имбафорт": 0.95},
            "Омега": {"Вкуснетта": 0.95, "Итифен": 0.95, "Семирол": 0.95, "Носорин": 0.95, "Плесс": 0.95, "Имбафорт": 0.95},
            "Будь Здоров!": {"Вкуснетта": 0.95, "Итифен": 0.95, "Семирол": 0.95, "Носорин": 0.95, "Плесс": 0.95, "Имбафорт": 0.95},
            "Молодость": {"Вкуснетта": 1.0, "Итифен": 1.0, "Семирол": 1.0, "Носорин": 1.0, "Плесс": 1.0, "Имбафорт": 1.0},
            "Таблетница": {"Вкуснетта": 1.05, "Итифен": 1.05, "Семирол": 1.05, "Носорин": 1.05, "Плесс": 1.05, "Имбафорт": 1.05},
            "Аспирин": {"Вкуснетта": 0.7, "Итифен": 0.7, "Семирол": 0.7, "Носорин": 0.7, "Плесс": 0.7, "Имбафорт": 0.7},
            "36 и 6": {"Вкуснетта": 1.2, "Семирол": 1.2, "Носорин": 1.2, "Плесс": 1.2, "Имбафорт": 1.2},
            "120 на 80": {"Вкуснетта": 1.04, "Итифен": 1.04, "Семирол": 1.04, "Носорин": 1.04, "Плесс": 1.04}
        }
