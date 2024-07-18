import time


class User:
    def __init__(self, *args):
        self.nickname = args[0]
        self.password = hash(args[1])
        self.age = args[2]

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname == other.nickname
        else:
            return False


class Video:
    def __init__(self, *args, adult_mode=False, time_now=0):
        self.title = args[0]
        self.duration = args[1]
        self.adult_mode = adult_mode
        self.time_now = time_now

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title
        else:
            return False

class UrTube:
    users = []
    videos = []
    current_user: User = None

    def register(self, *args):
        u = User(args[0], args[1], args[2])

        if u in self.users:
            print(f'Пользователь {u.nickname} уже существует')
        else:
            self.users.append(u)
            self.current_user = u

    def add(self, *args):
        for v in args:
            if isinstance(v, Video) and v not in self.videos:
                self.videos.append(v)

    def get_videos(self, word):
        found = []
        for i in self.videos:
            if word.lower() in i.title.lower():
                found.append(i)
        return found

    def log_out(self):
        self.current_user = None

    def log_in(self, *args):
        n = args[0]
        p = args[1]
        for i in self.users:
            if i.nickname == n and i.password == hash(p):
                self.current_user = i

    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for v in self.videos:
            if title == v.title:
                if v.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                else:
                    for i in range(0, v.duration):
                        print(i + 1, end=" ")
                        time.sleep(1)
                    print('Конец видео')
                    return


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
