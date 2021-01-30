letter_to_num = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25
}
class Converter():
    def __get_key(self, val):
        for key, value in letter_to_num.items():
            if val == value:
                return key
    def str_to_nums(self, str):
        nums = []
        for letter in str:
            nums.append(letter_to_num[letter])
        return nums
    def nums_to_str(self, nums):
        str = ''
        for num in nums:
            str += self.__get_key(num)
        return str
    def __extended_gcd(self, a, b):  
        if a == 0 :
            return b, 0, 1
        gcd, x1, y1 = self.__extended_gcd(b%a, a)  
        x = y1 - (b//a) * x1  
        y = x1
        return gcd, x, y
    def inv_mod(self, num, mod = 26):
        stored_num = num
        stored_mod = mod
        gcd, x, _ = self.__extended_gcd(stored_num, stored_mod)
        if not (gcd == 1):
            raise ArithmeticError(f"No inverse of key determinant ({num}) in mod {mod}!")
        if x < 0:
            x += mod
        return x
    def letter_to_num(self):
        return letter_to_num