from rotor import Rotor

class Enigma:

  def __init__(self, *letters):
    # Should return error if len(letters) != rotorNumber
    self.rotors = []
    self.turnNumber = 0
    self.rotorSize = len(letters[0])
    
    letterList= list(letters)
    for i in range(len(letterList)):
      self.rotors.append(Rotor(letterList[i]))

  def encrypt(self, letter):
    """
    A function returns the encoded version of letter
    """
    encryptedLetters = []
    for ch in letter:
      encryptedLetter = ch
      for i in range(len(self.rotors)):
        encryptedLetter = self.rotors[i].encryptLetter(encryptedLetter)
      encryptedLetters.append(encryptedLetter)
      self.click()

    return "".join(encryptedLetters)
    
  def decrypt(self, letter):
    """
    A function returns the decoded version of ciphertext
    """
    decryptedLetters = []
    for ch in letter:
      decryptedLetter = ch
      for i in reversed(range(len(self.rotors))):
        decryptedLetter = self.rotors[i].decryptLetter(decryptedLetter)
      decryptedLetters.append(decryptedLetter)
      self.click()
    return "".join(decryptedLetters)

  def fastDecrpytLetter(self, letter):
    """
    A function returns the decoded version of ciphertext
    """
    pass

  def decryptWithTurn(self, letter, turnNumber):
    self.setRotorTurns(turnNumber)
    return self.decrypt(letter)

  def setRotorTurns(self, turnNumber):
    for i in range(len(self.rotors)):
      turnAmount = turnNumber // (self.rotorSize**i)
      index = len(self.rotors) - i - 1
      self.rotors[index].turn(turnAmount)


  def click(self, reverse = True):
    rotorCycle = self.possiblityNumber()
    self.turnNumber = self.turnNumber + 1 % rotorCycle

    for i in range(len(self.rotors)):
      if self.turnNumber % self.rotorSize**i == 0:
        index = i
        if (reverse):
          index = len(self.rotors) - i -1
          
        self.rotors[index].click()
        
  def possiblityNumber(self):
    return self.rotorSize ** len(self.rotors)
  
  def resetRotor(self):
    """
    Resets all rotors to default positions
    """
    self.turnNumber = 0
    for i in range(len(self.rotors)):
        self.rotors[i].resetRotor()

  def __repr__(self):
    return str(self.rotors)

  def visualizeEnigma(self):
    """
    Visualizes the current state of enigma
    """
    for i in range(self.rotorSize):
      ch = chr(ord('A')+i)
      
      for k in range(len(self.rotors)):
        print(ch, end="-")
        mapped = self.rotors[k].encryptLetter(ch)
        print(mapped, end=" ")
      print()