# myinfo = {'Username' : 'asifulmamun',
#             'Name' : 'Al Mamun',
#             'Mobile' : '01721600688'
# }

# print(str(myinfo['Username']))

# for keys, values in myinfo.items():
#     print(keys, values)


users = {
    'mamun' : {
        'Name' : 'Al Mamun',
        'Age' : '22',
        'Dist' : 'Kishoreganj'
    },
    'rafi' : {
        'Name' : 'Rafi',
        'Age' : '23',
        'Dist' : 'Sirajganj'
    }
}

# print(users['mamun']['Age'])

for key in users.keys():
    print(key)
    # print(values)
    # for mykeys, myvalues in values.item():
    #     print(mykeys)

#Updated Loop and solution by Kawshik
for keys,values in users.items():
	print(keys.upper()) #upper() for capitalize the key only
		for value, data in values.items():
			print(value, ':', data) #nested loop to access nested dictionary
