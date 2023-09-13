from django import template

register = template.Library()

CENSOR_WORDS = ['Путин']


@register.filter()
def censor(value):
    text = value.split()
    new_value = []

    for i in text:
        if i in CENSOR_WORDS:
            censor_word = i[0] + '*'*(len(i)-1)
            new_value.append(censor_word)
        else:
            new_value.append(i)

    return ' '.join(new_value)


def main():
    print(censor('США следует убедить Зеленского отказаться от указа о запрете переговоров с Россией, пока ее возглавляет Путин, если считают, что Киев готов к диалогу, заявил российский лидер'))


if __name__ == '__main__':
    main()
