
from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass
    def is_two_object_has_same_value(first, second):
        return first == second



    def is_two_objects_has_same_type(first, second):
        return type(first) == type(second)

        """
        If @first and @second has same type should return True
        In another case should return False
        """



    def is_two_objects_is_the_same_objects(first, second):
        return  id(first) == id(second)



    def multiple_ints(first_value ,second_value):
        try:
            return first_value + second_value
        except:
            print('ValueError')





    def multiple_ints_with_conversion(first_value, second_value):
        try:
            first_value = int(first_value)
            second_value = int(second_value)
            return first_value *second_value
        except (ValueError):
            print("Not valid input data")

        """
        If possible to convert arguments to int value - convert and multiply them.
        If it is impossible raise OurAwesomeException
    
        Args:
            first_value: number for multiply
            second_value: number for multiply
    
        Raises:
            OurAwesomeException
    
        Returns: multiple of two numbers.
    
        Examples:
            multiple_ints_with_conversion(6, 6)
            >>> 36
            multiple_ints_with_conversion(2, 2.0)
            >>> 4
            multiple_ints_with_conversion("12", 1)
            >>> 12
            try:
                multiple_ints_with_conversion("Hello", 2)
            except ValueError:
                print("Not valid input data")
            >>> "Not valid input data"
        """



    def is_word_in_text(word: str, text: str) -> bool:
        if word in text:
            return True
        else:
            return False

        """
        If text contain word return True
        In another case return False.
    
        Args:
            word: Searchable substring
            text: Text for searching
    
        Examples:
            is_word_in_text("Hello", "Hello word")
            >>> True
            is_word_in_text("Glad", "Nice to meet you ")
            >>> False
    
        """



    def some_loop_exercise() -> list:
        a = []
        for i in range (13):
            if i!= 6 and i != 7:
                a += [i]
        return a
        """
        Use loop to create list that contain int values from 0 to 12 except 6 and 7
        """


    def remove_from_list_all_negative_numbers(data: List[int]) -> list:
        b = []
        for i in data:
            if i >= 0:
                b += [i]
        return b
        """
        Use loops to solve this task.
        You could use data.remove(negative_number) to solve this issue.
        Also you could create new list with only positive numbers.
        Examples:
            remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
            >>> [1, 5, 8]
        """


    def alphabet() -> dict:
        d = {a: b for a, b in zip(range(1, 27), 'abcdefghijklmnopqrstuvwxyz')}
        return d

        """
        Create dict which keys is alphabetic characters. And values their number in alphabet
        Notes You could see an implementaion of this one in test, but create another one
        Examples:
            alphabet()
            >>> {"a": 1, "b": 2 ...}
        """


    def simple_sort(data: List[int]) -> List[list]:
        b = []
        while len(data) > 2:
            b += [min(data)]
            data.remove(min(data))
        if data[0] >= data[1]:
            b += [data[1], data[0]]
        else:
            b += [data[0], data[1]]
        return b
        """
        Sort list of ints without using built-in methods.
        Examples:
            simple_sort([2, 9, 6, 7, 3, 2, 1])
            >>> [1, 2, 2, 3, 6, 7, 9]
        Returns:
    
        """
