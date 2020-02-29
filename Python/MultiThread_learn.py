import threading as tr


#--------------------------------------part1--------------------------------------------#

# threads = []
# result = {}

# testdata = [[1,2,3,4,5,6,7,8],[32,33,34,35,3,6,78,100],[7,4,2,3,6,654,100,43,32,1,4]]

# def top3(arr):
#     arr.sort()
#     result[tr.current_thread().name] =  arr[-3:]

# for i in range(len(testdata)):
#     t = tr.Thread(target=top3,name=str(i),args=(testdata[i],))
#     threads.append(t)
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()

# toparr = []
# for k,v in result.items():
#     toparr.extend(v)

# toparr = list(set(toparr))
# toparr.sort()

# print (toparr[-3:])

#-----------------------------------------part2--------------------------------------------#

lock = tr.Lock()
balance = 0

def changebalance(value):
    global balance
    balance += value

#if there is exception in the function, then the lock will never be released, so we need to use try catch
def runThread(n):
    lock.acquire()
    try:
        changebalance()
    except:
        pass
    finally:
        lock.release()

threads = []
for i in range(11):
    t = tr.Thread(target=changebalance,name=i,args=(i,))
    t.start()
    t.join()
print(balance)

