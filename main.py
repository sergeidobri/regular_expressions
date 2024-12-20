from utils import clean_phone_number, smart_insert
from files import get_raw_phonebook, save_clean_phonebook

def main():
    path_to_raw_file = 'data/phonebook_raw.csv'      # путь до начального файла
    path_to_clean_file = 'data/phonebook_clean.csv'  # путь до чистого файла
    data_in = get_raw_phonebook(path_to_raw_file)
    if not data_in:
        print("Ошибка чтения файла")
        return 0

    clean_data = [data_in[0]]  # заголовки

    for row in data_in[1:]:
        # задание 1
        fio = " ".join(row[:3]).split()
        # предполагается, что имя и фамилия есть всегда
        clean_row = fio + [""]*(len(fio)==2) + row[3:]

        # задание 2
        raw_phone = clean_row[-2]
        if raw_phone:
            clean_phone, sub_phone = clean_phone_number(raw_phone)
            if sub_phone is not None:
                clean_phone += f" доб.{sub_phone}"
            clean_row[-2] = clean_phone

        # задание 3
        clean_data = smart_insert(clean_data, clean_row)

    save_clean_phonebook(path_to_clean_file, clean_data)

if __name__ == "__main__":
    main()
    