
import random

### !Configure! ###

# If you would like to add some words go ahead *NOTE* These trigger words are quite strict so feel free to change and delete some
# Resource found at [reddit.com/r/copypasta/comments/fca22g/every_swear_word_in_alphabetical_order/]
slur_list = ["anus", "arse", "arsehole", "ass", "ass-hat", "ass-jabber", "ass-pirate", "assbag", "assbandit", "assbanger", "assbite", "assclown", "asscock", "asscracker", "asses", "assface", "assfuck", "assfucker", "assgoblin", "asshat", "asshead", "asshole", "asshopper", "assjacker", "asslick", "asslicker", "assmonkey", "assmunch", "assmuncher", "assnigger", "asspirate", "assshit", "assshole", "asssucker", "asswad", "asswipe", "axwound", "bampot", "bastard", "beaner", "bitch", "bitchass", "bitches", "bitchtits", "bitchy", "blow", "job", "blowjob", "bollocks", "bollox", "boner", "brotherfucker", "bullshit", "bumblefuck", "butt", "plug", "butt-pirate", "buttfucka", "buttfucker", "camel", "toe", "carpetmuncher", "chesticle", "chinc", "chink", "choad", "chode", "clit", "clitface", "clitfuck", "clusterfuck", "cock", "cockass", "cockbite", "cockburger", "cockface", "cockfucker", "cockhead", "cockjockey", "cockknoker", "cockmaster", "cockmongler", "cockmongruel", "cockmonkey", "cockmuncher", "cocknose", "cocknugget", "cockshit", "cocksmith", "cocksmoke", "cocksmoker", "cocksniffer", "cocksucker", "cockwaffle", "coochie", "coochy", "coon", "cooter", "cracker", "cum", "cumbubble", "cumdumpster", "cumguzzler", "cumjockey", "cumslut", "cumtart", "cunnie", "cunnilingus", "cunt", "cuntass", "cuntface", "cunthole", "cuntlicker", "cuntrag", "cuntslut", "dago", "damn", "deggo", "dick", "dick-sneeze", "dickbag", "dickbeaters", "dickface", "dickfuck", "dickfucker", "dickhead", "dickhole", "dickjuice", "dickmilk", "dickmonger", "dicks", "dickslap", "dicksucker", "dicksucking", "dicktickler", "dickwad", "dickweasel", "dickweed", "dickwod", "dike", "dildo", "dipshit", "doochbag", "dookie", "douche", "douche-fag", "douchebag", "douchewaffle", "dumass", "dumb", "ass", "dumbass", "dumbfuck", "dumbshit", "dumshit", "dyke", "fag", "fagbag", "fagfucker", "faggit", "faggot", "faggotcock", "fagtard", "fatass", "fellatio", "feltch", "flamer", "fuck", "fuckass", "fuckbag", "fuckboy", "fuckbrain", "fuckbutt", "fuckbutter", "fucked", "fucker", "fuckersucker", "fuckface", "fuckhead", "fuckhole", "fuckin", "fucking", "fucknut", "fucknutt", "fuckoff", "fucks", "fuckstick", "fucktard", "fucktart", "fuckup", "fuckwad", "fuckwit", "fuckwitt", "fudgepacker", "gay", "gayass", "gaybob", "gaydo", "gayfuck", "gayfuckist", "gaylord", "gaytard", "gaywad", "goddamn", "goddamnit", "gooch", "gook", "gringo", "guido", "handjob", "hard on", "heeb", "hell", "ho", "hoe", "homo", "homodumbshit", "honkey", "humping", "jackass", "jagoff", "jap", "jerk off", "jerkass", "jigaboo", "jizz", "jungle bunny", "junglebunny", "kike", "kooch", "kootch", "kraut", "kunt", "kyke", "lameass", "lardass", "lesbian", "lesbo", "lezzie", "mcfagget", "mick", "minge", "mothafucka", "mothafuckin'", "motherfucker", "motherfucking", "muff", "muffdiver", "munging", "negro", "nigaboo", "nigga", "nigger", "niggers", "niglet", "nut sack", "nutsack", "paki", "panooch", "pecker", "peckerhead", "penis", "penisbanger", "penisfucker", "penispuffer", "piss", "pissed", "pissed off", "pissflaps", "polesmoker", "pollock", "poon", "poonani", "poonany", "poontang", "porch monkey", "porchmonkey", "prick", "punanny", "punta", "pussies", "pussy", "pussylicking", "puto", "queef", "queer", "queerbait", "queerhole", "renob", "rimjob", "ruski", "sand nigger", "sandnigger", "schlong", "scrote", "shit", "shitass", "shitbag", "shitbagger", "shitbrains", "shitbreath", "shitcanned", "shitcunt", "shitdick", "shitface", "shitfaced", "shithead", "shithole", "shithouse", "shitspitter", "shitstain", "shitter", "shittiest", "shitting", "shitty", "shiz", "shiznit", "skank", "skeet", "skullfuck", "slut", "slutbag", "smeg", "snatch", "spic", "spick", "splooge", "spook", "suckass", "tard", "testicle", "thundercunt", "tit", "titfuck", "tits", "tittyfuck", "twat", "twatlips", "twats", "twatwaffle", "unclefucker", "va-j-j", "vag", "vagina", "vajayjay", "vjayjay", "wank", "wankjob", "wetback", "whore", "whorebag", "whoreface", "wop"]
'''
# Another way to get slurs. I will continue to keep the words hard coded, for the meantime.
with open('slurs.txt', 'r') as slur_file:
    slurs = slur_file.read()
'''

text_string = input(": ")

##===-- Main Fuction
# Loop through my slur list
for i in slur_list:
    # Split my text string into a list of all the words (split by spaces)
    text_list = text_string.split(' ')

    # Go through each word in my "text_string" list
    for j in range(len(text_list)):

        # If a slur is found in the list item (string type), it returns 0... else it returns -1. Also, lowercase the word (for the if-statement) just to compare to the slur word
        if text_list[j].lower().find(i) == 0:

            # Determines if a non-alpha character is in front or after the word and then puts it back. 
            punctuation = [True,text_list[j][0]] if not text_list[j][0].isalpha() else [False,text_list[j][-1] if not text_list[j][-1].isalpha() else '']

            # IF your string is less than or equal to your slur length + length of punctuation 
            if len(text_list[j]) <= len(i)+len(punctuation[1]):
                if punctuation[0]:
                    text_list[j] = punctuation[1]+'*'
                else:
                    text_list[j] = '*'*len(text_list[j])+punctuation[1]

    # Join all the words back together.
    text_string=' '.join(text_list)

# print filtered words
print(text_string)