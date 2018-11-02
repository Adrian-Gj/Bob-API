def istime(text):
    timepts = 0
    locpts = 0
    if 'noon' in text:
        timepts += 1
    if 'afternoon' in text:
        timepts += 1
    if 'midnight' in text:
        timepts += 1
    if 'th of' in text:
        timepts += 1
    if 'january' in text:
        timepts += 1
    if 'february' in text:
        timepts += 1
    if 'march' in text:
        timepts += 1
    if 'april' in text:
        timepts += 1
    if 'may' in text:
        timepts += 1
    if 'june' in text:
        timepts += 1
    if 'july' in text:
        timepts += 1
    if 'august' in text:
        timepts += 1
    if 'september' in text:
        timepts += 1
    if 'november' in text:
        timepts += 1
    if 'december' in text:
        timepts += 1
    if 'monday' in text:
        timepts += 1
    if 'tuesday' in text:
        timepts += 1
    if 'wednesday' in text:
        timepts += 1
    if 'thursday' in text:
        timepts += 1
    if 'friday' in text:
        timepts += 1
    if 'saturday' in text:
        timepts += 1
    if 'sunday' in text:
        timepts += 1
    if ' day' in text:
        timepts += 5
    if 'day ' in text:
        timepts += 5
    if ' night' in text:
        timepts += 5
    if 'night ' in text:
        timepts += 5
    if text.endswith(" night"):
        timepts += 40
    if text.endswith(" day"):
        timepts += 40
    if text.endswith(" noon"):
        timepts += 30
    if text.endswith(" afternoon"):
        timepts += 30
    if text.endswith(" midnight"):
        timepts += 30
    if "1" in text:
        timepts += 1
    if "2" in text:
        timepts += 1
    if "3" in text:
        timepts += 1
    if "4" in text:
        timepts += 1
    if "5" in text:
        timepts += 1
    if "6" in text:
        timepts += 1
    if "7" in text:
        timepts += 1
    if "8" in text:
        timepts += 1
    if "9" in text:
        timepts += 1

        
    if 'street' in text:
        locpts += 20
    if 'avenue' in text:
        locpts += 20
    if text.endswith(" street"):
        locpts += 40
    if text.endswith(" avenue"):
        locpts += 40

    return timepts>locpts

def q_type(text):
    if text.startswith("what is "):
        return "def1"
    elif text.startswith("what are "):
        return "def1"
    elif text.startswith("what am "):
        return "def1"
    elif text.startswith("what was "):
        return "def2"
    elif text.startswith("what were "):
        return "def2"
    elif text.startswith("who is "):
        return "def1"
    elif text.startswith("who are "):
        return "def1"
    elif text.startswith("what am "):
        return "def1"
    elif text.startswith("who was "):
        return "def2"
    elif text.startswith("who were "):
        return "def2"
    elif text.startswith("when is "):
        return "time1"
    elif text.startswith("when am "):
        return "time1"
    elif text.startswith("when are "):
        return "time1"
    elif text.startswith("when was "):
        return "time2"
    elif text.startswith("when were "):
        return "time2"
    elif text.startswith("what time is "):
        return "time1"
    elif text.startswith("what time am "):
        return "time1"
    elif text.startswith("what time are "):
        return "time1"
    elif text.startswith("what time was "):
        return "time2"
    elif text.startswith("what time were "):
        return "time2"
    elif text.startswith("where is "):
        return "loc1"
    elif text.startswith("where am "):
        return "loc1"
    elif text.startswith("where was "):
        return "loc2"
    elif text.startswith("how is "):
        return "def1"
    elif text.startswith("how are "):
        return "def1"
    elif text.startswith("how am "):
        return "def1"
    elif text.startswith("how was "):
        return "def2"
    elif text.startswith("how were "):
        return "def2"
def q_split(text):
    x = ""
    if text.startswith("what is "):
        x = text[8:]
    elif text.startswith("what are "):
        x = text[9:]
    if text.startswith("what am "):
        x = text[8:]
    elif text.startswith("what was "):
        x = text[9:]
    elif text.startswith("what were "):
        x = text[10:]
    elif text.startswith("who is "):
        x = text[7:]
    elif text.startswith("who are "):
        x = text[8:]
    elif text.startswith("who am "):
        x = text[7:]
    elif text.startswith("who was "):
        x = text[8:]
    elif text.startswith("who were "):
        x = text[9:]
    elif text.startswith("when is "):
        x = text[8:]
    elif text.startswith("when am "):
        x = text[8:]
    elif text.startswith("when are "):
        x = text[9:]
    elif text.startswith("when was "):
        x = text[9:]
    elif text.startswith("when were "):
        x = text[10:]
    elif text.startswith("what time is "):
        x = text[13:]
    elif text.startswith("what time am "):
        x = text[13:]
    elif text.startswith("what time are "):
        x = text[14:]
    elif text.startswith("what time was "):
        x = text[14:]
    elif text.startswith("what time were "):
        x = text[15:]
    elif text.startswith("where is "):
        x = text[9:]
    elif text.startswith("where am "):
        x = text[9:]
    elif text.startswith("where was "):
        x = text[10:]
    elif text.startswith("how is "):
        x = text[7:]
    elif text.startswith("how are "):
        x = text[8:]
    elif text.startswith("how am "):
        x = text[7:]
    elif text.startswith("how was "):
        x = text[8:]
    elif text.startswith("how were "):
        x = text[9:]

    if x == "it":
        x=it
    if x == "they":
        x=it
    return x
def q_t1_proc(text):

    x = text
    x = x.replace("the ", "")
    x = x.replace("current ", "")
    x = x.replace("value of ", "")
    return x

def findnth(string, substring, n):
    parts = string.split(substring, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(string) - len(parts[-1]) - len(substring)
def has_no(no):
    if '0' in no:
        return True
    if '1' in no:
        return True
    if '2' in no:
        return True
    if '3' in no:
        return True
    if '4' in no:
        return True
    if '5' in no:
        return True
    if '6' in no:
        return True
    if '7' in no:
        return True
    if '8' in no:
        return True
    if '9' in no:
        return True
    return False