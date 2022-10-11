import cipher

class Caesar_cipher(cipher.Cipher):
  

  def __init__(self, shift):
    """ getting the init from cipher and also making sure the shift is an intenger """
    super().__init__()
    if type(shift) == int:
      self._shift = shift
    else:
      raise TypeError("Sorry, incorrect shift value")    

  def _encrypt_letter(self, letter):
    """ changing letter depending on the shift """
    location = self._alphabet.index(letter)
    position = self._shift + location

    """ if position out of bount then we will substract in order to sind it within list """
    if position > 25:
      position -= 26
    
    return self._alphabet[position]

  def _decrypt_letter(self, letter):
    """ changing letter to find the message depending on the shift """
    location = self._alphabet.index(letter)
    position =  location - self._shift

    """ checking if position is negative(out of bound) so we can add in order to stay within the list range """
    if position < 0:
      position += 26
    
    return self._alphabet[position]