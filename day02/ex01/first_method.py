class Research:
    def file_reader(self):
        with open('../ex00/data.csv', 'r') as file:
            content = file.read()
        return content

if __name__ == '__main__':
    research = Research()
    content = research.file_reader()
    print(content)