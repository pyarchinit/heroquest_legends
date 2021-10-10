import random


points_of_view = {
    'A' : ('1', '4'),
    'B' : ('1', '2'),
    'C' : ('2', '3'),
    'D' : ('3', '4'),
    'E' : ('1', '5', '6'),
    'F' : ('2', '6', '7'),
    'G' : ('3', '7', '8'),
    'H' : ('4', '5', '8'),
    '1' : ('A', 'B', 'E'),
    '2' : ('B', 'C', 'F'),
    '3' : ('C', 'D', 'G'),
    '4' : ('A', 'D', 'H'),
    '5' : ('E', 'H'),
    '6' : ('E', 'F'),
    '7' : ('F', 'G'),
    '8' : ('G', 'H')}

dungeon_to_room = {
    'A1' : ('401', '402', '403'),
    'B1' : ('301', '302', '303'),
    'B2' : ('301', '304'),
    'C2' : ('201', '204'),
    'C3' : ('201', '202', '203'),
    'D3' : ('101', '102', '103'),
    'D4' : ('101', '104'),
    'A4' : ('401', '404'),
    'E1' : ('303', '403', '501'),
    'E5' : ('403', '406', '501'),
    'E6' : ('303', '305', '501'),
    'F2' : ('204', '205', '304', '305', '501'),
    'F6' : ('303', '305', '501'),
    'F7' : ('203', '205', '501'),
    'G3' : ('103', '203', '501'),
    'G7' : ('203', '205', '501'),
    'G8' : ('103', '105', '501'),
    'H4' : ('104', '105', '404', '405', '406', '501')}

room_to_room = {
    '101' : ('102', '104'),
    '102' : ('101', '103', '105'),
    '103' : ('102', '105'),
    '104' : ('101', '105'),
    '105' : ('102', '103', '104'),

    '201' : ('202', '204'),
    '202' : ('201', '203', '205'),
    '203' : ('202', '205'),
    '204' : ('201', '205'),
    '205' : ('202', '203', '204'),

    '301' : ('302', '304'),
    '302' : ('301', '303', '305'),
    '303' : ('302', '305'),
    '304' : ('301', '305'),
    '305' : ('302', '303', '304'),

    '401': ('402', '404'),
    '402' : ('401', '403', '404', '405', '406'),
    '403' : ('402'),
    '404' : ('401', '404', '405', '406'),
    '405' : ('402', '404', '406'),
    '406' : ('402', '405')}

room_to_dungeon = {
    '101' : ('D3', 'D4'),
    '102' : ('D3'),
    '103' : ('D3', 'G3', 'G8'),
    '104' : ('D4', 'H4'),
    '105' : ('H4', 'H8'),

    '201' : ('C2', 'C3'),
    '202' : ('C3'),
    '203' : ('C3', 'G3', 'G7'),
    '204' : ('C2', 'F2'),
    '205' : ('F2', 'F7'),

    '301' : ('B1', 'B2'),
    '302' : ('B1'),
    '303' : ('B1', 'E1', 'E6'),
    '304' : ('B2', 'F2'),
    '305' : ('F2', 'F6'),

    '401': ('A1', 'A4'),
    '402' : ('A1'),
    '403' : ('A1', 'E1'),
    '404' : ('A4', 'H4'),
    '405' : ('H4'),
    '406' : ('H4', 'H5'),

    '501' : ('E1', 'E5', 'E6', 'F2', 'F6', 'F7', 'G3', 'G7', 'G8', 'H4', 'H5', 'H8')}




def find_route(b, a):
    start = b
    arrive = a
    current = start
    path_temp = [start]
    count = 0
    while current != arrive and count <= 25:
        local_paths = points_of_view[current]
        length_list = len(local_paths)
        rng = random.SystemRandom()
        slice_number = rng.randint(0, int(length_list)-1)
        current_temp_pov = local_paths[slice_number]
        if current_temp_pov in path_temp:
            pass
        else:
            path_temp.append(current_temp_pov)
            current = current_temp_pov
            count = 0
        count +=1

    return path_temp


#INSERT VALUES 
start = '1' #CHOOSED RANDOMLY BY THE GAME
arrive = 'B' #CHOOSED RANDOMLY BY THE GAME
min_path = 3 #CHOOSED RANDOMLY BY THE GAME
the_primary_path = ''


#THEN PUSH THE BUTTON

the_primary_path = find_route(start,arrive)
while len(the_primary_path) < min_path or arrive != the_primary_path[-1]:
    the_primary_path = find_route(start, arrive)

print(str("The Dungeon Path is: "))
print(str(the_primary_path))

#THE GAME CHOOSE A SECONDARY PATH

half = len(the_primary_path) // 2
the_secondary_path_temp = the_primary_path[0:half]

for i in points_of_view.keys():
    if i not in the_primary_path:
        the_secondary_arrive = i
        print("the secondary arrive is:")
        print(the_secondary_arrive)
        break


the_secondary_start = the_secondary_path_temp[-1]
#CHOOSED RANDOMLY BY THE GAME

the_scondary_min_path = len(the_primary_path) #the current path lenght of primary_path
the_path = ''

#THEN PUSH THE BUTTON

#INSERT VALUES

#THEN PUSH THE BUTTON


secondary_res = find_route(the_secondary_start,the_secondary_arrive)

while len(secondary_res) >= len(the_primary_path) or the_secondary_arrive != secondary_res[-1]:
    secondary_res = find_route(the_secondary_start, the_secondary_arrive)

print("the secondary path is: ")
print(str(secondary_res))



def define_the_dugeons(p):
    the_path_temp = p


