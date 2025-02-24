alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ")", '{', '}', '[', ']', '-', '+', '=', '_']
checker = 'yes'

def encoder(message, shift):
  message = list(message)
  print("Encoded message: ", end='')
  for i in range(len(message)):
    symbols_count = symbols.count(message[i])
    number_count = numbers.count(message[i])
    if message[i] != ' ' and symbols_count == 0 and number_count == 0:
      position = alphabet.index(message[i])
      message[i] = alphabet[(position+shift)%26]
    print(message[i], end='')
  print("\n")

def decoder(message, shift):
  message = list(message)
  print("Decoded Message: ", end='')
  for i in range(len(message)):
    symbols_count = symbols.count(message[i])
    number_count = numbers.count(message[i])
    if message[i] != ' ' and symbols_count == 0 and number_count == 0:
      position = alphabet.index(message[i])
      message[i] = alphabet[(position-shift)%26]
    print(message[i], end='')
  print("\n")

while checker == 'yes':
  message = input("Enter a message: ").lower()
  shift = int(input("Enter the shift number: "))
  what_to_do = input("Encode or Decode: ").lower()

  if what_to_do == 'encode':
    encoder(message, shift)
  elif what_to_do == 'decode':
    decoder(message, shift)

  checker = input('Do you want to run again(Yes or No): ').lower()