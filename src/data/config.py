# from dataclasses import dataclass


# @dataclass
# class Config:
#     # token: str = '5955357746:AAHhMFog06M2JQdqO2jjdW2vjAc3syNukzU'
#     admin_ids: int = '495703844'
#     pay_token: str = '401643678:TEST:28cead34-8ea1-460a-a53a-2806eeefc7ad'
#     token_p2p: str = '4100118033451987.B7ED73A55871ADD1A9FF2F63AC9743D684FA150050CC750EE0E0812000F6BD6C614CFC267EBAF8F60484D6675C6F1C3A289E293BAA305E95FD371B03C838C7F129D6EBDF2133B66A0E81B53AAC60E51382AAA77AFDB1948541535FB750FBB4EF9F352FFD150DAA856D999AAB387459127D7EC8BDFB62518176ED4A3E3D89C67E'

import configparser

read_config = configparser.ConfigParser()
read_config.read("settings.ini")

BOT_TOKEN = read_config['settings']['token'].strip().replace(" ", "")
PATH_DATABASE = "src/data/database.db"
PATH_LOGS = "src/data/logs.log"
pay_token = '401643678:TEST:28cead34-8ea1-460a-a53a-2806eeefc7ad'
token_p2p: str = '4100118033451987.B7ED73A55871ADD1A9FF2F63AC9743D684FA150050CC750EE0E0812000F6BD6C614CFC267EBAF8F60484D6675C6F1C3A289E293BAA305E95FD371B03C838C7F129D6EBDF2133B66A0E81B53AAC60E51382AAA77AFDB1948541535FB750FBB4EF9F352FFD150DAA856D999AAB387459127D7EC8BDFB62518176ED4A3E3D89C67E'


def get_admins():
    read_admins = configparser.ConfigParser()
    read_admins.read("settings.ini")

    admins = read_admins['settings']['admin_id'].strip().replace(" ", "")

    if "," in admins:
        admins = admins.split(",")
    else:
        if len(admins) >= 1:
            admins = [admins]
        else:
            admins = []

    while "" in admins: admins.remove("")
    while " " in admins: admins.remove(" ")
    while "\r" in admins: admins.remove("\r")
    while "\n" in admins: admins.remove("\n")

    admins = list(map(int, admins))

    return admins