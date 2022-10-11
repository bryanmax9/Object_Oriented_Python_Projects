from email import message
import caesar_cipher
import cipher
import check_input

def main():
  

  

  print(""" 
  Secret Decoder Ring:
  1. Encrypt
  2. Decrypt
   """)

  usr_option =  check_input.get_int_range("",1,2)

  """ Encripting message """
  if usr_option == 1:
    print(""" 
    Enter encryption type:
    1. Atbash
    2. Caesar
     """)
    
    usr_option2 =  check_input.get_int_range("",1,2)

    """ encripting message with Atbash == Cipher object """
    if usr_option == 1 and usr_option2 == 1:
      file = open("message.txt", "w")
      mensaje = input("Enter message: ")
      encrypted = cipher.Cipher()
      hidden = encrypted.encrypt_message(mensaje)
      file.write(hidden)
      print("Encrypted message saved to “message.txt”.")
    
    elif usr_option == 1 and usr_option2 == 2:
      """encripting message with Caesar == Caesar_cipher object """
      file = open("message.txt", "w")
      mensaje = input("Enter message: ")
      shift = int(input("Enter shift value: "))
      encrypted = caesar_cipher.Caesar_cipher(shift)
      hidden = encrypted.encrypt_message(mensaje)
      file.write(hidden)
      print("Encrypted message saved to “message.txt”.")
   
  elif usr_option == 2:
    """ decrypting message """
    print(""" 
    Enter decryption type:
    1. Atbash
    2. Caesar
     """)
    
    usr_option2 = check_input.get_int_range("",1,2)

    """ decripting message with Atbash == Cipher object """
    if usr_option == 2 and usr_option2 == 1:
      file = open("message.txt", "r")
      decrypted = cipher.Cipher()
      mensaje = file.read()

      print("Reading encrypted message from “message.txt”.")
      revealed = decrypted.decrypt_message(mensaje)
      print("Decrypted message: ", revealed)
    
    elif usr_option == 2 and usr_option2 == 2:
      """encripting message with Caesar == Caesar_cipher object """
      file = open("message.txt", "r")
      shift = int(input("Enter shift value: "))
      decrypted = caesar_cipher.Caesar_cipher(shift)
      mensaje = file.read()

      print("Reading encrypted message from “message.txt”.")

      revealed = decrypted.decrypt_message(mensaje)

      print("Decrypted message: ", revealed)





main()