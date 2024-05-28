import re
from translator import to_english, to_amharic

def stem(word):
    cv_string = to_english(word)

    # Prepare suffix array
    suffix_list = "ኦችኣችኧውንንኣ|ኦችኣችህኡ|ኦችኣችኧውን|ኣችኧውንንኣ|ኦችኣችኧው|ኢዕኧልኧሽ|ኦችኣችን|ኣውኢው|ኣችኧውኣል|ችኣት|ችኣችህኡ|ችኣችኧው|ኣልኧህኡ|ኣውኦች|ኣልኧህ|ኣልኧሽ|ኣልችህኡ|ኣልኣልኧች|ብኣችኧውስ|ብኣችኧው|ኣችኧውን|ኣልኧች|ኣልኧን|ኣልኣችህኡ|ኣችህኡን|ኣችህኡ|ኣችህኡት|ውኦችንንኣ|ውኦችን|ኣችኧው|ውኦችኡን|ውኦችኡ|ውንኣ|ኦችኡን|ውኦች|ኝኣንኧትም|ኝኣንኣ|ኝኣንኧት|ኝኣን|ኝኣውም|ኝኣው|ኣውኣ|ብኧትን|ኣችህኡም|ችኣችን|ኦችህ|ኦችሽ|ኦችኡ|ኦችኤ|ኦውኣ|ኦቿ|ችው|ችኡ|ኤችኡ|ንኧው|ንኧት|ኣልኡ|ኣችን|ክኡም|ክኡት|ክኧው|ችን|ችም|ችህ|ችሽ|ችን|ችው|ይኡሽን|ይኡሽ|ውኢ|ኦችንንኣ|ኣውኢ|ብኧት|ኦች|ኦችኡ|ውኦን|ኝኣ|ኝኣውን|ኝኣው|ኦችን|ኣል|ም|ሽው|ክም|ኧው|ውኣ|ትም|ውኦ|ውም|ውን|ንም|ሽን|ኣች|ኡት|ኢት|ክኡ|ኤ|ህ|ሽ|ኡ|ሽ|ክ|ች|ኡን|ን|ም|ንኣ"
    sfx_arr = [to_english(i) for i in suffix_list.split('|')]
    sfx_arr.append("Wa")  # Special case for ሯ

    # Prepare prefix array
    prefix_list = "ስልኧምኣይ|ይኧምኣት|ዕንድኧ|ይኧትኧ|ብኧምኣ|ብኧትኧ|ዕኧል|ስልኧ|ምኧስ|ዕይኧ|ይኣል|ስኣት|ስኣን|ስኣይ|ስኣል|ይኣስ|ይኧ|ልኧ|ብኧ|ክኧ|እን|አል|አስ|ትኧ|አት|አን|አይ|ይ|አ|እ"
    pfx_arr = [to_english(i) for i in prefix_list.split('|')]

    # Remove suffixes
    for sfx in sfx_arr:
        if cv_string.endswith(sfx) and len(cv_string) > len(sfx) + 2:
            cv_string = cv_string[:-len(sfx)]
            break

    # Remove prefixes
    for pfx in pfx_arr:
        if cv_string.startswith(pfx) and len(cv_string) > len(pfx) + 2:
            cv_string = cv_string[len(pfx):]
            break

    # Remove infixes
    if re.search(r".+([^aeiou])[aeiou]\1[aeiou].?", cv_string):
        cv_string = re.sub(r"\S\S[^aeiou][aeiou]",
                           lambda m: m.group()[0:2], cv_string)
    elif re.match(r"^(.+)a\1$", cv_string):
        cv_string = re.sub(r"a.+", "", cv_string)

    if re.search(r"[bcdfghjklmnpqrstvwxyz]{2}e", cv_string):
        ccv = re.search(r"[bcdfghjklmnpqrstvwxyz]{2}e", cv_string).group()
        cv_string = cv_string.replace(ccv, ccv[0] + "X" + ccv[1])

    return to_amharic(cv_string)

