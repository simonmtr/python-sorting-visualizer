class ArrayHelper:
    def normalize_array(not_normalized_array):
        try:
            normalized_sorting_array = [i / max(not_normalized_array) for i in not_normalized_array]
        except ZeroDivisionError:
            normalized_sorting_array = []
            for i in not_normalized_array:
                if i == 0:
                    normalized_sorting_array.append(i)
                else:
                    normalized_sorting_array.append(i / max(not_normalized_array))
        return normalized_sorting_array