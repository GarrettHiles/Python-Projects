import os
import datetime

path = 'C:\\Users\\Garrett Hiles\\OneDrive\\Documents\\GitHub\\Tech-Academy-Projects\\Python-Projects\\Script_Assignment\\'

files_info = []

for file_name in os.listdir(path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(path, file_name)
        creation_time = os.path.getctime(file_path)
        formatted_creation_time = datetime.datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
        files_info.append({'file_name': file_name, 'creation_time': formatted_creation_time})

for file_info in files_info:
    print(f"{file_info['file_name']} - Created on: {file_info['creation_time']}")

    
