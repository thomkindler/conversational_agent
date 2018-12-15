#Initialize List and dictionary

dic_a={1:"test 1", 2:"test_2"}
print(dic_a)
print(dic_a[1])
print(dic_a[2])

# die LEement der Listen können ganz verschiedene Dinge sein wie zum Beispiel Dictionaries oder Listen von Listen
list_a=[1,[2,dic_a,["sch",3]],3]
print(list_a)

list_b=list_a[1:]
print(list_b)

#beginnt beim letzten Index for dem ende bis zum ende der Liste
list_c=list_a[-1:]
print(list_c)

#nur das nullte Elemnt der Liste wird genommen: 0<= n < 1
list_d=list_a[0:1]
print(list_d)

#Listen können addiert werden
list_e= list_d + list_c
print(list_e)

#mit append können eElemende an eine Liste angehängt werden
list_e.append(list_d)
print(list_e)

#arbeiten mit Listen
#pop löscht das letzte Eleemnt und übergibt es als Resultat
list_f=list_e.pop()
print(list_f)
print(list_e)

#sortieren von Listen
list_e=[1,3,2,5,0]
list_e.sort()
print(list_e)

#umgekehrt sortiert
list_e.sort(reverse=True)
print(list_e)

#element löschen
del list_e[1]
print(list_e)

#Laenge einer liste
print(len(list_e))

#Ist ELement in Liste entahlten
print( 5 in list_e )

#Loop über alle Element einer Liste
for x in list_e:
    print(x)

#Loop über alle Element einer List
for x in range(len(list_e)):
    print(list_e[x])

#minimum und maximum einer Liste
print(max(list_e))
print(min(list_e))

#liste umkehren
print(list_e)
list_e.reverse()
print(list_e)
list_e=list_e[::-1]
print(list_e)

#tuple in Liste umwandeln
tuple_a=(0,1,2,3)
list_f=list(tuple_a)
print(list_f)
