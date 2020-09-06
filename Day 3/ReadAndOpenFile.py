text = "First text\nSecond text\nLast text."
append_text = "\nLast last last text."

#'w' = write
#'r' = read
#'a' = append（追加上去）
my_file = open('File.txt','a')
my_file.write(append_text)
my_file.close()