LAN = {#DICXTIONARY OF PCS
    "PC1": ["PC2", "PC4"],
    "PC2": ["PC1", "PC3", "PC5"],
    "PC3": ["PC2", "PC5"],
    "PC4": ["PC1", "PC5"],
    "PC5": ["PC2", "PC3", "PC4"]
}

print(LAN["PC1"])


def pc2(list_1, dict1):
    li = []
    for key1 in list_1:
        for i in dict1[key1]:
            li.append(i)
    li2 = []
    for i in li:
        if i not in li2:
            li2.append(i)
    return li2


print(pc2(LAN["PC2"], LAN))