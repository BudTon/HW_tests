import pytest
import requests
from task_2 import create_folder_YA

@pytest.mark.parametrize(
    'folder_name',
    (
            'New_folder1',
            'New_folder2',
            'New_folder3',
            'New_folder4',
            'New_folder5',
     )
)
def test_create_folder_YA(folder_name):
    token_YA = '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'OAuth {token_YA}'
    }
    url_test_folder = 'https://cloud-api.yandex.net/v1/disk/resources?path=%2F%D0%97%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8'
    response = requests.get(url_test_folder, headers=headers)
    list_name_folder_old = [response.json()['_embedded']['items'][row]['name']
                            for row in range(len(response.json()['_embedded']['items']))
                            if response.json()['_embedded']['items'][row]['type'] == 'dir']
    assert folder_name not in list_name_folder_old
    result = create_folder_YA(token_YA, folder_name)
    url_test_folder = 'https://cloud-api.yandex.net/v1/disk/resources?path=%2F%D0%97%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8'
    response = requests.get(url_test_folder, headers=headers)
    list_name_folder_new = [response.json()['_embedded']['items'][row]['name']
                            for row in range(len(response.json()['_embedded']['items']))
                            if response.json()['_embedded']['items'][row]['type'] == 'dir']
    assert folder_name in list_name_folder_new
    url_delet = 'https://cloud-api.yandex.net/v1/disk/resources'
    response_delet = requests.delete(url_delet, params={'path': f'Загрузки/{folder_name}'}, headers=headers)
    print(response_delet.status_code)
    expected_response_status_code = 200
    expected_create_a_folder_status_code = 201
    assert response_delet.status_code == 204
    assert result[0] == expected_response_status_code
    assert result[1] == expected_create_a_folder_status_code
