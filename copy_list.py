def copy_list(a):
    local_list = []
    for i in a:
        local_list.append(i)
    return local_list

print(copy_list(["hej", "vad", "gör"]))