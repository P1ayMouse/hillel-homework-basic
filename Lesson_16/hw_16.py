if __name__ == "__main__":
    file_writer = open("text_file.txt", "w")
    while True:
        txt = str(input())
        if txt == "":
            break
        file_writer.write(txt + "\n")
    file_writer.close()
