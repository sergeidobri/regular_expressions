import csv

def get_raw_phonebook(path_to_file):    
    data = []
    try:
        with open(path_to_file, "r") as file_in:
            data = list(csv.reader(file_in))
    except:
        pass
    finally:
        return data

def save_clean_phonebook(path_to_new_file, data_to_save):
    with open(path_to_new_file, "w", encoding='utf-8', newline='') as file_out:
        manager_writer = csv.writer(file_out)
        manager_writer.writerows(data_to_save)