#Cs 162 - python queueing project
#Emma Nessly

#list:
input_queue = ["S Mary",
"P Dee",
"P Dee",
"E Eileen",
"E Mike",
"E Joe",
"P Dee",
"E Vicky",
"E George",
"P Dee",
"P Joe",
"E Sally",
"P Joe",
"S Pete",
"P Dee",
"S Bill",
"S Chase",
"E Price",
"P Dee",
"E Sue"
]
#Creating the queues: priority, standard, and economy
priority_queue = []
standard_queue = []
economy_queue = []

#Finding the num of packets
packets_input = len(input_queue)
print(packets_input)

#setting up the code to append
for i in range(packets_input):
    packets_in = input_queue[i]
    pclass = packets_in[0]
    if pclass == "P":
        priority_queue.append(input_queue[i])
    elif pclass == "S":
        standard_queue.append(input_queue[i])
    else:
        economy_queue.append(input_queue[i])

print(economy_queue)
print(standard_queue)
print(priority_queue)
#while loop and function
def queue_organization(input_queue, priority_queue, standard_queue, economy_queue):
    while (len(input_queue)) != 0:
        print(input_queue)

#setting up the different queues functions: priority, standard, and economy
def priority_organization(priority_queue,packets_input, queue_organization):
    for i in range(3):
        print(priority_queue[0])
        priority_queue.pop(0)
priority_organization(priority_queue,packets_input, queue_organization)

def standard_organization(standard_queue,packets_input, queue_organization):
    for i in range(2):
        print(standard_queue[0])
        standard_queue.pop(0)
standard_organization(standard_queue,packets_input,queue_organization)

def economy_organization(economy_queue, packets_input,queue_organization):
    for i in range(1):
        print(economy_queue[0])
        economy_queue.pop(0)
economy_organization(economy_queue, packets_input, queue_organization)
