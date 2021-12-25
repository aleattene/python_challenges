

def ping_pong(pings_lst, winner):
    pings_lst = ["Ping!", "Pong!"] * len(pings_lst)
    return pings_lst if winner else pings_lst[:-1]


