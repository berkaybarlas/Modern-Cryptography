from enigma import Enigma
from bombe import Bombe
import os
import sys
import time

DEFAULT_ROTOR_LETTERS = ["SHBMFWEIQRODTAVXCPYZUJKGNL", "GYRFNUCZLQDWMKHSJOEPBVITXA", "MSEWGQHDPRFNXATOIBUJLCZVYK"]
WORD_LIST_FILE = "wordList.txt"
DEFAULT_TARGET_FILE = "targetFile.txt"

def getWordList(fileName): 
  rF = open(fileName, "r")
  lines = rF.readlines()
  rF.close()
  return [word.rstrip() for word in lines]

def getTargetMessage(fileName): 
  rF = open(fileName, "r")
  lines = rF.readlines()
  rF.close()
  return [word.rstrip().upper().replace(" ", "") for word in lines]

def generateAllRotorLetters():
  """
  This function should create all the possible letter combinations
  """
  pass
if __name__ == '__main__':

  targetFile = DEFAULT_TARGET_FILE
  wordFile = WORD_LIST_FILE
  rotorLetters = []
  

  if (len(sys.argv) > 1):
    targetFile = sys.argv[1]
    if (len(sys.argv) > 2):
      wordFile = sys.argv[2]
      if (len(sys.argv) > 3):
        # Get initial rotor letters
        for i in range(3,len(sys.argv)):
          rotorLetters.append(sys.argv[i])

  guideWords = getWordList(wordFile)
  targetMessages = getTargetMessage(targetFile)
  print("Words to look in message:", guideWords)
  

  if len(rotorLetters) == 0:
    print("You didn't specified rotorletter, example values will be used for but it's not recommended")
    rotorLetters = DEFAULT_ROTOR_LETTERS

  bombe = Bombe(guideWords, *rotorLetters)

  for message in targetMessages:
    print("For target message:", message)
    print("Possible cracks are:", bombe.crack(message, include_all_words=False))
    