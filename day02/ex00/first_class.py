class Must_read:
    def file_reader(self):
        with open('data.csv', 'r') as file:
            content = file.read()
            print(content)

if __name__ == '__main__':
    must_read_instance = Must_read() #создаем экземпляр класса
    must_read_instance.file_reader() #вызывается метод файл_ридер для экземпляра