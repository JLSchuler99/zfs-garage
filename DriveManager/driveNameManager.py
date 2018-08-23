#/bin/python
import sys, os, json

script = os.path.realpath(__file__)
script = script[:len(script)-script[::-1].index("/")-1]



def addDrive(args):
    if len(args) != 2:
        print("Usage: driveNameManager add [drive name] [drive id]")
        exit(1)

    dName = args[0]
    dID = args[1]

    if dName in drives:
        print("You have already created a drive by this name")
        exit(1)

    ###TODO: Check for ID collision

    drives[dName] = dID


def removeDrive(args):
    if len(args) != 1:
        print("Usage: driveNameManager remove [drive name]")

    del drives[args[0]]

def get(args):
    print(drives[args[0]])

def dump(args):
    for x in drives:
        print(x + " " + drives[x])



if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage: driveNameManager [command] [options]")
    with open(script+"/drives.json", 'r') as t:
        drives = json.loads(t.read())
    if args[0] == "add":
        addDrive(args[1:])
    elif args[0] == "remove":
        removeDrive(args[1:])
    elif args[0] == "get":
        get(args[1:])
    elif args[0] == "dump":
        dump(args[1:])
    with open(script+"/drives.json", 'w') as t:
        t.write(json.dumps(drives))
