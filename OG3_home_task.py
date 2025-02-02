
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name
		
	def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'  # Специфический уровень доступа для администраторов
        self._users = []  # Список пользователей, управляемых администратором

    def add_user(self, user):
        if isinstance(user, User):
            self._users.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Ошибка: только объекты User могут быть добавлены.")
