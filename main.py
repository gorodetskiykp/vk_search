import vk

api = vk.API(
    # https://vkhost.github.io/
    access_token="vk1.a.KhqyKjh-123Plqr3Cj-8wPPs3BD4ngAJtDLAKFL0XwPyNvUVH6bqkPbqbRM_vWMYAdzdWy2-huBoeX5tCFGnbD2wOGosnUatqrq-lL8dRPExJNW66GH6unm1vTAarB7mqu1Hy8XHFc9WAfJRLD8t83w1FjukA5apNdqsJr7qE75qMByj9eDEIgUuveDHaDtHH5BU--1UECozNlebwyB1qg",
    v='5.131',
)

users = api.users.search(
    city=859,  # Королёв
    count=1000,
    sex=1,
    age_from=23,
    age_to=25,
    fields=(
        "about,activities,books,connections,contacts,followers_count,"
        "interests,last_seen,site,status"
    ),
    group_id="",
    online=True,
)

print(users["count"])

for user in users["items"]:
    if user["is_closed"]:
        continue
    # if not "t.me" in user["status"]:
    #     continue
    print(
        f'- {user["first_name"]}', 
        user["status"], 
        user["id"],
        user.get("about", ""),
        user.get("activities", ""),
        user.get("books", ""),
        user.get("connections", ""),
        user.get("contacts", ""),
        user.get("followers_count", ""),
        user.get("interests", ""),
        user.get("last_seen", {"time": ""}).get("time"),
        user.get("site", ""),
    ) 
    print()
    # print()
# print(users["items"][0].keys())
