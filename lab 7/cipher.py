


class Cipher:
  def __init__(self):
    """ initialiszing list of alphabets from A-Z """
    self._alphabet = ["A", "B", "C","D", "E", "F","G","H","I", "J","K", "L","M","N", "O", "P", "Q",  "R", "S", "T", "U", "V", "W","X", "Y","Z"]
            

  def encrypt_message(self, message):
    """ will take each character from string and send it to encrypt letter function """
    chg_message = list(message.upper())
    
    """ before we make sure is uppercase so we can find it in the list """
    for i in range(len(chg_message)):
      
      if chg_message[i] in self._alphabet:
        chg_message[i] = self._encrypt_letter(chg_message[i])


    return "".join(chg_message)

  def decrypt_message(self, message):
    """ will take each character from string and send it to decrypt letter function """
    chg_message = list(message.upper())
    """ before we make sure is uppercase so we can find it in the list """
    for i in range(len(chg_message)):
      if chg_message[i] in self._alphabet:
        chg_message[i] = self._decrypt_letter(chg_message[i])

    return "".join(chg_message)

  def _encrypt_letter(self, letter):
    """ we will change the letter to hide message """
    location = self._alphabet.index(letter)
    position = 25 - location

    return self._alphabet[position]


  def _decrypt_letter(self, letter):
    """ we will change the letter to reveal message """
    location = self._alphabet.index(letter)
    position = 25 - location

    return self._alphabet[position]

