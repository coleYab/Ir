import re
translation_table= {
    "": "X", "ሀ": "he", "ሁ": "hu", "ሂ": "hi",
    "ሃ": "he", "ሄ": "hE", "ህ": "h", "ሆ": "ho",
    "ለ": "le", "ሉ": "lu", "ሊ": "li", "ላ": "la",
    "ሌ": "lE", "ል": "l", "ሎ": "lo", "ሏ": "lWa",
    "ሐ": "he", "ሑ": "hu", "ሒ": "hi", "ሓ": "he",
    "ሔ": "hE", "ሕ": "h", "ሖ": "ho", "ሗ": "hWa",
    "መ": "me", "ሙ": "mu", "ሚ": "mi", "ማ": "ma",
    "ሜ": "mE", "ም": "m", "ሞ": "mo", "ሟ": "mWa",
    "ሠ": "se", "ሡ": "su", "ሢ": "si", "ሣ": "sa",
    "ሤ": "sE", "ሥ": "s", "ሦ": "so", "ሧ": "sWa",
    "ረ": "re", "ሩ": "ru", "ሪ": "ri", "ራ": "ra",
    "ሬ": "rE", "ር": "r", "ሮ": "ro", "ሯ": "rWa",
    "ሰ": "se", "ሱ": "su", "ሲ": "si", "ሳ": "sa",
    "ሴ": "sE", "ስ": "s", "ሶ": "so", "ሷ": "sWa",
    "ሸ": "xe", "ሹ": "xu", "ሺ": "xi", "ሻ": "xa",
    "ሼ": "xE", "ሽ": "x", "ሾ": "xo", "ሿ": "xWa",
    "ቀ": "qe", "ቁ": "qu", "ቂ": "qi", "ቃ": "qa",
    "ቄ": "qE", "ቅ": "q", "ቆ": "qo", "ቈ": "qWe",
    "ቊ": "qu", "ቋ": "qWa", "ቌ": "qWE", "ቍ": "qW",
    "በ": "be", "ቡ": "bu", "ቢ": "bi", "ባ": "ba",
    "ቤ": "bE", "ብ": "b", "ቦ": "bo", "ቧ": "bWa",
    "ቨ": "ve", "ቩ": "vu", "ቪ": "vi", "ቫ": "va",
    "ቬ": "vE", "ቭ": "v", "ቮ": "vo", "ቯ": "vWa",
    "ተ": "te", "ቱ": "tu", "ቲ": "ti", "ታ": "ta",
    "ቴ": "tE", "ት": "t", "ቶ": "to", "ቷ": "tWa",
    "ቸ": "ce", "ቹ": "cu", "ቺ": "ci", "ቻ": "ca",
    "ቼ": "cE", "ች": "c", "ቾ": "co", "ቿ": "cWa",
    "ኀ": "he", "ኁ": "hu", "ኂ": "hi", "ኃ": "he",
    "ኄ": "hE", "ኅ": "h", "ኆ": "ho", "ኈ": "hWe",
    "ኊ": "hWi", "ኋ": "hWa", "ኌ": "hWE", "ኍ": "hW",
    "ነ": "ne", "ኑ": "nu", "ኒ": "ni", "ና": "na",
    "ኔ": "nE", "ን": "n", "ኖ": "no", "ኗ": "nWa",
    "ኘ": "Ne", "ኙ": "Nu", "ኚ": "Ni", "ኛ": "Na",
    "ኜ": "NE", "ኝ": "N", "ኞ": "No", "ኟ": "NWa",
    "አ": "a", "ኡ": "u", "ኢ": "i", "ኣ": "a",
    "ኤ": "E", "እ": "I", "ኦ": "o", "ኧ": "e",
    "ከ": "ke", "ኩ": "ku", "ኪ": "ki", "ካ": "ka",
    "ኬ": "kE", "ክ": "k", "ኮ": "ko", "ኰ": "ko",
    "ኲ": "kWi", "ኳ": "kWa", "ኴ": "kWE", "ኵ": "kW",
    "ኸ": "Ke", "ኹ": "hu", "ኺ": "hi", "ኻ": "he",
    "ኼ": "hE", "ኽ": "h", "ኾ": "ho", "ዀ": "KWe",
    "ዂ": "KWi", "ዃ": "KWa", "ዄ": "KWE", "ዅ": "KW",
    "ወ": "we", "ዉ": "wu", "ዊ": "wi", "ዋ": "wa",
    "ዌ": "wE", "ው": "w", "ዎ": "wo", "ዐ": "e",
    "ዑ": "u", "ዒ": "i", "ዓ": "e", "ዔ": "E",
    "ዕ": "e", "ዖ": "o", "ዘ": "ze", "ዙ": "zu",
    "ዚ": "zi", "ዛ": "za", "ዜ": "zE", "ዝ": "z",
    "ዞ": "zo", "ዟ": "zWa", "ዠ": "Ze", "ዡ": "Zu",
    "ዢ": "Zi", "ዣ": "Za", "ዤ": "ZE", "ዥ": "Z",
    "ዦ": "Zo", "ዧ": "ZWa", "የ": "ye", "ዩ": "yu",
    "ዪ": "yi", "ያ": "ya", "ዬ": "yE", "ይ": "y",
    "ዮ": "yo", "ደ": "de", "ዱ": "du", "ዲ": "di",
    "ዳ": "da", "ዴ": "dE", "ድ": "d", "ዶ": "do",
    "ዷ": "dWa", "ጀ": "je", "ጁ": "ju", "ጂ": "ji",
    "ጃ": "ja", "ጄ": "jE", "ጅ": "j", "ጆ": "jo",
    "ጇ": "jWa", "ገ": "ge", "ጉ": "gu", "ጊ": "gi",
    "ጋ": "ga", "ጌ": "gE", "ግ": "g", "ጎ": "go",
    "ጐ": "go", "ጒ": "gWi", "ጓ": "gWa", "ጔ": "gWE",
    "ጕ": "gW", "ጠ": "Te", "ጡ": "Tu", "ጢ": "Ti",
    "ጣ": "Ta", "ጤ": "TE", "ጥ": "T", "ጦ": "To",
    "ጧ": "TWa", "ጨ": "Ce", "ጩ": "Cu", "ጪ": "Ci",
    "ጫ": "Ca", "ጬ": "CE", "ጭ": "C", "ጮ": "Co",
    "ጯ": "CWa", "ጰ": "Pe", "ጱ": "Pu",   "ጲ": "Pi",
    "ጳ": "Pa", "ጴ": "PE", "ጵ": "P", "ጶ": "Po",
    "ጷ": "PWa", "ጸ": "SSe", "ጹ": "SSu", "ጺ": "SSi",
    "ጻ": "SSa", "ጼ": "SSE", "ጽ": "SS", "ጾ": "SSo",
    "ጿ": "SSWa", "ፀ": "SSe", "ፁ": "SSu", "ፂ": "SSi",
    "ፃ": "SSa", "ፄ": "SSE", "ፅ": "SS", "ፆ": "SSo",
    "ፈ": "fe", "ፉ": "fu", "ፊ": "fi", "ፋ": "fa",
    "ፌ": "fE", "ፍ": "f", "ፎ": "fo", "ፏ": "fWa",
    "ፐ": "pe", "ፑ": "pu", "ፒ": "pi", "ፓ": "pa",
    "ፔ": "pE", "ፕ": "p", "ፖ": "po", "ፗ": "pWa",
}


def to_english(word: str) -> str:
    translated_text = ""

    for i in word:
        if i in translation_table.keys():
            translated_text += translation_table[i]

    return translated_text


def to_amharic(word: str) -> str:
    trans_word = ''
    tokens = [word[i:i+2] for i in range(0, len(word), 2)]

    if tokens is None:
        return ""

    for letter in tokens:
        if re.search(r'[^aeiou][aeiou]', letter, re.IGNORECASE):
            am_letter = ""
            if re.search(r'W[a]', letter):
                for key, value in translation_table.items():
                    if value == letter.lower():
                        am_letter = key
                        break
            else:
                for key, value in translation_table.items():
                    if value == letter:
                        am_letter = key
                        break

            if am_letter is not None:
                trans_word += am_letter
        else:
            ltrs = list(letter)
            am_letter = ""
            for ltr in ltrs:
                for key, value in translation_table.items():
                    if value == ltr:
                        am_letter += key
                        break

            if am_letter is not None and am_letter != "ኧ":
                trans_word += am_letter

    return trans_word
