file=open("pythonread.txt")
s_file= sorted(file.read().split()[1:324:2])
print('Sorted Variable:', s_file)
