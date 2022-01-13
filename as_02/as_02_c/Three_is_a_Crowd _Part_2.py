
#three is a croud part 2


peopleList = []

def addMember(name):
    peopleList.add(name)

def removeMember(name):
    peopleList.remove(name)

def crowdTest():
    if len(peopleList) >5:
        print(f'mob in the room: {len(peopleList)}')
    elif len(peopleList)>=3 and len(peopleList)<=5:
        print(f"room being crowded: {len(peopleList)}")
    elif len(peopleList)>0 and len(peopleList)<3:
        print(f"room is not very crowded: {len(peopleList)}")
    else:
        print(f"room is Empty : {len(peopleList)}")

def main():
    peopleList.append("Nimal");
    peopleList.append("Kamal");
    peopleList.append("Saman");
    peopleList.append("Ruwan");
    peopleList.append("Kemil");
    peopleList.append("Dann");
    crowdTest();

main()
