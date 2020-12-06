from enigma import Enigma
from os import path
import os
import sys
import time

chatFileFolder = "out/"
TIMEOUT_COUNT = 10
QUIT = False
first_agent = False
# Default values for rotor letters
DEFAULT_ROTOR_LETTERS = ["SHBMFWEIQRODTAVXCPYZUJKGNL", "GYRFNUCZLQDWMKHSJOEPBVITXA", "MSEWGQHDPRFNXATOIBUJLCZVYK"]

TARGET_FILE_LINES = []
def delete_last_line():
  "Use this function to delete the last line in the STDOUT"

  #cursor up one line
  sys.stdout.write('\x1b[1A')

  #delete last line
  sys.stdout.write('\x1b[2K')

def waitForTargetFile(targetFile):
  global first_agent
  timeoutCounter = 0
  # Wait for other end of line 
  while not path.exists(targetChatFile):
    first_agent = True
    if timeoutCounter == TIMEOUT_COUNT:
      print("Connection timeout try again later")
      sys.exit(1)
    print("Waiting for other person on line")
    time.sleep(2)
    timeoutCounter+=1
  timeoutCounter = 0

def initChatFolder():
  if not path.exists(chatFileFolder):
    os.mkdir(chatFileFolder)

def isNewMessageRecieved(fileName):
  global TARGET_FILE_LINES
  rF = open(fileName, "r")
  currentLines = rF.readlines()
  rF.close()

  if len(TARGET_FILE_LINES) == len(currentLines): # or (len(TARGET_FILE_LINES) == 0 and len(currentLines) > 1):
    time.sleep(1)
    return False
  TARGET_FILE_LINES = currentLines    
  if len(currentLines) == 0:
    return False
  return True

def getLastMessage(fileName):
  rF = open(fileName, "r")
  lines = rF.readlines()
  rF.close()
  return lines[len(lines)-1].rstrip()

def sendMessage(fileName, message):
  wF = open(fileName, "a")
  wF.write(message + "\n")
  wF.close()

def sendEncryptedMessage(fileName, message, enigma):
  encryptedMessage = encryptMessage(message, enigma)
  print("Encrypted Message:", encryptedMessage)
  sendMessage(fileName, encryptedMessage)
  
def decryptMessage(message, enigma):
  return enigma.decrypt(message)

def encryptMessage(message, enigma):
  # Remove spaces and make message uppercase
  return enigma.encrypt(message.upper().replace(" ", ""))

def removeAndCreateChatFile(fileName):
  if path.exists(fileName):
    os.remove(fileName)
  wF = open(fileName, "w")
  wF.close()

if __name__ == '__main__':

  initChatFolder()

  agentName = ""
  targetAgent = ""
  rotorLetters = []

  # Try to get arguments from command line
  if (len(sys.argv) > 1):
    agentName = sys.argv[1]
    if (len(sys.argv) > 2):
      targetAgent = sys.argv[2]
      if (len(sys.argv) > 3):
        for i in range(3,len(sys.argv)):
          rotorLetters.append(sys.argv[i])
    
  # Ask if not given with command line
  if agentName == "":
    agentName = input("Enter your name: ")
  else: 
    print("Hi", agentName)

  if targetAgent == "":
    targetAgent = input("Enter a person name to Chat: ")
  else:
    print("You are going to chat with ", targetAgent)

  chatFile = chatFileFolder + agentName.rstrip() + ".txt"
  targetChatFile = chatFileFolder + targetAgent.rstrip() + ".txt"

  # Open file to write messages, clear previus ones with "w"
  removeAndCreateChatFile(chatFile)
  
  waitForTargetFile(targetChatFile)


  """
    Create Enigma for security
  """
  if len(rotorLetters) == 0:
    print("You didn't specified rotorletter, default will be used for but it's not recommended")
    rotorLetters = DEFAULT_ROTOR_LETTERS

  print("rotorLetters", rotorLetters)
  enigma = Enigma(*rotorLetters)

  if not first_agent:
    isFirstAgent = input("There is a conflict. Are you the first person to send message? y/n: ")
    if isFirstAgent.rstrip() == "y":
      first_agent = True
    else:
      first_agent = False

  if first_agent:
    # Reset target file if it's not first agent
    removeAndCreateChatFile(targetChatFile)
    message = input("Enter first message: ")
    # Encrypt and send message
    sendEncryptedMessage(chatFile, message, enigma)
  
  print("Waiting for message...")

  while not QUIT:
    if isNewMessageRecieved(targetChatFile):
      delete_last_line()
      recievedMessage = getLastMessage(targetChatFile)
      print("Recieved Encrpyted Message:", recievedMessage)
      decryptedMessage = decryptMessage(recievedMessage, enigma)
      print("Recieved Message:", decryptedMessage)

      message = input("Enter your message: ")
      # Encrypt and send message
      
      sendEncryptedMessage(chatFile, message, enigma)
      if message.rstrip() == "QUIT":
        QUIT = True
      print("Waiting for message...")

  print("Closing...")
  