def is_anagram(first_string, second_string):
    """Faça o código aqui."""

    def quicksort(list):
        if len(list) <= 1:
            return list

        # se a lista for ["o", "i"], pivot vai ser "i"
        pivot = list[len(list) // 2]

        left = [char for char in list if char < pivot]  # entra "o"

        middle = [char for char in list if char == pivot]  # entra "i"

        # não entra item da lista
        right = [char for char in list if char > pivot]

        return quicksort(left) + middle + quicksort(right)

    sorted_lowered_str1 = quicksort(list(first_string.lower()))
    sorted_lowered_str2 = quicksort(list(second_string.lower()))

    return ("".join(sorted_lowered_str1),
            "".join(sorted_lowered_str2),
            sorted_lowered_str1 == sorted_lowered_str2)
