import pandas as pd

df = pd.read_csv('UL-Standards-List.csv')
# drop rows with no description
df = df.dropna(subset=['Description'])
len(df)
# df.head()
# Description to Title Case since there are some descriptions that are all caps
df['Description'] = df['Description'].str.title()

# Removing duplicates in the description separated by ' / '
def remove_duplicates(string):
    words = string.split(' / ')
    result = []
    for word in words:
        if word not in result:
            result.append(word)
    return ' / '.join(result)  # nothing to join if there are no duplicates

df['Description'] = df['Description'].apply(remove_duplicates)


# Look for non-English descriptions
def isEnglish(s):
    return s.isascii()

df['English?'] = df['Description'].apply(isEnglish)


df['Description'] = df['Description'].str.replace(' For ', ' for ')
df['Description'] = df['Description'].str.replace(' Of ', ' of ')

df['Category'] = ''
df['Topic'] = ''

# Remove non-English descriptions
for idx, row in df.iterrows():
    if row['English?'] == False:
        split_description = row['Description'].split(' / ', maxsplit=1)
        if len(split_description) > 1:
            df.at[idx, 'Topic'] = split_description[0]
        else:
            df.at[idx, 'Topic'] = row['Description']
    else:
        df.at[idx, 'Topic'] = row['Description']

import re
def find_words_in_description(string, words):
    start_index = 0
    found_word = ''
    for word in words:
        i = string.find(word, start_index)
        if i != -1:
            if i > 40:
                continue
            else:
                start_index = i + len(word)

            found_word = found_word + ' ' + word
        else:
            start_index = start_index
    return (start_index, found_word)

words = ['Standard', 'Method', 'Test', 'Outline', 'Guide', 'Guidance', 'Criteria', 'Procedure', 'Rule', 'Requirement','Enclosure']


for idx, row in df.iterrows():
    i = find_words_in_description(row['Topic'], words)[0]
    final_word = find_words_in_description(row['Topic'], words)[1]
    print(i, final_word)
    if final_word != '':
        df.at[idx, 'Category'] = final_word
        split_topic_desc = re.split(' for | of ', row['Topic'][i:], maxsplit=1)
        # join the word in description before the split if not in the list of words

        print(split_topic_desc)
        if len(split_topic_desc) > 1:
            lost_words = [word for word in row['Topic'][:i] if word not in words]
            new_string = ''.join(lost_words)
            df.at[idx, 'Category'] = new_string
            df.at[idx, 'Topic'] = split_topic_desc[1]

    else:
        pass


df.to_csv('Results_3.csv', index=False)
