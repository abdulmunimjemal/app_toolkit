import transliterate

suffix_list = (
    "ኦችኣችኧውንንኣ|ኦችኣችህኡ|ኦችኣችኧው|ኣችኧውንንኣ|ኦችኣችኧው|ኢዕኧልኧሽ|ኦችኣችን|ኣውኢው|ኣችኧውኣል|ችኣት|ችኣችህኡ|ችኣችኧው|ኣልኧህኡ|ኣውኦች|ኣልኧህ|ኣልኧሽ|ኣልችህኡ|ኣልኣልኧች|ብኣችኧውስ|ብኣችኧው|ኣችኧውን|ኣልኧች|ኣልኧን|ኣልኣችህኡ|ኣችህኡን|ኣችህኡ|ኣችህኡት|ውኦችንንኣ|ውኦችን|ኣችኧው|ውኦችኡን|ውኦችኡ|ውንኣ|ኦችኡን|ውኦች|ኝኣንኧትም|ኝኣንኣ|ኝኣንኧት|ኝኣን|ኝኣውም|ኝኣው|ኣውኣ|ብኧት|ኦች|ኦችኡ|ውኦን|ኝኣ|ኝኣውን|ኝኣው|ኦችን|ኣል|ም|ሽው|ክም|ኧው|ውኣ|ትም|ውኦ|ውም|ውን|ንም|ሽን|ኣች|ኡት|ኢት|ክኡ|ኤ|ህ|ሽ|ኡ|ሽ|ክ|ች|ኡን|ን|ም|ንኣ"
)
prefix_list = "ስልኧምኣይ|ይኧምኣት|ዕንድኧ|ይኧትኧ|ብኧምኣ|ብኧትኧ|ዕኧል|ስልኧ|ምኧስ|ዕይኧ|ይኣል|ስኣት|ስኣን|ስኣይ|ስኣል|ይኣስ|ይኧ|ልኧ|ብኧ|ክኧ|እን|አል|አስ|ትኧ|አት|አን|አይ|ይ|አ|እ"

sfx_arr = []
pfx_arr = []

# Prepare suffix array
sarr = suffix_list.split("|")
for suffix in sarr:
    sfx_arr.append(transliterate.transliterate(suffix, 'am'))

sfx_arr.append("Wa")  # Special case for ሯ

# Prepare prefix array
parr = prefix_list.split("|")
for prefix in parr:
    pfx_arr.append(transliterate.transliterate(prefix, 'am'))


def stem(word):
    cv_string = transliterate.transliterate(word, 'am')

    # Remove suffixes
    for sfx in sfx_arr:
        if cv_string.endswith(sfx):
            cv_string = cv_string[:-len(sfx)]
            break

    # Remove prefixes
    for pfx in pfx_arr:
        if cv_string.startswith(pfx):
            cv_string = cv_string[len(pfx):]
            break

    # Remove infixes
    while True:
        if len(cv_string) >= 3 and not cv_string[0].isnumeric() and cv_string[1] in "aeiou" and cv_string[2] == cv_string[0]:
            cv_string = cv_string[0] + cv_string[2:]
        else:
            break

    return transliterate.transliterate(cv_string, 'en')


# Example usage
stemmed_word = stem("ልጆቻቸውን")
print(stemmed_word)  # Output: "ልጅ"
