# criptrografia de senhas

"""
a senha base informada no input (key), será criptografada seguindo a
seguinte regra de criptografia. Depois de passar pelo precesso que
irá mascarar a key, ela será atribuida para a variavel password, e
poderá sera descriptografa sempre que o receptor conhecer o padrão

- é importante resaltar quando implementada será necessario bloqueios
de segurança, pois é possivel que utilizando reverse engineering um
invarsor consiga quebra a criptografia, ou até mesmo, processos de
entrada forçada
"""

key = str(input('Digite a base da sua senha: '))

password = ''

for x in key:
    if x in 'Aa':
        password += '3'
    elif x in 'Bb':
        password += '@'
    elif x in 'Cc':
        password += '1'
    elif x in 'Dd':
        password += '#'
    elif x in 'Ee':
        password += '8'
    elif x in 'Ff':
        password += '*'
    elif x in 'Gg':
        password += '6'
    elif x in 'Hh':
        password += '%'
    elif x in 'Ii':
        password += '2'
    elif x in 'Jj':
        password += '&'
    elif x in 'Kk':
        password += '9'
    elif x in 'Ll':
        password += '$'
    elif x in 'Mm':
        password += '4'
    elif x in 'Nn':
        password += '?'
    elif x in 'Oo':
        password += '!'
    elif x in 'Pp':
        password += '^'
    elif x in 'Qq':
        password += '0'
    elif x in 'Rr':
        password += '<'
    elif x in 'Ss':
        password += '/'
    elif x in 'Tt':
        password += '+'
    elif x in 'Uu':
        password += '5'
    elif x in 'Vv':
        password += '='
    elif x in 'Ww':
        password += '7'
    elif x in 'Xx':
        password += '{'
    elif x in 'Yy':
        password += '['
    elif x in 'Zz':
        password += '('
print(password)
