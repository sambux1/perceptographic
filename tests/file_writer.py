class write_in:
    def __init__(self,text_content):
        self.text_content=text_content+"\n"
        self.path="output/test.txt"

    def write_into_file(self):
        with open(self.path, "a") as file:
            file.write(self.text_content)
        print("写入成功！")




