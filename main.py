from database import get_all_stars, get_all_constellations, get_star_by_id, get_constellation_by_id, session, Star
import json

def load_star_symbols():
    try:
        with open("star_symbols.txt", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"большой": "*", "маленький": ".", "средний": "+"}

def save_star_symbols(symbols):
    with open("star_symbols.txt", "w") as f:
        json.dump(symbols, f)

def print_star_frame(stars, symbols):
    for star in stars:
        if star.size == 'Big':
            size_ru = 'большой'
        elif star.size == 'Small':
            size_ru = 'маленький'
        elif star.size == 'Medium':
            size_ru = 'средний'
        symbol = symbols[size_ru]
        print(f"{symbol} {star.name} ({size_ru}) - {star.constellation.name}")
        print(f"  Description: {star.description[:60]}...")
        print()

def print_constellation_frame(constellations):
    for constellation in constellations:
        print(f"{constellation.name}")
        print(f"  Описание: {constellation.description[:60]}...")
        print("  Звезды:")
        for star in constellation.stars:
            print(f"    {star.name} ({star.size})")
        print()

def print_star_details(star):
    print(f"Звезда: {star.name}")
    print(f"  Описание: {star.description}")
    print(f"  Координаты: ({star.x_coord}, {star.y_coord})")
    print(f"  Созвездие: {star.constellation.name} ({star.constellation.description})")
    print()

def print_constellation_details(constellation):
    print(f"Созвездие: {constellation.name}")
    print(f"  Описание: {constellation.description[:60]}...")
    print("  Звезды:")
    stars = session.query(Star).filter_by(constellation_id=constellation.id).all()
    for star in stars:
        if star.size == 'Big':
            size_ru = 'большой'
        elif star.size == 'Small':
            size_ru = 'маленький'
        elif star.size == 'Medium':
            size_ru = 'средний'
        print(f"    {star.name} ({size_ru})")
        break
    print()


def main():
    symbols = load_star_symbols()

    while True:
        print("Меню:")
        print("1. Показать все звезды")
        print("2. Показать все созвездий")
        print("3. Показать детали о звездах")
        print("4. Показать детали созвездий")
        print("5. Изменить символы звезд")
        print("6. Выход")

        choice = input("Введи свой выбор: ")

        if choice == "1":
            stars = get_all_stars()
            print_star_frame(stars, symbols)
        elif choice == "2":
            constellations = get_all_constellations()
            print_constellation_frame(constellations)
        elif choice == "3":
            star_id = int(input("Введи ID звезды: "))
            star = get_star_by_id(star_id)
            if star is None:
                print("Звезда не найдена")
            else:
                print_star_details(star)
        elif choice == "4":
            constellation_id = int(input("Введи ID созвездия: "))
            constellation = get_constellation_by_id(constellation_id)
            if constellation is None:
                print("Созвездие не найдено")
            else:
                print_constellation_details(constellation)
        elif choice == "5":
            symbols["большая"] = input("Введите символ для обозначения больших звезд: ")
            symbols["маленькая"] = input("Введите символ для обозначения маленьких звезд: ")
            symbols["средняя"] = input("Введите символ для обозначения средних звезд: ")
            save_star_symbols(symbols)
        elif choice == "6":
            break
        else:
            print("Ошибка ввода. Попробуйте снова!")

if __name__ == "__main__":
    main()