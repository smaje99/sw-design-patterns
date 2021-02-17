from creacionales.builder.builder import CardBuilder


def main():
    card = CardBuilder('Credit', '0000')\
        .name('Sergio')\
        .build()

    print(card)
    print(card.name)


if __name__ == '__main__':
    main()
