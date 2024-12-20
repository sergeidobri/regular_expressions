import re

def clean_phone_number(phone):
    pattern = r'\D'
    phone = re.sub(pattern, '', phone)

    sub_num = None
    if len(phone) > 11:
        phone, sub_num = phone[:11], phone[11:]

    phone = f"+7({phone[1:4]}){phone[4:7]}-{phone[7:9]}-{phone[9:]}"

    return(phone, sub_num)

def smart_insert(data, info):
    fields = data[0]

    for i, row in enumerate(data):
        l_name, f_name, *other = row
        if l_name == info[0] and f_name == info[1] and i != 0:
            for j, _ in enumerate(fields):
                if info[j] and not data[i][j]:
                    data[i][j] = info[j]
            return data

    data.append(info)
    return data
