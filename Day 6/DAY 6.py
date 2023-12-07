input = open('./input.txt')

times = input.readline().split()[1:]
distances = input.readline().split()[1:]

input.close()

timesWonList = []

def part1():
    for time, distance in zip(times, distances):
        time = int(time)
        distance = int(distance)
        x = range(time+1)
        timesBeat = 0
        for i in x:
            if(i*(time-i)>distance):
                timesBeat+=1
        print('Times beaten: %s' % timesBeat)
        timesWonList.append(timesBeat)

    answer = 1
    for wins in timesWonList:
        answer*=wins
    print('The answer is: %s' % answer)

def part2():
    newTime=""
    newDistance=""
    for time in times:
        newTime+=time
    print("New time: %s" % newTime)

    for dis in distances:
        newDistance+=dis
    print("New distance: %s" % newDistance)

    newTime = int(newTime)
    newDistance = int(newDistance)
    x = range(newTime+1)
    timesBeat = 0
    for i in x:
        if(i*(newTime-i)>newDistance):
            timesBeat+=1
    print('Times beaten: %s' % timesBeat)
    timesWonList.append(timesBeat)

part2()
    
