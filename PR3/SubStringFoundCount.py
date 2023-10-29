def count_substring(string_value: str, substring_value: str, ) -> int:
    count = 0
    string_value = string_value.replace("!", "#")
    string_value = string_value.replace(substring_value, "!")
    for symbol in string_value:
        if symbol == "!":
            count += 1
    return count


print(count_substring("Если нужно найти все вхождения подстроки", "и"))
