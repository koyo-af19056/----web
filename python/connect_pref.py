
copy = "copy.txt"
pref = "pref.txt"
f1 = open(copy,"r")
f2 = open(pref,"r")
f3 = open("connected.txt","w")

begin_string = '<a xlink:href="http://www.pref.'
pref_name = 'fukuoka'
begin_string += '.lg.jp/" target="_blank">'
begin_string += '<g id="fukuoka">'
end_string = '</g></a>\n'

dictionary = {}

for j in f2:
    j = j.split('\t')
    dictionary[j[0]] = j[1].replace('\n',"")
    
for k in f1:
    k = k.split("<")
    pref_name = dictionary[k[0]]
    print(k[0],dictionary[k[0]])
    begin_string =f'<a xlink:href="http://www.pref.{pref_name}.lg.jp/" target="_blank"><g id="{pref_name}">'
    end_string = '</g></a>\n'
    tag = begin_string + "<" +k[1] + end_string
    print(begin_string, k[1], end_string)
    f3.write(tag)


"""
for i in f1:
    new_string = begin_string + i + end_string
    f2.write(new_string)
"""    
    
    
f1.close()
f2.close()
f3.close()