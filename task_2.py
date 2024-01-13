import requests

def create_folder_YA(token_YA, folder_name):

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'OAuth {token_YA}'
    }

    url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
    response = requests.get(url, headers=headers)
    print(response.status_code)
    create_a_folder_status_code = 0
    if response.status_code == 200:
        print('Доступ к Я.Диску разрешен')
        create_a_folder = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                       params={'path': f'Загрузки/{folder_name}'}, headers=headers)
        if create_a_folder.status_code == 409:
            print(f'Папка - {folder_name} - уже существует на Я.Диску')
            create_a_folder_status_code = create_a_folder.status_code
        if create_a_folder.status_code == 201:
            print(f'Папка - {folder_name} - создана на Я.Диску')
            create_a_folder_status_code = create_a_folder.status_code
    else:
        print('ОШИБКА доступа к Я.Диску')
    return response.status_code, create_a_folder_status_code

if __name__ == '__main__':
    token_YA = '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    folder_name = 'New_folder3'
    create_folder_YA(token_YA, folder_name)
