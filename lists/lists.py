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
    def recurcive_search(input_list: list[int], query: int, indexes: list[int]) -> int:
        if not input_list:
            return -1
        list_center_index = int(len(input_list) / 2)
        if len(input_list) == 1:
            return indexes[0] if input_list[0] == query else -1
        elif input_list[list_center_index] <= query:
            return ListExercise.recurcive_search(
                input_list[list_center_index:], query, indexes[list_center_index:]
            )
        elif input_list[list_center_index] > query:
            return ListExercise.recurcive_search(
                input_list[:list_center_index], query, indexes[:list_center_index]
            )

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
        return ListExercise.recurcive_search(input_list, query, list(range(len(input_list))))
