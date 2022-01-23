

def alphabet_clash(def_str_player_a, att_lst_player_a, def_str_player_z, att_lst_player_z):

    final_result = {"A": 0, "Z": 0}

    def_lst_player_a = [ord(def_str_player_a[i]) for i in range(len(def_str_player_a)) if i not in att_lst_player_z]
    def_lst_player_z = [ord(def_str_player_z[i]) for i in range(len(def_str_player_z)) if i not in att_lst_player_a]

    for i in range(len(def_lst_player_a)):
        diff = def_lst_player_a[i] - def_lst_player_z[i]
        final_result["A" if diff > 0 else "Z"] += abs(diff)

    return final_result
