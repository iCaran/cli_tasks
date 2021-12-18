import sys

def help():
    sa = """Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics"""
    sys.stdout.buffer.write(sa.encode('utf8'))
    
def add(n,s):
    try:
        with open('../tasks/task.txt', 'r') as f:
            st=s+" ["+n+"]\n"
            lines=f.readlines()
            if len(lines)==0:
                with open('../tasks/task.txt', 'w') as g:
                    g.write("".join(st))
                    g.close()
                    s = '"'+s+'"'
                    print(f"Added task: {s} with priority {n}")
            else:
                if st not in lines:
                    pr=[]
                    for line in lines:
                        i=''.join(lines).rindex(line)
                        line=line.strip('\n')
                        beg=line.rfind("[")
                        p=line[beg+1:-1]
                        pr.append(p)
                        
                    for pri in pr:
                        if(n<pri):
                            lines.insert(pr.index(pri),st)
                            break
                        elif pr.index(pri)==len(pr)-1:
                            lines.append(st)
                    
                    with open('../tasks/task.txt', 'w') as f:
                        f.write("".join(lines))
                        f.close()
                        s = '"'+s+'"'
                        print(f"Added task: {s} with priority {n}")
                else:
                    print('''Added task: "'''+s+'''"''')
    except:
        print("Could not add item. Try help.")
    
def ls():
    
    try:
  
        nec()
        l = 1
        k = l
        if len(d)>0:
            for i in d:
                sys.stdout.buffer.write(f"{l}. {d[l]}".encode('utf8'))
                sys.stdout.buffer.write("\n".encode('utf8'))
                l = l+1
        else: sys.stdout.buffer.write("There are no pending tasks!".encode('utf8'))
  
    except Exception as e:
        raise e
        
def done(no):
    try:
  
        nec()
        no = int(no)
        f = open('../tasks/completed.txt', 'a')
        st = d[no]
          
        f.write(st)
        f.write("\n")
        f.close()
        print(f"Marked item as done.")
          
        with open("../tasks/task.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
              
            for i in lines:
                if i.strip('\n') != d[no]:
                    f.write(i)
            f.truncate()
    except:
        print(f"Error: no incomplete item with index #{no} exists.")
        
def report():
    nec()
    try:
        nf = open('../tasks/completed.txt', 'r')
        c = 1
          
        for line in nf:
            line = line.strip('\n')
            don.update({c: line})
            c = c+1
        print("Pending:",len(d))
        for i in d: 
            print(str(i)+". "+d[i])
        print("\nCompleted:",len(don))
        for i in don: 
            b=don[i].rfind("[")
            print(str(i)+". "+don[i][0:b-1])
      
    except:
        print(
            f'Pending : {len(d)} \n\nCompleted : {len(don)}')
            
def deL(no):
    try:
        no = int(no)
        nec()
  
        with open("../tasks/task.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
              
            for i in lines:
                if i.strip('\n') != d[no]:
                    f.write(i)
            f.truncate()
        print(f"Deleted task #{no}")
  
    except Exception as e:
        
        print(f"Error: task with index #{no} does not exist. Nothing deleted.")
        
def nec():
  
    try:
        f = open('../tasks/task.txt', 'r')
        c = 1
        for line in f:
            line = line.strip('\n')
            d.update({c: line})
            c = c+1
    except:
        sys.stdout.buffer.write("There are no pending tasks!".encode('utf8'))
  
  
if __name__ == '__main__':
    try:
        d = {}
        don = {}
        args = sys.argv
        
        if (len(args[1:])==0):
            help()
        if(args[1] == 'del'):
            args[1] = 'deL'
              
        if(args[1] == 'add' and len(args[2:]) == 0 and len(args[3:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing tasks string. Nothing added!".encode('utf8'))
  
        elif(args[1] == 'done' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing NUMBER for marking tasks as done.".encode('utf8'))
  
        elif(args[1] == 'deL' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing NUMBER for deleting tasks.".encode('utf8'))
        else:
            globals()[args[1]](*args[2:])
  
    except Exception as e:
        pass
