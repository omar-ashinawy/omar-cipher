from numpy import array, mod, sqrt, matmul, ndarray, linalg, add, subtract, rint
from converter import Converter
class Caeser():
    def __init__(self, key, converter):
        self.__converter = converter
        self.__key = key
    def encrypt(self, message):
        nums = self.__converter.str_to_nums(message)
        encrypted_nums = array(nums)
        encrypted_nums = mod((encrypted_nums + self.__key), 26)
        return self.__converter.nums_to_str(encrypted_nums)
    def decrypt(self, message):
        nums = self.__converter.str_to_nums(message)
        decrypted_nums = array(nums)
        decrypted_nums = mod((decrypted_nums - self.__key), 26)
        return self.__converter.nums_to_str(decrypted_nums)

class PlayFair():
    def __init__(self, key, converter):
        self.__converter = converter
        self.__playfair_matrix = self.__construct_matrix(key.replace(' ', '').lower())
    def __get_playfair_key(self, key):
        dup_free_key = ''
        for letter in key:
            if not (letter in dup_free_key):
                dup_free_key += letter
        playfair_key = dup_free_key
        for letter in self.__converter.letter_to_num():
            if not (letter in dup_free_key) and letter != 'j':
                playfair_key += letter
        return playfair_key
    def __construct_matrix(self, key):
        playfair_matrix = [[0 for i in range(5)] for j in range(5)]
        playfair_key = self.__get_playfair_key(key)
        k = 0
        for i in range(5):
            for j in range(5):
                playfair_matrix[i][j] = playfair_key[k]
                k += 1
        return playfair_matrix
    def __get_pairs(self, message):
        message_pairs = []
        for i in range(0, len(message), 2):
            if (i != len(message) - 1):
                if (message[i] == message[i+1]):
                    message = message[:i+1] + 'x' + message[i+1:]
        if len(message) % 2:
            message += 'x'
        for i in range(0, len(message), 2):
            message_pairs.append(message[i] + message[i+1])
        return message_pairs
    def __locate(self, letter):
        if letter == 'j':
            letter = 'i'
        for i in range(5):
            for j in range(5):
                if self.__playfair_matrix[i][j] == letter:
                    return i, j
    def __move_pair(self, pair, encrypt):
        first_row, first_col = self.__locate(pair[0])
        second_row, second_col = self.__locate(pair[1])
        if first_row == second_row:
            step_first = (first_col + 1) if encrypt else (first_col - 1)
            step_second = (second_col + 1) if encrypt else (second_col - 1)
            new_first = self.__playfair_matrix[first_row][step_first%5]
            new_second = self.__playfair_matrix[second_row][step_second%5]
            return new_first + new_second
        if first_col == second_col:
            step_first = (first_row + 1) if encrypt else (first_row - 1)
            step_second = (second_row + 1) if encrypt else (second_row - 1)
            new_first = self.__playfair_matrix[step_first%5][first_col]
            new_second = self.__playfair_matrix[step_second%5][second_col]
            return new_first + new_second
        new_first = self.__playfair_matrix[first_row][second_col]
        new_second = self.__playfair_matrix[second_row][first_col]
        return new_first + new_second
    def encrypt(self, message):
        encrypted_message = ''
        for pair in self.__get_pairs(message):
            encrypted_message = encrypted_message + self.__move_pair(pair, True)
        return encrypted_message
    def decrypt(self, message):
        decrypted_message = ''
        for pair in self.__get_pairs(message):
            decrypted_message = decrypted_message + self.__move_pair(pair, False)
        return decrypted_message

class Hill():
    def __init__(self, key, converter):
        self.__converter = converter
        self.__hill_type = sqrt(len(key)).astype(int)
        self.__key = array(key).reshape((self.__hill_type, self.__hill_type))
    def __expand_message(self, message):
        while (len(message) % self.__hill_type):
            message += 'x'
        return message
    def encrypt(self, message):
        message = self.__expand_message(message)
        nums = self.__converter.str_to_nums(message)
        encrypted_nums = []
        for i in range(0, len(nums), self.__hill_type):
            current = array([nums[i+j] for j in range(self.__hill_type)]).reshape((self.__hill_type, 1))
            encrypted_nums.append(mod(matmul(self.__key, current), 26))
        encrypted_nums = ndarray.flatten(array(encrypted_nums))
        return self.__converter.nums_to_str(encrypted_nums)
    def decrypt(self, message):
        nums = self.__converter.str_to_nums(message)
        key_det = linalg.det(self.__key)
        key_det_inv = self.__converter.inv_mod(mod(rint(key_det.copy()).astype(int), 26))
        key_inv = key_det_inv * key_det * linalg.inv(self.__key)
        key_inv = rint(mod(key_inv, 26)).astype(int)
        decrypted_nums = []
        for i in range(0, len(nums), self.__hill_type):
            current = array([nums[i+j] for j in range(self.__hill_type)]).reshape((self.__hill_type, 1))
            decrypted_nums.append(mod(matmul(key_inv, current), 26))
        decrypted_nums = ndarray.flatten(array(decrypted_nums))
        return self.__converter.nums_to_str(decrypted_nums)

class Vegenere():
    def __init__(self, key, converter, auto_mode = True):
        self.__converter = converter
        self.__key = key.replace(' ', '').lower()
        self.__auto_mode = auto_mode
    def __expand_key(self, key, message, auto_mode = True):
        while len(key) < len(message):
            if auto_mode:
                key += message
            else:
                key += key
        if len(key) > len(message):
            key = key[: len(message)]
        return key
    def encrypt(self, message):
        self.__key = self.__expand_key(self.__key, message, self.__auto_mode)
        num_key = array(self.__converter.str_to_nums(self.__key))
        nums = array(self.__converter.str_to_nums(message))
        encrypted_nums = mod(add(nums, num_key), 26)
        return self.__converter.nums_to_str(encrypted_nums)
    def decrypt(self, message):
        num_key = array(self.__converter.str_to_nums(self.__key))
        nums = array(self.__converter.str_to_nums(message))
        decrypted_nums = mod(subtract(nums, num_key), 26)
        return self.__converter.nums_to_str(decrypted_nums)

class Vernam():
    def __init__(self, key, converter):
        self.__converter = converter
        self.__key = array(self.__converter.str_to_nums(key.replace(' ', '').lower()))
    def encrypt(self, message):
        nums = array(self.__converter.str_to_nums(message))
        encrypted_nums = mod(add(nums, self.__key), 26)
        return self.__converter.nums_to_str(encrypted_nums)
    def decrypt(self, message):
        nums = array(self.__converter.str_to_nums(message))
        decrypted_nums = mod(subtract(nums, self.__key), 26)
        return self.__converter.nums_to_str(decrypted_nums)

class Classical_Ciphers():
    def __init__(self, cipher, key, vegenere_auto_mode = True):
        self.__converter = Converter()
        self.__cipher_type = cipher.lower()
        if self.__cipher_type == 'caeser':
            self.__cipher = Caeser(key, self.__converter)
        elif self.__cipher_type == 'playfair':
            self.__cipher = PlayFair(key, self.__converter)
        elif self.__cipher_type == 'hill':
            self.__cipher = Hill(key, self.__converter)
        elif self.__cipher_type == 'vegenere':
            self.__cipher = Vegenere(key, self.__converter, vegenere_auto_mode)
        elif self.__cipher_type == 'vernam':
            self.__cipher = Vernam(key, self.__converter)
        else:
            raise ModuleNotFoundError(f'The {self.__cipher_type} cipher is not supported!')
    def encrypt(self, message):
        return self.__cipher.encrypt(message.replace(' ', '').lower())
    def decrypt(self, message):
        return self.__cipher.decrypt(message.replace(' ', '').lower())

# Usage Example
# cipher = Classical_Ciphers('vegenere', 'aether')
# encrypted = cipher.encrypt('lemfazxf')
# print(encrypted)
# decrypted = cipher.decrypt(encrypted)
# print(decrypted)