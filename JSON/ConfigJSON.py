

# Индексы для использования.

I_LAST_MAIL = 0 # список последних почт (учитывая, что их может быть несколько)
I_STANDART_MAIL = 1  # список почт, на которые будет рассылаться по умолчанию.
I_DEFAULT_SETTINGS = 2 # изменял ли человек что-то в настройках. Необходимо для пропуска некоторых этапов.
I_INS_CHAT = 3  # отправлять сразу в чат.
I_INS_MAIL = 4  # отправлять сразу на почту, указанную в standart_mail.
I_TO_FILE = 5  # отправлять ли протокол файлом.
I_TO_tar = 6  # отправлять ли протокол раром.
I_TO_ZIP = 7  # отправлять ли протокол зипом.
I_STATE = 8
I_INPUT = 9

IndexToJSON = {
    I_LAST_MAIL: "last_mail",
    I_STANDART_MAIL: "standart_mail",
    I_DEFAULT_SETTINGS : "default_settings",
    I_INS_CHAT : "ins_chat",
    I_INS_MAIL : "ins_mail",
    I_TO_FILE : "to_file",
    I_TO_tar : "to_tar",
    I_TO_ZIP : "to_zip",
}


input_fields = ["values", "protocol", "send", "ion", "input_indexed","indexed", "type_file", "list", "chosen_column"]


PATH_DEFAULT_USER = "JSON/DefaultUser.json"
PATH_USERS = "JSON/Users.json"