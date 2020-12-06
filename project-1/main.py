# Enigma
from rotor import Rotor
from enigma import Enigma
from bombe import Bombe

def RotorTest():
  r = Rotor("FABECD")
  print(r.encryptLetter('D')=='E')
  print(r.decryptLetter('E')=='D')
  r.click()
  print(r.encryptLetter('D')=='C')
  print(r.decryptLetter('E')=='C')

def RotorTest1():
  r = Rotor("CAB")
  print(r.decryptLetter(r.encryptLetter('A'))=='A')
  print(r.decryptLetter(r.encryptLetter('B'))=='B')
  print(r.decryptLetter(r.encryptLetter('C'))=='C')

def RotorClickTest():
  r = Rotor("CAB")
  for i in range(4):
    r.click()
    print(str(r))
    print(r.decryptLetter(r.encryptLetter('A'))=='A')

def EnigmaTest():
  enigma = Enigma("CAB", "BAC", "BCA")
  print(enigma.encrypt('ABC') == 'AAA') # should ACB
  print(enigma.decrypt('ACB') == 'CBA')

  print(enigma.encrypt('CAB') == 'CCC')
  print(enigma.decrypt('CAB') == 'AAA')

def EnigmaTest1():
  enigma = Enigma("CAB", "BAC", "BCA")
  messages = ['ABC','CAB', 'BCA']
  for message in messages:
    enigma.resetRotor()
    encrypted_m= enigma.encrypt(message)
    enigma.resetRotor()
    print(enigma.decrypt(encrypted_m)==message)


def EnigmaSpecialTest():
  enigma = Enigma("SHBMFWEIQRODTAVXCPYZUJKGNL", "GYRFNUCZLQDWMKHSJOEPBVITXA", "MSEWGQHDPRFNXATOIBUJLCZVYK")
  
  cipherText = "OQMTANMGPABQSDAKAUFXXGJBSPHBZXHLXMBNOHTNQZQGDBMIQNZJ"
  cipherText2 = "MXNMFKPDVWDPIMPYACVYZUGUWGPVGAOXCDZDGYTLATOIBUJLCZVYNXATOIBUJLCZVYKMSEWGQHDPRFIBUJLCZVYKMSEWGQHDPRFNXATOWGQHDPRFNXATOIBUJLCZVYKMSEZVYKMSEWGQHDPRFNXATOIBUJLCXATOIBUJLCZVYKMSEWGQHDPRFNFNXATOIBUJLCZVYKMSEWGQHDPRDPRFNXATOIBUJLCZVYKMSEWGQHUJLCZVYKMSEWGQHDPRFNXATOIBRFNXATOIBUJLCZVYKMSEWGQHDPTOIBUJLCZVYKMSEWGQHDPRFNXAGQHDPRFNXATOIBUJLCZVYKMSEWOIBUJLCZVYKMSEWGQHDPRFNXATSEWGQHDPRFNXATOIBUJLCZVYKMCZVYKMSEWGQHDPRFNXATOIBUJLPRFNXATOIBUJLCZVYKMSEWGQHDJLCZVYKMSEWGQHDPRFNXATOIBUVYKMSEWGQHDPRFNXATOIBUJLCZMSEWGQHDPRFNXATOIBUJLCZVYKHDPRFNXATOIBUJLCZVYKMSEWGQYKMSEWGQHDPRFNXATOIBUJLCZVBUJLCZVYKMSEWGQHDPRFNXATOIQHDPRFNXATOIBUJLCZVYKMSEWGATOIBUJLCZVYKMSEWGQHDPRFNXLCZVYKMSEWGQHDPRFNXATOIBUJZ"
  print(enigma.decrypt(cipherText))
  enigma.resetRotor()
  print(enigma.decrypt(cipherText2))

def EnigmaClickTest():
  enigma = Enigma("CAB", "BAC", "BCA")
  print(str(enigma))
  for i in range(27):
    enigma.click()
    print(str(enigma))

def BombeTest():
  bombe = Bombe(["MINE", "ONE"], "SHBMFWEIQRODTAVXCPYZUJKGNL", "GYRFNUCZLQDWMKHSJOEPBVITXA", "MSEWGQHDPRFNXATOIBUJLCZVYK")
  cipherText = "NPWCDPBRIVDZGARYLECHBTOCKJCMJVDRFZEYFWJTRZLPDEVDHIJXYHRBRJTVVQCFDQUWHRQKYPYFAJJKSDEJVOVZNWYFYINBPBSNHZAGDACJRYRLLJAWCJKHTEVATAAZWVUHSBTCKBVHTNSGFDPHGIZDSZXMBSIKWLMMISUQNWCRPSHSNFAALBQNMKESIHCPGVRTRFTPRYTRIRMNYMVSLEKAPRISAUSTRXQFVCLYWXZLLXHHKHJJUTPKHBTFENHMFRLFLUHYQJSCMNEBB"
  bombe.crack(cipherText)

def BombeTestFast():
  rotorLetters = ["SHBMFWEIQRODTAVXCPYZUJKGNL", "GYRFNUCZLQDWMKHSJOEPBVITXA", "MSEWGQHDPRFNXATOIBUJLCZVYK"]
  bombe = Bombe(["MINE", "ONE"], *rotorLetters)
  cipherText = "NPWCDPBRIVDZGARYLECHBTOCKJCMJVDRFZEYFWJTRZLPDEVDHIJXYHRBRJTVVQCFDQUWHRQKYPYFAJJKSDEJVOVZNWYFYINBPBSNHZAGDACJRYRLLJAWCJKHTEVATAAZWVUHSBTCKBVHTNSGFDPHGIZDSZXMBSIKWLMMISUQNWCRPSHSNFAALBQNMKESIHCPGVRTRFTPRYTRIRMNYMVSLEKAPRISAUSTRXQFVCLYWXZLLXHHKHJJUTPKHBTFENHMFRLFLUHYQJSCMNEBB"
  bombe.crack(cipherText, earlyFinish=True)

if __name__ == '__main__':

  RotorTest()
  RotorTest1()
  RotorClickTest()
  print("Rotor tests passed")

  EnigmaTest()
  EnigmaTest1()
  # EnigmaSpecialTest()
  # EnigmaClickTest()
  print("Enigma tests passed")

  BombeTest()
  # BombeTestFast()




