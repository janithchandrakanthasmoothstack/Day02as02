
#three is a croud


peopleList = []

def addMember(name):
    peopleList.add(name)

def removeMember(name):
    peopleList.remove(name)

def crowdTest():
    if len(peopleList) >3:
        print(f'Room Full: {len(peopleList)}')

def main():
    peopleList.append("Nimal");
    peopleList.append("Kamal");
    peopleList.append("Saman");
    peopleList.append("Ruwan");
    crowdTest();
    peopleList.remove("Saman");
    peopleList.remove("Ruwan");
    crowdTest();

main()
