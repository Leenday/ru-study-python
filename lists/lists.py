class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        pass
        if not input_list:
            return input_list
        # take a num first num for reference
        max_num = input_list[0]
        for i in input_list:
            if i > max_num:
                max_num = i
        return list(map(lambda x: max_num if x > 0 else x, input_list))

    @staticmethod
    def recurcive_search(input_list: list[int], query: int, start: int, end: int) -> int:
        if not input_list:
            return -1
        center = (start + end) // 2
        if input_list[center] == query:
            return center
        elif end - start <= 1:
            return -1
        elif input_list[center] <= query:
            return ListExercise.recurcive_search(input_list, query, center, end)
        elif input_list[center] > query:
            return ListExercise.recurcive_search(input_list, query, start, center)

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        pass
        return ListExercise.recurcive_search(input_list, query, 0, len(input_list))
