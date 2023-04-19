import json

f = open("imdb_top_250.json", 'r')
json_data = json.load(f)
f.close()

attribute = ['year', 'rating', 'genres', 'countries']

organized_dict = {}
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]

for movie in json_data:
    if int(movie[attribute[0]]) < 1990:
        if float(movie[attribute[1]]) < 8.3:
            if "Drama" in movie[attribute[2]]:
                if "United States" in movie[attribute[3]]:   
                    a.append(movie)
                else:
                    b.append(movie)
            else:
                if "United States" in movie[attribute[3]]:
                    c.append(movie)
                else:
                    d.append(movie)
        else:
            if "Drama" in movie[attribute[2]]:
                if "United States" in movie[attribute[3]]:
                    e.append(movie)
                else:
                    f.append(movie)
            else:
                if "United States" in movie[attribute[3]]:
                    g.append(movie)
                else:
                    h.append(movie)
    else:
        if float(movie[attribute[1]]) < 8.3:
            if "Drama" in movie[attribute[2]]:
                if "United States" in movie[attribute[3]]:
                    i.append(movie)
                else:
                    j.append(movie)
            else:
                if "United States" in movie[attribute[3]]:
                    k.append(movie)
                else:
                    l.append(movie)
        else:
            if "Drama" in movie[attribute[2]]:
                if "United States" in movie[attribute[3]]:
                    m.append(movie)
                else:
                    n.append(movie)
            else:
                if "United States" in movie[attribute[3]]:
                    o.append(movie)
                else:
                    p.append(movie)
print(e)

with open("organized_data.json", "w") as outfile:
        json.dump(organized_dict, outfile)

tree = \
    ["Do you prefer movies before 1990?(Y/N)", 
        ["Do you prefer movies with a rating lower than 8.3?(Y/N)", 
            ["Do you prefer drama movies?(Y/N)", 
                ["Do you prefer movies showed in the United States?(Y/N)",
                    [a,None,None],[b,None,None]],
                ["Do you prefer movies showed in the United States?(Y/N)",
                    [c,None,None],[d,None,None]]], 
            ["Do you prefer drama movies?(Y/N)",
                ["Do you prefer movies showed in the United States?(Y/N)",
                    [e,None,None],[f,None,None]],
                ["Do you prefer movies showed in the United States?(Y/N)",
                    [g,None,None],[h,None,None]]]],
        ["Do you prefer movies with a rating lower than 8.3?(Y/N)", 
            ["Do you prefer drama movies?(Y/N)",
                ["Do you prefer movies showed in the United States?(Y/N)",
                    [i,None,None],[j,None,None]],
                ["Do you prefer movies showed in the United States?(Y/N)",
                    [k,None,None],[l,None,None]]], 
            ["Do you prefer drama movies?(Y/N)",
                ["Do you prefer movies showed in the United States?(Y/N)",
                    [m,None,None],[n,None,None]],
                ["Do you prefer movies showed in the United States?(Y/N)",
                    [o,None,None],[p,None,None]]]]]

with open("tree.json", "w") as outfile:
        json.dump(tree, outfile)