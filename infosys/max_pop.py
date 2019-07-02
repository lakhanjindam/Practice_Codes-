#PF-Prac-39
def max_populated_state(cities_dict,state):
    maxx = 0
    total = 0
    out = []
    for i in range(len(cities_dict)):

        if state == cities_dict[i]["State"]:
            total = cities_dict[i]["Population"]
            if total > maxx:
                maxx = total
                out.append(cities_dict[i])



    return maxx, out              


    
cities_dict = [
 {'Name':'Vancouver','State':'WA','Population':161791},
 {'Name':'Salem','State':'OR','Population':154637},
 {'Name':'Seattle','State':'WA','Population':80885},
 {'Name':'Bellingham','State':'WA','Population':608660},
 {'Name':'Spokane','State':'WA','Population':208916},
 {'Name':'Bellevue','State':'WA','Population':608660},
 {'Name':'Portland','State':'OR','Population':583776}
 ]
state="WA"
print("The city details are:",cities_dict)
print("State:",state)
output=max_populated_state(cities_dict,state)
print(output)


'''
def cmp(a, b):
    return (a > b) - (a < b)
a="sasa"
b = "xsas"
if cmp(a, b)==-1:
    print(a)
else:
    print(b)'''