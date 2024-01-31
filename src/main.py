import random

# Create an array of strings that contain prefixes
listprefixes = [
    "anti", "de", "dis", "en", "fore", "inter", "mid", "mis", "non", "over",
    "pre", "re", "semi", "sub", "trans", "un", "up", "under", "post", "pro"
]

# create an array of strings that contain suffixes
listsuffixes = [
    "act", "al", "ance", "ant", "ate", "ble", "do", "eal", "eous", "er",
    "esque", "ful", "ic", "ing", "ion", "ish", "ive", "less", "ly", "ment"
]

# create an array of strings that contain the root word
listroots = [
    "ambi", "aud", "auto", "bene", "mal", "mit", "mort", "nas", "port", "puel",
    "sens", "sent", "spect", "struct", "tic", "vic", "vul"
    "voc", "hypo", "hyper"
]

# create definitions
listprefixesdef = [ "against ", "before ", "between ", "in between ", "not ",
    "not ", "above ", "before ", "again ", "kinda ", "under", "change ", "one ",
    "above ", "beneath ", "after ", "for "
]

listsuffixesdef = [
    "to do ", "assimilated before ", "doing something ", "against ",
    "characteristics of ", "ability of ", "act ", "pertaining to ", "composed of ",
    "doing ", "resembling ", "full of ", "characterized by ", "characterized by ",
    "characterized by ", "kind of ", "tending to ", "without ", "in a manner ",
    "enjoyment "
]

listrootsdef = [
    "both ", "sound ", "automatic ", "good ", "bad ", "matter ", "death ", "nose ",
    "to carry ", "biology ", "sense ", "send ", "view ", "structure ", "doing ",
    "tend to ", "without ", "in a way ", "joy ", "under ", "over "
]

count = 10

while count > 0:
  x = random.randint(0, len(listprefixes)-1)
  y = random.randint(0, len(listsuffixes)-1)
  z = random.randint(0, len(listroots)-1)
  word = listprefixes[x] +  listroots[z] +  listsuffixes[y]
  print(word)

  definition = listprefixesdef[x] +listrootsdef[z] + listsuffixesdef[y]
  print(definition)
  count -= 1
