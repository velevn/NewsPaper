from django import template

register = template.Library()

CENSOR_WORDS = ['Путин']

class CensorException(Exception):
    def __str__(self):
        return 'Фильтр обрабытвает только текст'

@register.filter()
def censor(value):

    if not isinstance(value, str):
        raise CensorException

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
    print(censor(4))


if __name__ == '__main__':
    main()
