import time

seeds = []

seedsToSoil = []

soilToFert = []

fertToWater = []

waterToLight = []

lightToTemp = []

tempToHumid = []

humidToLoc = []

shortestLocation = 100000000000

contents = ""

input = open('../input.txt') 
        
while(True):
    line = input.readline()
    words = line.split()
    if(len(words) >= 1):
        if(words[0] == 'seeds:'):
            seeds = words[1:]
        if(words[0] == 'seed-to-soil'):
            sts = input.readline().strip()
            while(sts != ""):
                 seedsToSoil.append(sts)
                 sts = input.readline().strip()
        if(words[0] == 'soil-to-fertilizer'):
            sts = input.readline().strip()
            while(sts != ""):
                 soilToFert.append(sts)
                 sts = input.readline().strip()
        if(words[0] == 'fertilizer-to-water'):
            sts = input.readline().strip()
            while(sts != ""):
                 fertToWater.append(sts)
                 sts = input.readline().strip()
        if(words[0] == 'water-to-light'):
            sts = input.readline().strip()
            while(sts != ""):
                 waterToLight.append(sts)
                 sts = input.readline().strip()
        if(words[0] == 'light-to-temperature'):
            sts = input.readline().strip()
            while(sts != ""):
                 lightToTemp.append(sts)
                 sts = input.readline().strip()
        if(words[0] == 'temperature-to-humidity'):
            sts = input.readline().strip()
            while(sts != ""):
                 tempToHumid.append(sts)
                 sts = input.readline().strip()
        if(words[0] == 'humidity-to-location'):
            sts = input.readline().strip()
            while(sts != ""):
                 humidToLoc.append(sts)
                 sts = input.readline().strip()
            break
input.close()



def part1():
    currentNum = 0
    for seed in seeds:
        currentNum = int(seed)
        print(str(currentNum) + "SEED")
        for s in seedsToSoil:
            nums = s.split()
            if(currentNum >= int(nums[1]) and currentNum < int(nums[1])+ (int(nums[2]))):
                currentNum = currentNum + (int(nums[0]) - int(nums[1]))
                break
            print(str(currentNum) + "SOIL")
        for s in soilToFert:
            nums = s.split()
            if(currentNum >= int(nums[1]) and currentNum < int(nums[1])+ (int(nums[2]))):
                currentNum = currentNum + (int(nums[0]) - int(nums[1]))
                break
            print(str(currentNum) + "FERT")
        for s in fertToWater:
            nums = s.split()
            if(currentNum >= int(nums[1]) and currentNum < int(nums[1])+ (int(nums[2]))):
                currentNum = currentNum + (int(nums[0]) - int(nums[1]))
                break
            print(str(currentNum) + "WATER")
        for s in waterToLight:
            nums = s.split()
            if(currentNum >= int(nums[1]) and currentNum < int(nums[1])+ (int(nums[2]))):
                currentNum = currentNum + (int(nums[0]) - int(nums[1]))
                break
            print(str(currentNum) + "LIGHT")
        for s in lightToTemp:
            nums = s.split()
            if(currentNum >= int(nums[1]) and currentNum < int(nums[1])+ (int(nums[2]))):
                currentNum = currentNum + (int(nums[0]) - int(nums[1]))
                break
            print(str(currentNum) + "TEMP")
        for s in tempToHumid:
            nums = s.split()
            if(currentNum >= int(nums[1]) and currentNum < int(nums[1])+ (int(nums[2]))):
                currentNum = currentNum + (int(nums[0]) - int(nums[1]))
                break
            print(str(currentNum) + "HUMID")
        for s in humidToLoc:
            nums = s.split()
            if(currentNum >= int(nums[1]) and currentNum < int(nums[1])+ (int(nums[2]))):
                currentNum = currentNum + (int(nums[0]) - int(nums[1]))
                break
            print(str(currentNum) + "Location")
        if(currentNum < shortestLocation): 
            shortestLocation = currentNum


       
    print(shortestLocation)

"""
#173,706,076




"""

def part2():
    print("Running Part 2")
    smallestLocation = 0
    currentNum = 0
    s_time = time.time()
    
    while(True):
        currentNum = smallestLocation
        for s in humidToLoc:
                nums = s.split()
                if(currentNum >= int(nums[0]) and currentNum < int(nums[0])+ (int(nums[2]))):
                    currentNum = currentNum + (int(nums[1]) - int(nums[0]))
                    break

        for s in tempToHumid:
                nums = s.split()
                if(currentNum >= int(nums[0]) and currentNum < int(nums[0])+ (int(nums[2]))):
                    currentNum = currentNum + (int(nums[1]) - int(nums[0]))
                    break

        for s in lightToTemp:
                nums = s.split()
                if(currentNum >= int(nums[0]) and currentNum < int(nums[0])+ (int(nums[2]))):
                    currentNum = currentNum + (int(nums[1]) - int(nums[0]))
                    break

        for s in waterToLight:
                nums = s.split()
                if(currentNum >= int(nums[0]) and currentNum < int(nums[0])+ (int(nums[2]))):
                    currentNum = currentNum + (int(nums[1]) - int(nums[0]))
                    break

        for s in fertToWater:
                nums = s.split()
                if(currentNum >= int(nums[0]) and currentNum < int(nums[0])+ (int(nums[2]))):
                    currentNum = currentNum + (int(nums[1]) - int(nums[0]))
                    break

        for s in soilToFert:
                nums = s.split()
                if(currentNum >= int(nums[0]) and currentNum < int(nums[0])+ (int(nums[2]))):
                    currentNum = currentNum + (int(nums[1]) - int(nums[0]))
                    break

        for s in seedsToSoil:
                nums = s.split()
                if(currentNum >= int(nums[0]) and currentNum < int(nums[0])+ (int(nums[2]))):
                    currentNum = currentNum + (int(nums[1]) - int(nums[0]))
                    break

        if(isInRange(currentNum)):
            print(str(smallestLocation) + " SMALLEST LOCATION FOUND")
            break
        else:
            smallestLocation+=1
            if(smallestLocation % 100000 == 0):
                e_time = time.time()
                print('SmallestLocationTried: '+str(smallestLocation) + ' Time: ', e_time - s_time)

def isInRange(num):
    if(num > int(seeds[0]) and num < int(seeds[0]) + int(seeds[1])):
        return True
    elif(num > int(seeds[2]) and num < int(seeds[2]) + int(seeds[3])):
        return True
    elif(num > int(seeds[4]) and num < int(seeds[4]) + int(seeds[5])):
        return True
    elif(num > int(seeds[6]) and num < int(seeds[6]) + int(seeds[7])):
        return True
    elif(num > int(seeds[8]) and num < int(seeds[8]) + int(seeds[9])):
        return True
    elif(num > int(seeds[10]) and num < int(seeds[10]) + int(seeds[11])):
        return True
    elif(num > int(seeds[12]) and num < int(seeds[12]) + int(seeds[13])):
        return True
    elif(num > int(seeds[14]) and num < int(seeds[14]) + int(seeds[15])):
        return True
    elif(num > int(seeds[16]) and num < int(seeds[16]) + int(seeds[17])):
        return True
    elif(num > int(seeds[18]) and num < int(seeds[18]) + int(seeds[19])):
        return True
    else:
        return False


part2()



"""
79 - 14   79 through 92

seed-to-soil map:
52 50 48   50 through 97 +2

81 - 14    81 through 94

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

81 - 14

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

81 - 14  81 through 94

water-to-light map:
88 18 7
18 25 70  25 through 94  -7

74 - 14  74 through 87


light-to-temperature map:
45 77 23   77 through 99 -32  so 77-32=45
81 45 19
68 64 13  64 through 76  +4

74 - 3
45 - 11


temperature-to-humidity map:
0 69 1
1 0 69  0 through 68 +1

74 - 3
46 - 11


humidity-to-location map:
60 56 37  56 through 92 +4
56 93 4   93 through 96 -37

78 - 3
46 - 10
67 - 1






"""


    

