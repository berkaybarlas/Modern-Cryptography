## Rotor
class Rotor:

  def __init__(self, letters):
    """ 
    constructor Rotor("FABECD")
    """
    self.rotorLetters = []
    self.reverseRotor = {}
    self.rotorTurn = 0

    for i, ch in enumerate(letters):
      self.reverseRotor[ch.upper()] = chr(i + ord('A'))
      self.rotorLetters.append(ch)   

  def encryptLetter(self, letter):
    """
    A function returns the encoded version of letter
    """
    charIndex = (ord(letter.upper()) - ord('A') + self.rotorTurn) % len(self.rotorLetters)
    return self.rotorLetters[charIndex]

  def encrypt(self, letter):
    """
    A function returns the encoded version of letter
    """
    encryptedLetters = []
    for ch in letter:
      encryptedLetters.append(self.encryptLetter(ch))
    return "".join(encryptedLetters)

  def decryptLetter(self, letter):
    """
    A function returns the decoded version of ciphertext
    """
    charDifference = ((ord(self.reverseRotor[letter]) - ord('A') - self.rotorTurn) % len(self.rotorLetters))
    return chr(ord('A') + charDifference)

  def decrypt(self, word):
    """
    A function returns the decoded version of ciphertext
    """
    decryptedLetters = []
    for ch in word:
      decryptedLetters.append(self.decryptLetter(ch))
    return "".join(decryptedLetters)

  def click(self):
    """
    A function that moves rotor one click
    ['F','A','B'] -> ['A','B','F']
    """
    self.rotorTurn = (self.rotorTurn + 1) % len(self.rotorLetters)
  
  def turn(self, turnAmount):
    newTurnAmount = turnAmount % len(self.rotorLetters)
    self.rotorTurn = newTurnAmount
 
  def resetRotor(self):
    self.rotorTurn = 0

  def __repr__(self):
    alphebet = []
    for i in range(len(self.rotorLetters)):
      alphebet.append(chr(ord('A') + i ))

    return self.encrypt("".join(alphebet))