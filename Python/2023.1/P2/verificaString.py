texto = input()
string = input()
# anabanana
# ana texto[0] == string[0] texto[1] == string[1] texto[2] == string[2]
#  ana texto[1] == string[0] texto[2] == string[1] texto[3] == string[2]
#   ana texto[2] == string[0] texto[3] == string[1] texto[4] == string[2]
msg = 'não'
i = 0
tam = len(texto)
while i < tam-2:
    if texto[i] == string[0] and texto[i+1] == string[1] and texto[i+2] == string[2]:
        msg = 'sim'
        i = tam
    i += 1
print(msg)