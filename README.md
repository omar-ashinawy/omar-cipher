# omar-cipher
## Implementation of five classical ciphers, DES, and AES in python
In this project, I implemented five classical ciphers: Caesar, PlayFair, Hill, Vigenere, and Vernam in addition to two of the modern ciphers: DES and AES. All code is written in python using only numpy as an external library for some optimized arithmatic operations.
## Usage
### Classical Ciphers
To use one of the five classical ciphers, you have to instantiate the `Classical_Ciphers` class passing the type of the cipher you want to use, the key, and a boolean determining the mode of operation of Vigenere cipher (in case you wants Vigenere). When using Hill cipher, you have to pass a python list consisting of the key values arranged in a row-major style. 
```python
# using any of the ciphers except for hill and vegenere
cipher = Classical_Ciphers(cipher = 'playfair', key = 'rats')
encrypted = cipher.encrypt('omarashinawy')
print(encrypted)
decrypted = cipher.decrypt(encrypted)
print(decrypted)
```
```python
# using hill
cipher = Classical_Ciphers(cipher = 'HiLL', key = [5, 17, 8, 3])
encrypted = cipher.encrypt('omarashinawy')
print(encrypted)
decrypted = cipher.decrypt(encrypted)
print(decrypted)
```
```python
# using vegenere
cipher = Classical_Ciphers(cipher = 'Vigenere', key = 'rats', vegenere_auto_mode = True)
encrypted = cipher.encrypt('omarashinawy')
print(encrypted)
decrypted = cipher.decrypt(encrypted)
print(decrypted)
```
