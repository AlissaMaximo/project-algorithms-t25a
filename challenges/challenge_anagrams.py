def is_anagram(first_string, second_string):
    """Faça o código aqui."""

    def quicksort(array_list):
        if len(array_list) <= 1:
            return array_list

        # se a lista for ["o", "i"], pivot vai ser "i"
        pivot = array_list[len(array_list) // 2]

        left = [char for char in array_list if char < pivot]  # entra "o"

        middle = [char for char in array_list if char == pivot]  # entra "i"

        # não entra item da lista
        right = [char for char in array_list if char > pivot]

        return quicksort(left) + middle + quicksort(right)

    lowered_str1 = first_string.lower()
    lowered_str2 = second_string.lower()

    sorted_lowered_str1 = quicksort(list(lowered_str1))
    sorted_lowered_str2 = quicksort(list(lowered_str2))

    return (""
            .join(sorted_lowered_str1),
            "".join(sorted_lowered_str2),
            sorted_lowered_str1 == sorted_lowered_str2)
