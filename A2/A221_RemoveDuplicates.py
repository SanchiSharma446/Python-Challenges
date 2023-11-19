def remove_dupli(user_list):
    done = []
    for i in user_list:
        if i not in done:
            done.append(i)
    return done
