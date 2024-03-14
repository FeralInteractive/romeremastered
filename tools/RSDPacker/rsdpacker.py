import struct
import os

byte_debugging = False

def read_int(infile):
    if (byte_debugging):
        debug_output_next_n_bytes(infile,4)
    return struct.unpack('i',infile.read(4))[0]

def read_uint(infile):
    if (byte_debugging):
        debug_output_next_n_bytes(infile,4)
    return struct.unpack('I',infile.read(4))[0]

def read_long(infile):
    if (byte_debugging):
        debug_output_next_n_bytes(infile,8)
    return struct.unpack('l',infile.read(8))[0]

def read_short(infile):
    if (byte_debugging):
        debug_output_next_n_bytes(infile,2)
    return struct.unpack('h',infile.read(2))[0]

def read_ushort(infile):
    if (byte_debugging):
        debug_output_next_n_bytes(infile,2)
    return struct.unpack('H',infile.read(2))[0]

def read_float(infile):
    if (byte_debugging):
        debug_output_next_n_bytes(infile,4)
    return struct.unpack('f',infile.read(4))[0]

def read_bool(infile):
    if (byte_debugging):
        debug_output_next_n_bytes(infile,1)
    return struct.unpack('?',infile.read(1))[0]

def read_char_string(infile):
    string = b''
    lastchar = b''
    while (not lastchar == b'\x00'):
        lastchar = read_char(infile)
        string += lastchar
    return string

def read_fixstring(infile,chars):
    return struct.unpack('{}s'.format(chars),infile.read(chars))[0]

def read_unichar_string(infile):
    string = b''
    lastchar = b''
    while (not lastchar == b'\x00\x00'):
        lastchar = read_unichar(infile)
        string += lastchar
    return string

def read_char(infile):
    if (byte_debugging):
        debug_output_next_n_bytes(infile,1)
    return struct.unpack('c',infile.read(1))[0]

def read_unichar(infile):
    return struct.unpack('2s',infile.read(2))[0]

def debug_output_next_n_bytes(infile,n):
    currpos = infile.tell()
    for i in range(n):
        print(r"\x"+str(infile.read(1).hex()),end="")
    infile.seek(currpos)
    print("")

def read_no_incr(infile,length=1):
    pos = infile.tell()
    dat = infile.read(length)
    infile.seek(pos)
    return dat

def read_pad(infile, length=1):
    infile.read(length)

def as_string(bytestring):
    try:
        return bytestring.decode('utf-8')[0:-1]
    except:
        return "ERROR_INVALID_STRING"

def as_unistring(bytestring):
    try:
        return bytestring.decode('utf-16')[0:-2]
    except:
        return "ERROR_INVALID_STRING"

def read_byte_flags(infile, length):
    #if length == Max_Factions:
    #    length = OldMax_Factions
    return_array = []
    for i in range((length >> 3) + 1):
        char_rep = ord(read_char(infile))
        bit = 128
        temp_array = []
        while (bit > 0):
            temp_array.append(char_rep >= bit)
            char_rep %= bit
            bit = int(bit/2)
        temp_array.reverse()
        return_array += temp_array
    #if length == OldMax_Factions:
    #    length = Max_Factions
    #    return_array += [False]*(len(return_array)-Max_Factions)
    return return_array[0:length]

def write_byte_flags(inarray):
    return_array = []
    for i in range((len(inarray) >> 3) + 1):
        rep = 0
        bit = 1
        for j in range(8):
            if ((i*8)+j < len(inarray) and inarray[(i*8)+j]):
                rep += bit
            bit *= 2
        return_array.append(rep)
    return bytes(return_array)

page_names = [
    "UI_BATTLE_SPRITE_PAGE",
    "UI_SHARED_SPRITE_PAGE",
    "UI_STRAT_SPRITE_PAGE",
    #"UI_OVERVIEW_SPRITE_PAGE",
    #"UI_DIPLOMACY_BUTTONS_PAGE",
    #"UI_BATTLE_ED_SPRITE_PAGE",
    #"UI_STRAT_ED_SPRITE_PAGE",
    "UI_STRAT_V2_SPRITE_PAGE",
    "UI_BATTLE_V2_SPRITE_PAGE",
    #"UI_EDITOR_SHARED_SPRITE_PAGE",
]
rsds = [
    "battle.rsd",
    "shared2.rsd",
    "strat.rsd",
    #"overview.rsd",
    #"diplomacy_toolbar.rsd",
    #"battle_ed.rsd",
    #"strat_ed.rsd",
    "strat3.rsd",
    "battle3.rsd",
    #"shared_editor.rsd",
]

from PIL import Image
import struct
import math

directory = "./"

class SubImage:
    def __init__(self,f):
        #self.size = f.tell()
        string_size = read_uint(f)
        self.file_path = read_fixstring(f,string_size)
        #print(self.file_path,f.tell())
        #print(self.file_path)

        self.tex_handle = read_ushort(f)
        #print("Tex_handle =",self.tex_handle)
        self.left = read_ushort(f)
        self.right = read_ushort(f)
        self.top = read_ushort(f)
        self.bottom = read_ushort(f)
        self.alpha = read_bool(f)
        self.cursor = read_bool(f)
        self.x_offset = read_ushort(f)
        self.y_offset = read_ushort(f)
        #print("l",self.left,"r",self.right,"t",self.top,"b",self.bottom,"x",self.x_offset,"y",self.y_offset)
        #self.size = f.tell() - self.size
        #print("Read",self.size)

    def write(self,f):
        #print(self.file_path)
        #s = f.tell()
        f.write(struct.pack("=I{}sHHHHH??HH".format(len(self.file_path)),len(self.file_path),self.file_path,self.tex_handle,self.left,self.right,self.top,self.bottom,self.alpha,self.cursor,self.x_offset,self.y_offset))
        #print("Wrote",f.tell()-s)

def generate_new_collision_map(image_path):
    threshhold = 128

    im = Image.open(image_path)
    data = list(im.getdata(3))
    first = True
    n = 0
    c = 0
    ns = []
    bytestream = []
    print(len(data))
    for i in range(len(data)):
        #print(data[i])
        if (data[i] > threshhold):
            n |= 1 << c
            #bytestream.append(b'\x00')
        #else:
            #bytestream.append(b'\xff')
        
        c+=1
        if (c % 8 == 0):
            c = 0
            ns.append(n)
            n = 0
    ns.append(n)
    asbytes = bytes(ns)

    return asbytes

    #bytestream = b''.join(bytestream)
    #newim = Image.frombuffer('L',(im.width,im.height),bytestream)
    #newim.save("image_collission_map.bmp")

regen_collisions = False
re_serialise = True

class TexPage:
    def __init__(self, f):
        #self.size = f.tell()
        string_size = read_uint(f) #skip weird first path
        self.weird_string = read_fixstring(f,string_size);
        #print(read_fixstring(f,string_size))
        #read_pad(f,string_size)
        
        string_size = read_uint(f)
        self.page_name = read_fixstring(f,string_size) #get page name
        print(self.page_name)
        #print(" - tex page:",self.page_name)

        self.force32 = read_bool(f)
        
        self.width = read_uint(f)
        self.height = read_uint(f)

        bit_array_size = read_uint(f)
        print("Calculated bytes:",self.width,"x",self.height,"/ 8 =",(self.width*self.height)/8,"actual:",bit_array_size,f.tell());
        self.collision_map = f.read(bit_array_size)

        if (regen_collisions):
            collisionDir = directory+"data/ui/roman/interface"
            if (not os.path.exists(collisionDir)):
                os.mkdir(collisionDir)
            self.collision_map = generate_new_collision_map(collisionDir +"/"+self.page_name.decode('UTF-8'))

        asbytes = []
        report_every = 100000
        accumulator = 0
        total = (self.width*self.height)
        for i in self.collision_map:
            for c in range(8):
                 asbytes.append(b'\x00' if ((1 << c) & i) else b'\xff')
            if (accumulator % report_every == 0):
                print(accumulator,"/",total)
            accumulator += 1
            #print(i,end="")
        collim = Image.frombytes('L',(self.width,self.height),b''.join(asbytes))
        
        outputdir = "spritesheet_unpack"
        if (not os.path.exists(outputdir)):
            os.mkdir(outputdir)
            
        collim.save(outputdir+"/"+self.page_name.decode('utf-8')+"_collision.tga")
        #self.size = f.tell() - self.size
        #print("Read",self.size)

    def write(self,f):
        #print(self.page_name)
        #s = f.tell()
        f.write(struct.pack("=I{}sI{}s?III{}s".format(len(self.weird_string),len(self.page_name),len(self.collision_map)),len(self.weird_string),self.weird_string,len(self.page_name),self.page_name,self.force32,self.width,self.height,len(self.collision_map),self.collision_map))
        #print("Wrote",f.tell()-s)

class RSD:
    def __init__(self, f, pageid, pagestring):
        self.pageid = pageid
        self.name = pagestring
        self.version = read_uint(f)
        self.num_tex_pages = read_uint(f)
        self.num_sprites = read_uint(f)
        
        string_size = read_uint(f)
        self.enum_name = read_fixstring(f,string_size)
        print("Enum name:",self.enum_name)
        
        self.tex_pages = []
        for i in range(self.num_tex_pages):
            self.tex_pages.append(TexPage(f))

        self.sprites = []
        for i in range(self.num_sprites):
            #print(" - sprite("+str(i)+")",end = " = ")
            self.sprites.append(SubImage(f))

    def output(self):
        #if (len(enums) < len(self.sprites)):
        #    print("Need at least as many enums as sprites ("+str(len(enums))+" enums vs",len(self.sprites),"sprites)")
        #    return
        outputdir = "spritesheet_unpack"
        if (not os.path.exists(outputdir)):
            os.mkdir(outputdir)
        outputdir = outputdir +"/"+self.name
        if (not os.path.exists(outputdir)):
            os.mkdir(outputdir)

        bigimages = []
        
        tgadir = "data/ui/roman/interface/"
        serialized = (os.path.exists("spritesheet_repack"))
        if(serialized):
            tgadir = "spritesheet_repack/"
            print("Using repacked interface images located in [spritesheet_repack/]")
        else:
            print("Failed to locate - [spritesheet_repack/] directory. Using ["+tgadir+ "] instead!")
        
        for i in self.tex_pages:
            bigimages.append(Image.open(directory+tgadir+i.page_name.decode('UTF-8')))

        for i in range(len(self.sprites)):
            im = self.sprites[i]
            area = (im.left,im.top,im.right,im.bottom)
            sub = bigimages[im.tex_handle].crop(area)
            imgname = (im.file_path.decode('UTF-8').split(".")[0])
            c = 0
            while (not imgname[c].isalpha()):
                c+=1
            imgname = im.file_path#"("+str(i)+")"+enums[i].replace("CUS_FERAL_","").replace("BUS_FERAL_","")+"_"+imgname[c:len(imgname)]
            sub.save(outputdir+"/"+imgname.decode('utf-8').split(".")[0] + ".tga")

    def write(self,f):
        f.write(struct.pack("=IIII{}s".format(len(self.enum_name)),self.version,self.num_tex_pages,self.num_sprites,len(self.enum_name),self.enum_name))
        for i in self.tex_pages:
            i.write(f)
        for i in self.sprites:
            i.write(f)

        
        outputdir = "spritesheet_repack/"
        if (not os.path.exists(outputdir)):
            os.mkdir(outputdir)
        
        inputdir = "spritesheet_unpack/"+self.name
        if (not os.path.exists(inputdir)): 
            return
        
        bigimages = []
        imagesOutDir = []
        for i in self.tex_pages:
            outputImageDir = (outputdir+i.page_name.decode('UTF-8'))
            #print(outputImageDir)
            
            bigimage = Image.new("RGBA", (i.width, i.height))
            bigimages.append(bigimage)
            imagesOutDir.append(outputImageDir)
        for i in range(len(self.sprites)):
            im = self.sprites[i]
            area = (im.left,im.top,im.right,im.bottom)
            imgname = (im.file_path.decode('UTF-8').split(".")[0])
            c = 0
            while (not imgname[c].isalpha()):
                c+=1
            imgname = im.file_path#"("+str(i)+")"+enums[i].replace("CUS_FERAL_","").replace("BUS_FERAL_","")+"_"+imgname[c:len(imgname)]
            imgname = imgname.decode('utf-8').split(".")[0] + ".tga"
            subimage = Image.open(inputdir + "/" + imgname)
            bigimages[im.tex_handle].paste(subimage, area)
            
        for i in range(len(bigimages)):
            bigimages[i].save(imagesOutDir[i])
            print("Writing: "+ imagesOutDir[i])
pages = {}

def open_rsd(page_id):
    if (not os.path.exists(directory+"data/ui/"+rsds[page_id])):
        #print("Unable to open",page_names[page_id]+":",rsds[page_id])
        return
    f = open(directory+"data/ui/"+rsds[page_id],'rb')
    print("Opening",page_names[page_id]+":",rsds[page_id])
    pages[page_names[page_id]] = RSD(f,page_id,page_names[page_id])
    f.close()

def get_page(page_id, sprite_index):
    if (not page_id in pages):
        print("Page",page_id,"wasn't loaded!")

    page = pages[page_id]

    if (sprite_index >= page.num_sprites):
        print("Sprite index is out of range")

    print(page.sprites[sprite_index].file_path)

print("Starting")

deserialized = (os.path.exists("spritesheet_unpack"))

for i in range(len(page_names)):
    open_rsd(i)

if (re_serialise):
    if(deserialized):
        print("\n=============")
        print("Reserializing")
        print("=============")
        for i in range(len(page_names)):
            if (page_names[i] in pages):
                #print(directory+"data/ui/"+rsds[pages[page_names[i]].pageid])
                newf = open(directory+"data/ui/"+rsds[pages[page_names[i]].pageid],'wb')
                #print(page_names[i])
                pages[page_names[i]].write(newf)
                newf.close()
        print("=============\n")
    else:
        print("=============")
        print("Skipped reserializing -> You need deserialized files first!")
        print("Run this script again to reserialize, because deserialization should be done automatically...")
        print("=============")   
        
for i in range(len(page_names)):
    if (page_names[i] in pages):
        print(page_names[i])
        pages[page_names[i]].output()
