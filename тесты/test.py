import time
import asyncio
import sys

COEFF = 0.01


async def prosess(person):
    print(f"Buying gifts at {str(int(person.split()[0]) + 1)} stop")
    await asyncio.sleep(COEFF * int(person.split()[1]))
    print(f"Arrive from {str(int(person.split()[0]) + 1)} stop")
    time.sleep(COEFF * int(person.split()[2]))


async def prosess1(person):
    print(f"Buy {person.split()[1]}")
    time.sleep(COEFF * int(person.split()[2]))
    await asyncio.sleep(COEFF * int(person.split()[3]))
    print(f"Got {person.split()[1]}")


async def interviews_2(o, tasks12):
    taskss = []
    taskss.append(asyncio.create_task(prosess(o)))
    for j1 in tasks12:
        taskss.append(asyncio.create_task(prosess1(j1)))
    await asyncio.gather(*taskss)


async def interviews_1(tasks12):
    taskss = []
    for j1 in tasks12:
        taskss.append(asyncio.create_task(prosess1(j1)))
    await asyncio.gather(*taskss)


if __name__ == '__main__':
    data = list(map(str.strip, sys.stdin))
    tasks = []
    stops = []
    flag = 0
    for i in range(len(data) - 1):
        if flag == 1:
            tasks.append(str(int(data[i].split()[1]) + int(data[i].split()[2])) + ' ' + data[i])
        if data[i] == '':
            flag = 1
        if flag == 0:
            stops.append(str(i) + ' ' + data[i])
    tasks = sorted(tasks)
    for i in stops:
        tasks1 = []
        k = 0
        k1 = int(i.split()[1])
        for j in range(len(tasks)):
            if k + int(tasks[len(tasks) - j - 1].split()[0]) <= k1:
                k += int(tasks[len(tasks) - j - 1].split()[0])
                tasks1.append(tasks[len(tasks) - j - 1])
        asyncio.run(interviews_2(i, tasks1))
        tasks2 = []
        for i1 in tasks:
            if i1 not in tasks1:
                tasks2.append(i1)
        tasks = tasks2
        tasks = sorted(tasks)
    if len(tasks) != 0:
        print("Buying gifts after arrival")
        tasks1 = []
        k = 0
        for j in range(len(tasks)):
            tasks1.append(tasks[len(tasks) - j - 1])
        asyncio.run(interviews_1(tasks1))

