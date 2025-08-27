import json

def auth_user(username, password):
    # absolute path
    absolute_path = "F:\\TH5\\QLDA_IT01\\MuonTraSach\\MuonTraSach\\data\\users.json"
    with open(absolute_path, encoding='utf-8') as f:
        users = json.load(f)

        for u in users:
            if u['username']==username and u['password']==password:
                return True

    return False


if __name__=="__main__":
    print(auth_user("user", 345))