import requests


def make_api_call(welcome_script, cancel_script, wait_script, phone_number):
    base_url = "https://telebotserver.onrender.com/make_call?"
    query_params = {
        "phone_number": phone_number,
        "welcome_script": welcome_script,
        "cancel_script": cancel_script,
        "wait_script": wait_script
    }
    url = base_url + \
        "&".join([f"{key}={value}" for key, value in query_params.items()])

    response = requests.get(url)
    if response.status_code == 200:
        print("API call successful.")
    else:
        print(f"API call failed with status code: {response.status_code}")


def main():
    print("Please provide the following inputs:")
    welcome_script = input("Welcome Script: ")
    cancel_script = input("Cancel Script: ")
    wait_script = input("Wait Script: ")
    phone_number = input("Phone Number: ")

    make_api_call(welcome_script, cancel_script, wait_script, phone_number)


if __name__ == "__main__":
    main()
