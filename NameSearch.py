import argparse
import urllib.parse

parser = argparse.ArgumentParser(
                    prog='NameSearch',
                    description="search people's name in google",
                    epilog='')

parser.add_argument('--firstname', metavar='', type=str, help="Person's first name")
parser.add_argument('--lastname', metavar='', type=str, help="Person's first last")
parser.add_argument('--words', metavar='', type=argparse.FileType('r'), help="Add extra words for search")




args = parser.parse_args()

c = " _"
c = [""] + [*c]

words = None

if args.words != None:
    words = args.words.readlines()

def get_search_1(firstname, lastname, words):
    search= ""

    for char in c:
        search += '"' + firstname + char + lastname + '"' + " OR "
        search += '"' + lastname + char + firstname + '"' + " OR "

    search = search[:-4]
    
    if words != None:
        
        wordSearch = ""
        for word in words:
            wordSearch += f'"{word}" OR '
            
        wordSearch = wordSearch[:-4]
            
        search = f"({search}) AND ({wordSearch})"

    return 'https://www.google.com/search?q=' + urllib.parse.quote(search)

def get_search_2(firstname, lastname, words):
    search= ""

    search += f'"{firstname}" AND "{lastname}" '
    
    if words != None:
        wordSearch = ""
        for word in words:
            wordSearch += f'"{word}" OR '
            
        wordSearch = wordSearch[:-4]
            
        search = f"({search}) AND ({wordSearch})"

    return 'https://www.google.com/search?q=' + urllib.parse.quote(search)




print("""
   BY
 ▄████▄   ██▀███   ██▓  ▄████ 
▒██▀ ▀█  ▓██ ▒ ██▒▓██▒ ██▒ ▀█▒
▒▓█    ▄ ▓██ ░▄█ ▒▒██▒▒██░▄▄▄░
▒▓▓▄ ▄██▒▒██▀▀█▄  ░██░░▓█  ██▓
▒ ▓███▀ ░░██▓ ▒██▒░██░░▒▓███▀▒
░ ░▒ ▒  ░░ ▒▓ ░▒▓░░▓   ░▒   ▒ 
  ░  ▒     ░▒ ░ ▒░ ▒ ░  ░   ░ 
░          ░░   ░  ▒ ░░ ░   ░ 
░ ░         ░      ░        ░ 
░                             
""")
print("\nLinks:\n\n")

print("1:    " + get_search_1(args.firstname, args.lastname, words) + "\n")
print("2:    " + get_search_2(args.firstname, args.lastname, words) + "\n")




