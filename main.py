from adventurer import Adventurer
from barbarian import Barbarian
from wizard import Wizard
from monk import Monk
from dice import Dice

def main():
    b = Barbarian(
        'Kithri',
        6,
        18,
        72,
        {
            'Strength': 19,
            'Dexterity': 14,
            'Constitution': 16,
            'Intelligence': 12,
            'Wisdom': 12,
            'Charisma': 10,
        },
        {
            'Battleaxe': [Dice(1, 10, 4), 'Strength', True],
            'Longbow': [Dice(1, 8, 2), 'Dexterity', True],
            'Shortsword': [Dice(1, 6, 4), 'Strength', True],
        }
    )

    w = Wizard(
        'Cyruk',
        1,
        10,
        10,
        {
            'Strength': 12,
            'Dexterity': 14,
            'Constitution': 10,
            'Intelligence': 12,
            'Wisdom': 16,
            'Charisma': 16,
        },
        {},
        {
            'FireBolt': Dice(1, 10)
        }
    )

    m = Monk(
        'Vani',
        1,
        10,
        15,
        {
            'Strength': 12,
            'Dexterity': 14,
            'Constitution': 10,
            'Intelligence': 12,
            'Wisdom': 16,
            'Charisma': 16,
        },
        {
            'Shortsword': [Dice(1, 6, 4), 'Strength', True]
        }
    )

    print(b)
    print(w)
    print(m)

    print()

    print(m.name)
    print('Ki points:', m.get_ki_points())
    m.level_up()
    print('Ki points after lvl up:', m.get_ki_points())
    print(m)

    print()

    print(w.name)
    print('Cast FireBolt:', w.cast_cantrip('FireBolt'))
    print('Hit points:', w.hp)
    w.level_up()
    print('Hit points after lvl up:', w.hp)
    print(w)

    print()

    print(b.name)
    print('Attack with Battleaxe', b.attack('Battleaxe'))
    print('Attack with Longbow', b.attack('Longbow'))
    print('Max rages:', b.get_max_rages())
    print('Current rages:', b.rages)
    print('Entering a rage')
    b.enter_rage()
    print(b)
    print('Attack with Battleaxe', b.attack('Battleaxe'))
    print('Attack with Longbow', b.attack('Longbow'))
    print('Current rages:', b.rages)
    b.exit_rage()
    print('Current rages:', b.rages)
    print(b)

if __name__ == "__main__":
    main()
