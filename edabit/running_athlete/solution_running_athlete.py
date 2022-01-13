

def running_athlete(instructions, path):
    instructions_path = {
        "run_": "_",
        "run|": "/",
        "jump|": "|",
        "jump_": "x"
    }
    final_path = ""
    for i in range(len(instructions)):
        final_path += instructions_path[instructions[i]+path[i]]
    return final_path
