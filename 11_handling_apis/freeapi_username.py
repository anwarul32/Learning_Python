import requests

def fectch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data :
        user_data = data["data"]
        user_name = user_data['login']['username']
        user_country = user_data['location']["country"]
        user_street = user_data['location']['street']['name']
        # print(f'{user_name}, Country = {user_country} Street : {user_street}')
        return user_name, user_country, user_street
    else :
        # print('Failed to fetch user data')
        raise Exception("Failed to fetch user data")
        

def main():
    try:
        user_name, user_country, user_street = fectch_random_user_freeapi()
        print(f'User-name: {user_name} \nCountry: {user_country} \nStreet: {user_street}')
    except Exception as ex:
        print(str(ex))
    

if __name__ == "__main__":
    main()