calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(text: str):
    count_calls()
    return [len(text), text.upper(), text.lower()]

def is_contains(text: str, l:list):
    count_calls()
    for i in l:
        if text.lower() == i.lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)