#for packing an unpacking
import struct
#for checking the directory
import os

#utility methods
def read_int(infile):
    return struct.unpack('i',infile.read(4))[0]

def read_uint(infile):
    return struct.unpack('I',infile.read(4))[0]

def read_long(infile):
    return struct.unpack('l',infile.read(8))[0]

def read_short(infile):
    return struct.unpack('h',infile.read(2))[0]

def read_ushort(infile):
    return struct.unpack('H',infile.read(2))[0]

def read_float(infile):
    return struct.unpack('f',infile.read(4))[0]

def read_bool(infile):
    return struct.unpack('?',infile.read(1))[0]

def read_char(infile):
    return struct.unpack('c',infile.read(1))[0]

def read_pad(infile, length=1):
    infile.read(length)

def read_char_string(infile):
    string = b''
    lastchar = b''
    while (not lastchar == b'\x00'):
        lastchar = read_char(infile)
        string += lastchar
    return string

def as_string(bytestring):
    try:
        return bytestring.decode('utf-8')[0:-1]
    except:
        return "ERROR_INVALID_STRING"

#global variable to store the version of the current pack
packver = 0

#vector3 class, very simple and standard
class Vector3:
    def __init__(self, fromfile = None):
        if (fromfile):
            self.initialiseFile(fromfile)
        else:
            self.initialiseDefault()
            
    def initialiseFile(self, fromfile):
        self.X = read_float(fromfile)
        self.Y = read_float(fromfile)
        self.Z = read_float(fromfile)

    def initialiseDefault(self):
        self.X = 0
        self.Y = 0
        self.Z = 0

    def getfulloutputformat(self):
        sformat = "fff"
        return sformat

    def transcribe(self):
        datatopack = [
            self.X,
            self.Y,
            self.Z
        ]
        return datatopack

    #operators
    def __mul__(self, by):
        self.X *= by
        self.Y *= by
        self.Z *= by
        return self
    def __eq__(self, other):
        return other and (
            self.X == other.X and
            self.Y == other.Y and
            self.Z == other.Z
        )

#representation of a bone
class Bone:
    def __init__(self, fromfile):
        """
        types:
            0 = unknown
            1 = saddle
            2 = platform (?)
            3 = wheel
            4 = left hand
            5 = right hand
        """
        #type of bone, used for attachment points, see above
        self.type = read_uint(fromfile)

        #obvious
        self.pose =   Vector3(fromfile)

        #index of the bone this one is connected to
        self.parent_index    =  read_int(fromfile)

        #???
        self.has_translation = read_bool(fromfile)

        #IK control
        self.apply_IK        = read_bool(fromfile)

        #manual padding
        read_pad(fromfile,2)

    #get the packing format
    def getfulloutputformat(self):
        sformat = "I" + self.pose.getfulloutputformat() + "i??h"
        return sformat

    #write the data
    def transcribe(self):
        datatopack = [
            self.type
        ]
        for i in self.pose.transcribe():
            datatopack.append(i)
        datatopack += [
            self.parent_index,
            self.has_translation,
            self.apply_IK,
            #0 for padding
            0,
        ]
        return datatopack

#string conversions from misc sounds to banked sounds
shouldbeambient = """DRUID_CHANT
ANIM_SCREECHERS
ANIM_ARCHER_AIM
ANIM_ARCHER_FIRE
ANIM_ARCHER_LOAD
ANIM_SLINGER_FIRE
ANIM_SLINGER_HIGHWHIRL
ANIM_SLINGER_LOWWHIRL
ANIM_IDLE_CLOTH
ANIM_KILL_MOUNT
ANIM_SCRAPE
ANIM_SPEAR_FIRE
ANIM_SQUASH
ANIM_SWOOSH
ANIM_TESTUDO
ANIM_FALL_SQUASH""".split("\n")
ambientreplacement = """chant
chant
archer_aim
archer_fire
archer_load
slinger_fire
slinger_highwhirl
slinger_lowwhirl
move_cloth
kill_mount
scrape
spear_fire
squash
swoosh
testudo_adjust
fall_squash""".split("\n")
shouldbeanimal = """ANIM_CAMEL_ATTACK
ANIM_CAMEL_DEATH
ANIM_CHARIOT_DESTROY
ANIM_ELE_ATTACK
ANIM_ELE_DEATH
ANIM_HORSE_ATTACK
ANIM_HORSE_DEATH
ANIM_HORSE_REGROUP
ANIM_PIG_ATTACK
ANIM_PIG_DEATH
ANIM_WARDOG_ATTACK
ANIM_WARDOG_BARK
ANIM_WARDOG_DEATH
FLAMING_PIG
ANIM_ELE_HEADBUTT_BUILDING""".split("\n")
animalreplacement = """attack
death
death
attack
death
attack
death
speak
attack
death
attack
speak
death
burn
ram""".split("\n")
done = []
#keyframed sound event
class Anim_Event:
    def __init__(self, fromfile=None):
        if (fromfile):
            self.initialiseFile(fromfile)
        else:
            self.initialiseDefault()
    
    def initialiseDefault(self):
        self.type = 0
        self.startframe = 0
        self.endframe = 0
        self.id = b'\x00'
        self.extra = 0.0

    def initialiseFile(self, fromfile):
        global packver

        #type of sound
        """
        Unknown
        misc_sound - pull from unrestricted misc sound bank, id is sound ID
        footstep - footstep sound, extra defines which bank to use (human walk, human run, human fall, then repeat for animals)
        shockwave - apply a shockwave to the camera, extra defines strength (seems nonfunctional?)
        unit sound - use unit anim bank to filter sounds by unit parameters, id defines the anim ID
        animal sound - same as above but for animal anim bank, which filters mostly by animal class
        """
        self.type = read_uint(fromfile)

        #conversions from old(ver 3)->new(ver 4)
        typeswizzle = [
            0, #unknown -> unknown
            5, #sound -> misc_sound
            1, #sound_bank -> footstep
            2, #shockwave -> shockwave
            3, #sound_voice -> unit sound
            3, #ambient -> unit sound
            ]

        #start and end frame for the sound (end used for either random in range or looped sounds)
        self.startframe  = read_ushort(fromfile)
        self.endframe    = read_ushort(fromfile)

        #conversion stuff
        if (packver == 3):
            #old version always used IDs for everything, which was dumb
            self.id = read_char_string(fromfile)
            self.extra = 0.0

            #remap old anim names into new formats
            alreadyambient = [b'stretch_back\x00',b'neck_crack\x00',b'clear_throat\x00',b'sniff\x00',b'exert\x00',b'relief\x00',b'scratch_head\x00',b'stretch_arms\x00',b'sneeze\x00',b'2\x00',b'taunt_hit\x00',]
            voice_remapping = {b'INDIVIDUAL_ATTACK_GRUNT\x00':b'attack grunt\x00', b'INDIVIDUAL_ATTACK_SCREAM\x00':b'attack scream\x00', b'INDIVIDUAL_DEATH\x00':b'death cry\x00', b'Death_Cry\x00':b'death cry\x00', b'Fall_Scream\x00':b'fall scream\x00', b'INDIVIDUAL_FALL_GRUNT\x00':b'Fall grunt\x00', b'Inviduals_Charge\x00':b'Charge\x00', b'Attack_Scream\x00':b'Attack scream\x00', b'INDIVIDUAL_GRUNT\x00':b'Grunt\x00', b'Individuals_Grunt\x00':b'Grunt\x00', b'Taunting\x00':b'Taunt\x00', b'Celebration\x00':b'Celebrate\x00'}
            shockwave_remapping = {b'ELE_WALK\x00':1.0, b'ELE_RUN\x00':1.5, b'ELE_DIE\x00':3.0}
            soundbank_remapping = [b'unit_march\x00', b'unit_run\x00', b'fall\x00', b'animal_footstep_walk\x00', b'animal_footstep_run\x00', b'animal_fall\x00']

            remaps = [
                [soundbank_remapping],
                [shockwave_remapping],
                [voice_remapping,shouldbeambient,alreadyambient],
                [shouldbeanimal],
            ]
            #default to misc sound, can't go wrong there
            self.type = 5
            sub_type = 0
            #check every remap list, if the id is contained in there assume it's that one
            for i in range(len(remaps)):
                for j in range(len(remaps[i])):
                    if (self.id in remaps[i][j] or as_string(self.id) in remaps[i][j]):
                        self.type = i+1
                        sub_type = j
                        break
            types = ["Unknown","Footstep","Shockwave","Unit sound","Animal sound","Misc sound"]
            if (not self.id in done):
                done.append(self.id)
                print("Remapping",as_string(self.id),"to type",self.type,"("+types[self.type]+")")

            #translate string ID as needed
            if (self.type == 1): #soundbank
                self.extra = soundbank_remapping.index(self.id) % 3
            if (self.type == 2):
                self.extra = shockwave_remapping[self.id]
            if (self.type == 3):
                #don't need to convert existing ambient anims
                if sub_type == 2:
                    pass
                #do proper conversion if else
                elif sub_type == 0:
                    self.id = voice_remapping[self.id].lower()
                else:
                    self.extra = ambientreplacement[shouldbeambient.index(as_string(self.id))].replace("!","").encode('UTF-8')+b'\x00'
            if (self.type == 4):
                self.extra = animalreplacement[shouldbeanimal.index(as_string(self.id))].replace("!","").encode('UTF-8')+b'\x00'
                

        #non-conversion stuff
        else:
            self.id = b'\x00'
            self.extra = 0.0

            #footstep takes in the bank
            if (self.type == 2):
                self.extra = read_uint(fromfile)

            #shockwave takes in the strength
            elif (self.type == 3):
                self.extra = read_float(fromfile)

            #everything else wants an ID
            else:
                self.id = read_char_string(fromfile)

        #should trigger on a random frame within the range
        self.randomframe =   read_bool(fromfile)

        #should loop within range (I think)
        self.looped      =   read_bool(fromfile)

    #write out the packing format
    def getfulloutputformat(self):
        sformat = "IHH"
        if (self.type == 1):
            sformat += "I"
        elif (self.type == 2):
            sformat += "f"
        else:
            sformat +="{}s".format(len(self.id))
        sformat += "??"
        return sformat

    #write in the data
    def transcribe(self):
        datatopack = [
            self.type,
            self.startframe,
            self.endframe,
            
            self.extra if (self.type in [1,2]) else self.id,
        
            self.randomframe,
            self.looped
        ]
        
        return datatopack

#parameters for a given animation
class Anim_Params:
    def __init__(self, fromfile = None):
        if (fromfile):
            self.initialiseFile(fromfile)
        else:
            self.initialiseDefault()
    
    def initialiseDefault(self):
        self.delta_rot = 0
        self.delta_impact = Vector3()
        self.delta_angle  = 0
        self.delta_length = 0
        self.impact_frame = 0
        self.impact_dist  = 0
        self.min_turn_del = 0
        self.max_turn_del = 0
        self.launch_dir = Vector3()
        self.num_events = 0
        self.events = []

    def initialiseFile(self, fromfile,dvars = None):
        #I'll be honest, I'm the sound girl, I don't know what most of this does
        self.delta_rot    = read_short(fromfile)
        self.delta_impact =    Vector3(fromfile)
        self.delta_angle  = read_short(fromfile)
        self.delta_length = read_float(fromfile)
        self.impact_frame =read_ushort(fromfile)
        self.impact_dist  = read_float(fromfile)
        self.min_turn_del = read_short(fromfile)
        self.max_turn_del = read_short(fromfile)
        self.launch_dir   =    Vector3(fromfile)
        
        num_events = read_uint(fromfile)
        self.events = []
        for i in range(num_events):
            self.events.append(Anim_Event(fromfile))

    def getfulloutputformat(self):
        sformat = "h" + self.delta_impact.getfulloutputformat() + "hfHfhh" + self.launch_dir.getfulloutputformat() + "I"
        for i in self.events:
            sformat += i.getfulloutputformat()
        return sformat

    def transcribe(self):
        datatopack = [self.delta_rot]
        datatopack += self.delta_impact.transcribe()
        datatopack += [
            self.delta_angle,
            self.delta_length,
            self.impact_frame,
            self.impact_dist,
            self.min_turn_del,
            self.max_turn_del
        ]
        datatopack += self.launch_dir.transcribe()
        datatopack += [len(self.events)]

        for i in self.events:
            datatopack += i.transcribe()
        
        return datatopack

class Skeleton:
    def __init__(self, tup):
        global curranim
        
        idxfile = tup[2]
        datfile = tup[3]

        #ID of the skeleton
        self.id = read_char_string(idxfile)

        #for rescaling? idk
        self.scale = read_float(datfile)

        #number of bones
        self.num_nodes = read_ushort(datfile)

        #I have no idea what a trans node is but I support it
        self.num_nodes_with_trans_rights = read_ushort(datfile)

        # ???
        self.IK_lerp_fraction = read_float(datfile)

        #read in the bones
        self.nodes = []
        for i in range(self.num_nodes):
            self.nodes.append(Bone(datfile))

        #read in the animations
        self.anims = []
        #300 possible animation enums to assign an animation to
        for i in range(300):
            path = read_char_string(datfile)
            #null string represents no animation
            if (path != b'\x00'):
                #link the path and the animation together
                self.anims.append([path,Anim_Params(datfile)])
            else:
                #add a default entry for null entries
                self.anims.append([b'\x00',Anim_Params()])

        #movement speeds
        self.walk_speed   = read_float(datfile)
        self.run_speed    = read_float(datfile)
        self.charge_speed = read_float(datfile)

        #can this skeleton use missiles?
        self.can_missile  =  read_bool(datfile)
        #can this skeleton turn in place?
        self.can_ip_turn  =  read_bool(datfile)

    def getfulloutputformat(self):
        sformat = "fHHf"
        for i in self.nodes:
            sformat += i.getfulloutputformat()
        for i in self.anims:
            #no animation gets a null byte
            if (i[0] == b'\x00'):
                sformat += "c"
            else:
                #otherwise output the string followed by the animation
                sformat += "{}s".format(len(i[0]))
                sformat += i[1].getfulloutputformat()
        sformat += "fff??"
        return sformat

    def transcribe(self):
        datatopack = [
            self.scale,
            self.num_nodes,
            self.num_nodes_with_trans_rights,
            self.IK_lerp_fraction
        ]
        for i in self.nodes:
            datatopack += i.transcribe()
        for i in self.anims:
            datatopack.append(i[0])
            #if not null add the data too
            if (i[0] != b'\x00'):
                datatopack += i[1].transcribe()
        datatopack += [
            self.walk_speed,
            self.run_speed,
            self.charge_speed,
            self.can_missile,
            self.can_ip_turn
        ]

        #pack without padding
        datData = struct.pack("="+self.getfulloutputformat(),*datatopack)

        return (self.id, datData)

if (os.path.exists("skeletons.dat")):
    path = "skeletons"
else:
    path = str(input("Enter the path of the skeleton file you want to convert:\n")).replace('.dat','').replace('.idx','')
idx = open(path+".idx",'rb')
dat = open(path+".dat",'rb')

"""
    Header content:
        9 chars text ID
        32 bit uint version number
        32 bit uint num records
"""
idxHeaderStruct = struct.unpack('9sII',idx.read(20))
datHeaderStruct = struct.unpack('9sII',dat.read(20))

idxIDstr = idxHeaderStruct[0]
datIDstr = datHeaderStruct[0]

if (idxIDstr != datIDstr):
    print(".dat and .idx are not the same type of pack file!")
    raise IOError
if (idxIDstr != b'SKEL.PACK'):
    print("these are not sound packs!")
    raise IOError

idxVer = idxHeaderStruct[1]
datVer = datHeaderStruct[1]

if (idxVer != datVer):
    print(".dat and .idx have mismatching versions!")
    raise IOError

packver = idxVer

idxNumRecords = idxHeaderStruct[2]
datNumRecords = datHeaderStruct[2]

if (idxNumRecords != datNumRecords):
    print(".dat and .idx have mismatching numbers of records!")
    raise IOError

#if we reach this point, all good

spookyscaryskeletons = []

#unpack
for i in range(idxNumRecords):
    idx_size   = read_uint(idx)
    dat_offset = read_uint(idx)
    dat_size   = read_uint(idx)

    dat.seek(dat_offset) #protect against misalignment

    spookyscaryskeletons.append(Skeleton((idx_size,dat_size,idx,dat)))

#if you want to edit anything, do it here

#repack
idx.close()
dat.close()
idx = open(path+"_new.idx",'wb')
dat = open(path+"_new.dat",'wb')

#upgrade version
if (packver == 3):
    packver = 4

#write the headers
idx.write(struct.pack('9sII',idxIDstr,packver,len(spookyscaryskeletons)))
dat.write(struct.pack('9sII',idxIDstr,packver,len(spookyscaryskeletons)))

#initalise the offset
dat_offset = 20
for i in spookyscaryskeletons:
    data = i.transcribe()

    #entry header
    idx.write(struct.pack("III",len(data[0]),dat_offset,len(data[1])))

    #actual data
    idx.write(data[0])
    dat.write(data[1])

    #increment offset
    dat_offset += len(data[1])

print("Done upgrading file!")

idx.close()
dat.close()
