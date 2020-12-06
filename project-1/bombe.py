from enigma import Enigma
import time
import random

class Bombe:
  
  def __init__(self, guideWords, *rotorLetters):
    rotorLetterList = list(rotorLetters)
    random.shuffle(rotorLetterList)
    print("rotorLetterList", rotorLetterList)
    self.enigmas = self.enigmaPossibilities([], rotorLetterList)
    self.guideWords = guideWords

  def enigmaPossibilities(self, rotorOrder, rotorLetters):
    if (len(rotorLetters)==0):
      return [Enigma(*rotorOrder)]

    enigmaList = []
    for i in range(len(rotorLetters)):
      newRotorOrder = list.copy(rotorOrder)
      newRotorOrder.append(rotorLetters[i])
      remainingLetters = list.copy(rotorLetters)
      del remainingLetters[i]
      enigmaList.extend(self.enigmaPossibilities(newRotorOrder, remainingLetters))
    
    
    return enigmaList

  def crack(self, ciphertext, earlyFinish = False, include_all_words = True, match_threshold = 3):

    crackedList = []
    crackStart = time.time()
    for enigma in self.enigmas:
      sectionStart = time.time()
      print("Trying one of the orders with: ", enigma.possiblityNumber(), " possibilities.")
      enigma.resetRotor()
      for i in range(enigma.possiblityNumber()):
        message = enigma.decryptWithTurn(ciphertext, i)
        
        matchedWords = []
        
        for word in self.guideWords:
          if word in message:
            matchedWords.append(word)

        if len(matchedWords) == len(self.guideWords) or (not include_all_words and len(matchedWords) >= match_threshold):
          crackedList.append(message)
          print(message)
          if earlyFinish:
            break

      sectionEnd = time.time()
      print("Finished in: ", sectionEnd - sectionStart)

    crackEnd = time.time()
    print("Cracked in: ",crackEnd - crackStart, " seconds")
    return crackedList
  
  def __repr__(self):
    return str(self.enigmas)