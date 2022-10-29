# используется для сортировки
from operator import itemgetter
from pprint import pprint


class Сhp:
    """Раздел"""

    def __init__(self, id, n1, ws, doc_id):
        self.id = id
        self.n1 = n1
        self.ws = ws
        self.doc_id = doc_id


class Doc:
    """Документ"""

    def __init__(self, id, n2):
        self.id = id
        self.n2 = n2


class СhpDoc:
    """
    'Разделы документа' для реализации
    связи многие-ко-многим
    """

    def __init__(self, doc_id, сhp_id):
        self.doc_id = doc_id
        self.сhp_id = сhp_id


# Документы
docs = [
    Doc(1, 'Рубежный контроль по БКИТ'),
    Doc(2, 'Домашнее задание по Правоведению'),
    Doc(3, 'Отчёт по практике УПСП'),
    Doc(4, 'Лекция по Экологии'),
    Doc(5, 'Курсовая работа по АСОИУ'),
    Doc(6, 'Ответы к РК'),
]

# Разделы
сhps = [
    Сhp(1, 'Содержание', 159, 3),
    Сhp(2, 'Введение', 255, 3),
    Сhp(3, 'Основная часть', 1532, 1),
    Сhp(4, 'Заключение', 199, 3),
    Сhp(5, 'Приложение', 532, 5),
    Сhp(6, 'Ответы', 2222, 5),
    Сhp(7, 'Эпилог', 15, 4),
]

сhps_docs = [
    СhpDoc(1, 1),
    СhpDoc(2, 2),
    СhpDoc(3, 3),
    СhpDoc(3, 4),
    СhpDoc(3, 5),

    СhpDoc(4, 3),
    СhpDoc(6, 6),
    СhpDoc(5, 4),
    СhpDoc(2, 6),
    СhpDoc(7, 3),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(с.n1, с.ws, d.n2)
                   for d in docs
                   for с in сhps
                   if с.doc_id == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.n2, cd.doc_id, cd.сhp_id)
                         for d in docs
                         for cd in сhps_docs
                         if d.id == cd.doc_id]

    many_to_many = [(c.n1, c.ws, doc_n2)
                    for doc_n2, doc_id, chp_id in many_to_many_temp
                    for c in сhps if c.id == chp_id]

    print('Задание Б1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    pprint(res_11)

    print('\nЗадание Б2')
    res_12_unsorted = []
    # Перебираем все документы
    for d in docs:
        # Список разделов документа
        d_сhps = list(filter(lambda i: i[2] == d.n2, one_to_many))
        # Если документ не пустой
        if len(d_сhps) > 0:
            res_12_unsorted.append((d.n2, len(d_сhps)))

    # Сортировка по количеству разделов
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    pprint(res_12)

    print('\nЗадание Б3')
    res_13 = {}
    # Перебираем все документы
    for c in сhps:
        if "От" in c.n1:
            d_chps = list(filter(lambda i: i[0] == c.n1, many_to_many))
            d_chps_n1s = [x for _, _, x in d_chps]

            res_13[c.n1] = d_chps_n1s

    pprint(res_13)


if __name__ == '__main__':
    main()
