import requests
import json
import os
import time

user_info_url = "https://tgapi.duckchain.io/user/info"
quack_execute_url = "https://tgapi.duckchain.io/quack/execute"

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def read_query_ids_from_file(filename):
    with open(filename, 'r') as file:
        query_ids = [line.strip() for line in file.readlines()]
    return query_ids

def get_user_info(query_id):
    headers = {
        "authority": "tgapi.duckchain.io",
        "method": "GET",
        "path": "/user/info",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "authorization": f"tma {query_id}",
        "if-none-match": 'W/"2c9-YE4kAhXbFsP8p9hIYbaPn2nqfww"',
        "origin": "https://tgdapp.duckchain.io",
        "priority": "u=1, i",
        "referer": "https://tgdapp.duckchain.io/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(user_info_url, headers=headers)
        response.raise_for_status()
        data = response.json() 
        if data.get('code') == 200:
            user_data = data.get('data', {})
            duck_name = user_data.get('duckName', 'N/A')
            quack_times = user_data.get('quackTimes', 'N/A')
            box_amount = user_data.get('boxAmount', 'N/A')
            decibels = user_data.get('decibels', 'N/A')
            print(f"[*] Tài khoản: {duck_name}.")
            print(f"[*] Số điểm hiện tại: {quack_times}.")
            print(f"[*] Số rương hiện tại: {box_amount}.")
            print(f"[*] Số năng lượng hiện tại: {decibels}.")
        else:
            print(f"[*] Hiện tại không thể truy xuất dữ liệu từ tài khoản.")
    except requests.exceptions.RequestException as e:
        print(f"[*] Đã xảy ra lỗi khi truy xuất dữ liệu từ tài khoản!")

def execute_quack(query_id):
    headers = {
        "authority": "tgapi.duckchain.io",
        "method": "GET",
        "path": "/quack/execute?",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "authorization": f"tma {query_id}",
        "if-none-match": 'W/"96-uq81erNaAraWBW4GxTgnE6YlXg8"',
        "origin": "https://tgdapp.duckchain.io",
        "priority": "u=1, i",
        "referer": "https://tgdapp.duckchain.io/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    try:
        for _ in range(100):
            response = requests.get(quack_execute_url, headers=headers)
            response.raise_for_status()
        data = response.json() 
        if data.get('code') == 200:
            print(f"[*] Đã thu hoạch số điểm cho tài khoản thành công.")
        else:
            print(f"[*] Hiện tại không thể thu hoạch số điểm cho tài khoản.")
    except requests.exceptions.RequestException as e:
        print(f"[*] Đã xảy ra lỗi khi thu hoạch số điểm cho tài khoản!")

def main():
    while True:
        clear_console()
        query_ids = read_query_ids_from_file('data.txt')
        for query_id in query_ids:
            get_user_info(query_id)
            execute_quack(query_id)
        print(f"[*] Đã hoàn thành xong tất cả tài khoản! Vui lòng đợi một xíu để tiếp tục vòng lặp.")
        time.sleep(600)
  
if __name__ == "__main__":
    main()
