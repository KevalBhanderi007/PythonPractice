import re 

line = "email  : info@domain.co.uk number : 5641384168464 name : mera bharat mahan phone number : 456-478-8596"
find_word = r'bharat'

find_num = r'\d+'

find_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

find_phone_num = r'\d{3}-\d{3}-\d{4}'


explore = re.findall(find_phone_num,line)

print(explore)



