"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open ('/Users/peter/projects/learn-homework-2/referat.txt', 'r', encoding='utf-8') as file_input:
        content = file_input.read()
        print(f'Длина получившейся строки: {len(content)}')
        list_of_words = content.split()
        content_with_exclamations = content.replace('.','!')
        print(f'Количество слов в тексте: {len(list_of_words)}')

        with open('/Users/peter/projects/learn-homework-2/referat2.txt', 'w', encoding='utf-8') as file_output:
            file_output.write(content_with_exclamations)
        

if __name__ == "__main__":
    main()
