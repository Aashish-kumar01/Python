import requests

def fetch_random_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/100"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        jokes = data["data"]
        content = jokes["categories"]["content"]
        id = jokes["categories"]["id"]
        message = jokes["message"]
        status = jokes["statusCode"]

        return message, content, id, status
    else:
        raise Exception("Failed to fetch data")
    

def main():
    try:
        message, content, id, status = fetch_random_jokes()
        print(f"Content is {content} \nid is {id} \nmessage is {message} \nStatus is {status}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()







# import requests

# def fetch_random_jokes():
#     url = "https://api.freeapi.app/api/v1/public/randomjokes/100"
#     response = requests.get(url)
#     data = response.json()  # ✅ call json() method

#     if data.get("success") and "data" in data:
#         jokes_list = data["data"]  # ✅ this is a list of jokes
#         if len(jokes_list) > 0:
#             joke = jokes_list[0]  # ✅ take first joke
#             content = joke.get("content", "No content")
#             joke_id = joke.get("id", "No ID")
#             message = data.get("message", "No message")
#             status = data.get("statusCode", "No status")

#             return message, content, joke_id, status
#         else:
#             raise Exception("No jokes found")
#     else:
#         raise Exception("Failed to fetch data")
    

# def main():
#     try:
#         message, content, joke_id, status = fetch_random_jokes()
#         print(f"Content: {content}\nID: {joke_id}\nMessage: {message}\nStatus: {status}")
#     except Exception as e:
#         print(str(e))

# if __name__ == "__main__":
#     main()




# import requests

# def fetch_random_jokes():
#     url = "https://api.freeapi.app/api/v1/public/randomjokes/100"
#     response = requests.get(url)
#     data = response.json()  # ✅ call json method

#     if data.get("success") and "data" in data:
#         jokes_list = data["data"]
#         if len(jokes_list) > 0:
#             joke = jokes_list[0]  # ✅ take first joke
#             content = joke.get("content", "No content")
#             joke_id = joke.get("id", "No ID")
#             message = data.get("message", "No message")
#             status = data.get("statusCode", "No status")
#             return message, content, joke_id, status
#         else:
#             raise Exception("No jokes found")
#     else:
#         raise Exception("Failed to fetch data")

# def main():
#     try:
#         message, content, joke_id, status = fetch_random_jokes()
#         print(f"Content: {content}\nID: {joke_id}\nMessage: {message}\nStatus: {status}")
#     except Exception as e:
#         print("Error:", e)

# if __name__ == "__main__":
#     main()


