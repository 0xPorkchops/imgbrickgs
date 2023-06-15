#Welcome to ImgBrick GS (Made by GShocked).
#This program will convert images that the Python Imaging Library supports and turns them into Roblox models, with various options available.
#You can see a video tutorial of an older version of this at https://www.youtube.com/watch?v=MVKOzHdd1m4

#Technical Ideas
#   Make into a GUI program
#   Make it create a New File (1) if the requested file name already exists, maybe make this optional
#   Fix the repetition of /item /roblox tags in several ending strings
#   Optimize file sizes by adjusting unnecessary header information
#   Change loop to be individual in options, so that it doesn't loop all those if statements, which should save time

#Feature Ideas
#   Add option to use misinterpreted colors
#       Add option to adjust for the color misinterpretation

import Image
import math

Model1 = """<roblox xmlns:xmime="http://www.w3.org/2005/05/xmlmime" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.roblox.com/roblox.xsd" version="4">
	<External>null</External>
	<External>nil</External>
	<Item class="Model" referent="RBX921BBA7D6AEF4143ADDB298CD197EC45">
		<Properties>
			<CoordinateFrame name="ModelInPrimary">
				<X>0</X>
				<Y>0</Y>
				<Z>0</Z>
				<R00>1</R00>
				<R01>0</R01>
				<R02>0</R02>
				<R10>0</R10>
				<R11>1</R11>
				<R12>0</R12>
				<R20>0</R20>
				<R21>0</R21>
				<R22>1</R22>
			</CoordinateFrame>
			<string name="Name">ImgBrick</string>
			<Ref name="PrimaryPart">null</Ref>
		</Properties>"""
#Insert pixels
Model2 = """	</Item>
</roblox>"""

Part1 = """		<Item class="Part" referent="RBXD7428C2B72934DEE8EE1ADCC57C99670">
			<Properties>
				<bool name="Anchored">true</bool>
				<float name="BackParamA">-0.5</float>
				<float name="BackParamB">0.5</float>
				<token name="BackSurface">10</token>
				<token name="BackSurfaceInput">0</token>
				<float name="BottomParamA">-0.5</float>
				<float name="BottomParamB">0.5</float>
				<token name="BottomSurface">10</token>
				<token name="BottomSurfaceInput">0</token>
				<int name="BrickColor">"""
#Insert nearest brick color
Part2 = """</int>
				<CoordinateFrame name="CFrame">
					<X>"""
#Insert X position
Part3 = """</X>
					<Y>"""
#Insert Y position
Part4 = """</Y>
					<Z>"""
#Insert Z position
Part5 = """</Z>
					<R00>1</R00>
					<R01>0</R01>
					<R02>0</R02>
					<R10>0</R10>
					<R11>1</R11>
					<R12>0</R12>
					<R20>0</R20>
					<R21>0</R21>
					<R22>1</R22>
				</CoordinateFrame>
				<bool name="CanCollide">true</bool>
				<PhysicalProperties name="CustomPhysicalProperties">
					<CustomPhysics>false</CustomPhysics>
				</PhysicalProperties>
				<float name="Elasticity">0.5</float>
				<float name="Friction">0.300000012</float>
				<float name="FrontParamA">-0.5</float>
				<float name="FrontParamB">0.5</float>
				<token name="FrontSurface">10</token>
				<token name="FrontSurfaceInput">0</token>
				<float name="LeftParamA">-0.5</float>
				<float name="LeftParamB">0.5</float>
				<token name="LeftSurface">10</token>
				<token name="LeftSurfaceInput">0</token>
				<bool name="Locked">false</bool>
				<token name="Material">272</token>
				<string name="Name">Pixel</string>
				<float name="Reflectance">0</float>
				<float name="RightParamA">-0.5</float>
				<float name="RightParamB">0.5</float>
				<token name="RightSurface">10</token>
				<token name="RightSurfaceInput">0</token>
				<Vector3 name="RotVelocity">
					<X>0</X>
					<Y>0</Y>
					<Z>0</Z>
				</Vector3>
				<float name="TopParamA">-0.5</float>
				<float name="TopParamB">0.5</float>
				<token name="TopSurface">10</token>
				<token name="TopSurfaceInput">0</token>
				<float name="Transparency">0</float>
				<Vector3 name="Velocity">
					<X>0</X>
					<Y>0</Y>
					<Z>0</Z>
				</Vector3>
				<token name="formFactorRaw">3</token>
				<token name="shape">1</token>
				<Vector3 name="size">
					<X>1</X>
					<Y>1</Y>
					<Z>1</Z>
				</Vector3>
			</Properties>
"""

Part6 = """	</Item>"""

Mesh1 = """		<Item class="SpecialMesh" referent="RBX1">
			<Properties>
				<token name="LODX">2</token>
				<token name="LODY">2</token>
				<Content name="MeshId"><url>rbxassetid://9856898</url></Content>
				<token name="MeshType">5</token>
				<string name="Name">Mesh</string>
				<Vector3 name="Offset">
					<X>0</X>
					<Y>0</Y>
					<Z>0</Z>
				</Vector3>
				<Vector3 name="Scale">
					<X>2</X>
					<Y>2</Y>
					<Z>2</Z>
				</Vector3>
				<Content name="TextureId"><url>rbxassetid://1361097</url></Content>
				<Vector3 name="VertexColor">
					<X>"""
#Insert X color decimal (R?)
Mesh2 = """</X>
					<Y>"""
#Insert X color decimal (G?)
Mesh3 = """</Y>
					<Z>"""
#Insert X color decimal (B?)
Mesh4 = """</Z>
				</Vector3>
			</Properties>
		</Item>"""

BillboardGui1 = """<roblox xmlns:xmime="http://www.w3.org/2005/05/xmlmime" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.roblox.com/roblox.xsd" version="4">
	<External>null</External>
	<External>nil</External>
	<Item class="BillboardGui" referent="RBX2E9B9F3C614D449B807B7EF6DCD8A46A">
		<Properties>
			<bool name="Active">false</bool>
			<Ref name="Adornee">null</Ref>
			<bool name="AlwaysOnTop">true</bool>
			<bool name="Enabled">true</bool>
			<Vector3 name="ExtentsOffset">
				<X>0</X>
				<Y>0</Y>
				<Z>0</Z>
			</Vector3>
			<string name="Name">ImgBrick GS</string>
			<Ref name="PlayerToHideFrom">null</Ref>
			<UDim2 name="Size">
				<XS>0</XS>
				<XO>"""
#Insert BillboardGui X Offset size
BillboardGui2 = """</XO>
				<YS>0</YS>
				<YO>"""
#Insert BillboardGui Y Offset size
BillboardGui3 = """</YO>
			</UDim2>
			<Vector2 name="SizeOffset">
				<X>0</X>
				<Y>0</Y>
			</Vector2>
			<Vector3 name="StudsOffset">
				<X>0</X>
				<Y>0</Y>
				<Z>0</Z>
			</Vector3>
		</Properties>"""
#Insert pixels
BillboardGui4 = """	</Item>
</roblox>"""

Frame1 = """		<Item class="Frame" referent="RBXB8B442EED67D4787B684DC921D086BD1">
			<Properties>
				<bool name="Active">false</bool>
				<Color3 name="BackgroundColor3">"""
#Insert encoded backgroundcolor3
Frame2 = """</Color3>
				<float name="BackgroundTransparency">0</float>
				<Color3 name="BorderColor3">4278190080</Color3>
				<int name="BorderSizePixel">0</int>
				<bool name="ClipsDescendants">false</bool>
				<bool name="Draggable">false</bool>
				<string name="Name">Frame</string>
				<Ref name="NextSelectionDown">null</Ref>
				<Ref name="NextSelectionLeft">null</Ref>
				<Ref name="NextSelectionRight">null</Ref>
				<Ref name="NextSelectionUp">null</Ref>
				<UDim2 name="Position">
					<XS>0</XS>
					<XO>"""
#Insert X offset position
Frame3 = """</XO>
					<YS>0</YS>
					<YO>"""
#Insert Y offset position
Frame4 = """</YO>
				</UDim2>
				<float name="Rotation">0</float>
				<bool name="Selectable">false</bool>
				<Ref name="SelectionImageObject">null</Ref>
				<UDim2 name="Size">
					<XS>0</XS>
					<XO>1</XO>
					<YS>0</YS>
					<YO>1</YO>
				</UDim2>
				<token name="SizeConstraint">0</token>
				<token name="Style">0</token>
				<bool name="Visible">true</bool>
				<int name="ZIndex">1</int>
			</Properties>
		</Item>"""

ScreenGui1 = """<roblox xmlns:xmime="http://www.w3.org/2005/05/xmlmime" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.roblox.com/roblox.xsd" version="4">
	<External>null</External>
	<External>nil</External>
	<Item class="ScreenGui" referent="RBX71262B3D4CAE4DF1A5BB72924C51AEA7">
		<Properties>
			<string name="Name">ImgBrick GS</string>
		</Properties>"""
#Insert pixels
ScreenGui2 = """	</Item>
</roblox>"""

SurfaceGui1 = """<roblox xmlns:xmime="http://www.w3.org/2005/05/xmlmime" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.roblox.com/roblox.xsd" version="4">
	<External>null</External>
	<External>nil</External>
	<Item class="SurfaceGui" referent="RBX827C71C7434D407C845C857E8F96BC4C">
		<Properties>
			<bool name="Active">true</bool>
			<Ref name="Adornee">null</Ref>
			<Vector2 name="CanvasSize">
				<X>"""
#Insert x size
SurfaceGui2 = """</X>
				<Y>"""
#Insert y size
SurfaceGui3 = """</Y>
			</Vector2>
			<bool name="Enabled">true</bool>
			<token name="Face">5</token>
			<string name="Name">ImgBrick GS</string>
			<float name="ToolPunchThroughDistance">0</float>
		</Properties>"""
#Insert pixels
SurfaceGui4 = """	</Item>
</roblox>"""

BCPartScript1 = """l = {"""
#Insert color information
BCPartScript2 = """}
local w = """
#Insert image height
BCPartScript3 = """
local o = {0, 0, 0}
for i = #l, 1, -1 do
	p = Instance.new('Part', script)
	p.Size = Vector3.new(1, 1, 1)
    p.BrickColor = BrickColor.new(l[i])
    p.Position = Vector3.new(o[3], o[2], o[1])
    p.Material = 'SmoothPlastic'
    p.Anchored = true
    p.BackSurface = "SmoothNoOutlines"
    p.BottomSurface = "SmoothNoOutlines"
    p.FrontSurface = "SmoothNoOutlines"
    p.LeftSurface = "SmoothNoOutlines"
    p.RightSurface = "SmoothNoOutlines"
    p.TopSurface = "SmoothNoOutlines"
	o[3] = o[3] - 1	
	if o[3]%w == 0 then
		o[3] = o[3] + w
		o[1] = o[1] - 1
	end
end"""

ScriptModel1 = """<roblox xmlns:xmime="http://www.w3.org/2005/05/xmlmime" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.roblox.com/roblox.xsd" version="4">
	<External>null</External>
	<External>nil</External>
	<Item class="Script" referent="RBXFF79737625514507B7790B810CBEAD01">
		<Properties>
			<bool name="Disabled">false</bool>
			<Content name="LinkedSource"><null></null></Content>
			<string name="Name">Script</string>
			<ProtectedString name="Source"><![CDATA["""
#Insert script
ScriptModel2 = """]]></ProtectedString>
		</Properties>
	</Item>
</roblox>"""

C3PartScript1 = """l = {"""
#Insert color data
C3PartScript2 = """}
local h = """
#Insert width
C3PartScript3 = """
local o = {0, 0, 0} --The origin (bottom-right corner of your image) goes here
for i = #l, 1, -3 do
    p = Instance.new('Part', script)
    p.CanCollide = false
    p.Size = Vector3.new(1, 1, 1)
    p.Position = Vector3.new(o[3], o[2], o[1])
    p.Material = 'SmoothPlastic'
    p.Anchored = true
    p.BackSurface = "SmoothNoOutlines"
    p.BottomSurface = "SmoothNoOutlines"
    p.FrontSurface = "SmoothNoOutlines"
    p.LeftSurface = "SmoothNoOutlines"
    p.RightSurface = "SmoothNoOutlines"
    p.TopSurface = "SmoothNoOutlines"
    p.FormFactor = 'Custom'
    p.Size = Vector3.new(1, 1, 1)
    m = Instance.new('SpecialMesh', p)
    m.MeshId = "rbxassetid://9856898"
    m.MeshType = "FileMesh"
    m.Scale = Vector3.new(2, 2, 2)
    m.TextureId = "rbxassetid://1361097"
    m.VertexColor = Vector3.new((l[i-2])/255, (l[i-1])/255, (l[i])/255)
    o[3] = o[3] - 1	
    if o[3]%h == 0 then
            o[3] = o[3] + h
            o[1] = o[1] - 1
    end
end"""

BBGBCFrameScript1 = """l = {"""
#Insert color data
BBGBCFrameScript2 = """}
local w = """
#Insert width
BBGBCFrameScript3 = """
local o = {0, 0}
a = Instance.new('BillboardGui', game.Workspace)
a.AlwaysOnTop = true
a.Size = UDim2.new(0, """
#Insert w
BBGBCFrameScript4 = """, 0, """
#Insert h
BBGBCFrameScript5 = """)
for i = 1, #l, 1 do
		f = Instance.new('Frame', a)
		f.BorderSizePixel = 0
		f.BackgroundColor3 = BrickColor.new(l[i]).Color
		f.Size = UDim2.new(0, 1, 0, 1)		
		f.Position = UDim2.new(0, o[1], 0, o[2])
		o[1] = o[1] + 1	
		if o[1]%w == 0 then
			o[1] = o[1] - w
			o[2] = o[2] + 1
		end
end""" #Fix this, as it transfers the last column of pixels on the right to the first line on the left

BBGC3FrameScript1 = """l = {"""
#Insert color data
BBGC3FrameScript2 = """}
local w = """
#Insert width
BBGC3FrameScript3 = """
local o = {0, 0}
a = Instance.new('BillboardGui', game.Workspace)
a.AlwaysOnTop = true
a.Size = UDim2.new(0, """
#Insert w
BBGC3FrameScript4 = """, 0, """
#Insert h
BBGC3FrameScript5 = """)
for i = 1, #l, 3 do
    f = Instance.new('Frame', a)
    f.BorderSizePixel = 0
    f.BackgroundColor3 = Color3.new(l[i]/255, l[i+1]/255, l[i+2]/255)
    f.Size = UDim2.new(0, 1, 0, 1)
    f.Position = UDim2.new(0, o[1], 0, o[2])
    o[1] = o[1] + 1
    if o[1]%w == 0 then
            o[1] = o[1] - w
            o[2] = o[2] + 1
    end
end"""

SGC3FrameScript1 = """l = {"""
#Insert color data
SGC3FrameScript2 = """}
local w = """
#Insert width
SGC3FrameScript3 = """
local o = {0, 0}
a = Instance.new('SurfaceGui', game.Workspace)
a.CanvasSize = Vector2.new("""
#Insert w
SGC3FrameScript4 = ","
#Insert h
SGC3FrameScript5 = """)
for i = 1, #l, 3 do
    f = Instance.new('Frame', a)
    f.BorderSizePixel = 0
    f.BackgroundColor3 = Color3.new(l[i]/255, l[i+1]/255, l[i+2]/255)
    f.Size = UDim2.new(0, 1, 0, 1)
    f.Position = UDim2.new(0, o[1], 0, o[2])
    o[1] = o[1] + 1
    if o[1]%w == 0 then
            o[1] = o[1] - w
            o[2] = o[2] + 1
    end
end"""

SC3FrameScript1 = """l = {"""
#Insert color data
SC3FrameScript2 = """}
local w = """
#Insert width
SC3FrameScript3 = """
local o = {0, 0}
a = Instance.new('ScreenGui', game.Workspace)
for i = 1, #l, 3 do
    f = Instance.new('Frame', a)
    f.BorderSizePixel = 0
    f.BackgroundColor3 = Color3.new(l[i]/255, l[i+1]/255, l[i+2]/255)
    f.Size = UDim2.new(0, 1, 0, 1)
    f.Position = UDim2.new(0, o[1], 0, o[2])
    o[1] = o[1] + 1
    if o[1]%w == 0 then
            o[1] = o[1] - w
            o[2] = o[2] + 1
    end
end"""

SGBCFrameScript1 = """l = {"""
#Insert color data
SGBCFrameScript2 = """}
local w = """
#Insert width
SGBCFrameScript3 = """
local o = {0, 0}
a = Instance.new('SurfaceGui', game.Workspace)
a.CanvasSize = Vector2.new("""
#Insert w
SGBCFrameScript4 = ","
#Insert h
SGBCFrameScript5 = """)
for i = 1, #l, 1 do
		f = Instance.new('Frame', a)
		f.BorderSizePixel = 0
		f.BackgroundColor3 = BrickColor.new(l[i]).Color
		f.Size = UDim2.new(0, 1, 0, 1)		
		f.Position = UDim2.new(0, o[1], 0, o[2])
		o[1] = o[1] + 1	
		if o[1]%w == 0 then
			o[1] = o[1] - w
			o[2] = o[2] + 1
		end
end"""

SBCFrameScript1 = """l = {"""
#Insert color data
SBCFrameScript2 = """}
local w = """
#Insert width
SBCFrameScript3 = """
local o = {0, 0}
a = Instance.new('ScreenGui', game.Workspace)
for i = 1, #l, 1 do
		f = Instance.new('Frame', a)
		f.BorderSizePixel = 0
		f.BackgroundColor3 = BrickColor.new(l[i]).Color
		f.Size = UDim2.new(0, 1, 0, 1)		
		f.Position = UDim2.new(0, o[1], 0, o[2])
		o[1] = o[1] + 1	
		if o[1]%w == 0 then
			o[1] = o[1] - w
			o[2] = o[2] + 1
		end
end"""

def clear(f):
    c = open(f,'w')
    c.write('')
    c.close()

def distance(c1, c2):
    (r1,g1,b1) = c1
    (r2,g2,b2) = c2
    return math.sqrt((r1 - r2)**2 + (g1 - g2) ** 2 + (b1 - b2) **2)

colors = {(27,42,53):26, (242,243,243):1, (163,162,165):194, (215,197,154):5, (232,186,200):9, (128,187,219):11, (204,142,105):18, (196,40,28):21, (13,105,172):23, (245,205,48):24, (40,127,71):28, (161,196,140):29, (75,151,75):37, (160,95,53):38, (180,210,228):45, (218,134,122):101, (110,153,202):102, (107,50,124):104, (226,155,64):105, (218,133,65):106, (0,143,156):107, (164,189,71):119, (234,184,146):125, (116,134,157):135, (39,70,45):141, (120,144,130):151, (149,121,119):153, (105,64,40):192, (163,162,165):194, (99,95,98):199, (229,228,223):208, (124,92,70):217, (253,234,141):226, (80,109,84):301, (91,93,105):302, (0,16,176):303, (44,101,29):304, (82,124,174):305, (51,88,130):306, (16,42,220):307, (61,21,133):308, (52,142,64):309, (91,154,76):310, (159,161,172):311, (89,34,89):312, (31,128,29):313, (159,173,192):314, (9,137,207):315, (123,0,123):316, (124,156,107):317, (138,171,133):318, (185,196,177):319, (202,203,209):320, (167,94,155):321, (123,47,123):322, (148,190,129):323, (168,189,153):324, (223,223,222):325, (151,0,0):327, (177,229,166):328, (152,194,219):329, (255,152,220):330, (255,89,89):331, (117,0,0):332, (239,184,56):333, (248,217,109):334, (231,231,236):335, (199,212,228):336, (255,148,148):337, (190,104,98):338, (86,36,36):339, (241,231,199):340, (254,243,187):341, (224,178,208):342, (212,144,189):343, (150,85,85):344, (116,71,71):345, (211,190,150):346, (226,220,188):347, (237,234,234):348, (233,218,218):349, (136,62,62):350, (188,155,93):351, (199,172,120):352, (202,191,163):353, (187,179,178):354, (108,88,75):355, (160,132,79):356, (149,137,136):357, (171,168,158):358, (175,148,131):359, (150,103,102):360, (86,66,54):361, (126,104,63):362, (105,102,92):363, (90,76,66):364, (106,57,9):365, (248,248,248):1001, (205,205,205):1002, (17,17,17):1003, (255,0,0):1004, (213,115,61):1005, (180,128,255):1006, (163,75,75):1007, (193,190,66):1008, (255,255,0):1009, (0,0,255):1010, (0,32,96):1011, (33,84,185):1012, (4,175,236):1013, (170,85,0):1014, (170,0,170):1015, (255,102,204):1016, (255,175,0):1017, (18,238,212):1018, (0,255,255):1019, (0,255,0):1020, (58,125,21):1021, (127,142,100):1022, (140,91,159):1023, (175,221,255):1024, (255,201,201):1025, (177,167,255):1026, (159,243,233):1027, (204,255,204):1028, (255,255,204):1029, (255,204,153):1030, (98,37,209):1031, (255,0,191):1032}

outputformat = int(raw_input('Output Format:\n1) Roblox Model (.rbxmx)\n2) Roblox Script (.lua)\n3) Roblox Script (.rbxmx)\n'))
outputtype = int(raw_input('Output Type:\n1) Bricks\n2) BillboardGui\n3) ScreenGui\n4) SurfaceGui\n'))
if outputformat == 1:
    if outputtype == 1:    
        outputcolor = int(raw_input('Output Color:\n1) BrickColor (Less lag, less quality, smaller file size)\n2) Color3 (More lag, more quality, larger file size)\n'))
    elif outputtype == 2 or outputtype == 3 or outputtype == 4:
        outputcolor = int(raw_input('Output Color:\n1) BrickColor (Same lag, less quality, same file size)\n2) Color3 (Same lag, more quality, same file size)\n'))
elif outputformat == 2 or outputformat == 3:
    if outputtype == 1:
        outputcolor = int(raw_input('Output Color:\n1) BrickColor (Less lag, less quality, smaller file size)\n2) Color3 (More lag, more quality, larger file size)\n'))
    elif outputtype == 2 or outputtype == 3 or outputtype == 4:
        outputcolor = int(raw_input('Output Color:\n1) BrickColor (Same lag, less quality, smaller file size)\n2) Color3 (Same lag, more quality, larger file size)\n'))


f = raw_input('Image:\n')
im = Image.open(f)
w, h = im.size
pixels = w * h
pixel = 0
x, y = 0, 0
z = 0

if outputformat == 1:
    clear(f + '.rbxmx')
    rbxmx = open(f + '.rbxmx', 'a')

    if outputtype == 1:
        rbxmx.write(Model1)
    elif outputtype == 2:
        rbxmx.write(BillboardGui1 + str(w) + BillboardGui2 + str(h) + BillboardGui3)
    elif outputtype == 3:
        rbxmx.write(ScreenGui1)
    elif outputtype == 4:
        rbxmx.write(SurfaceGui1 + str(w) + SurfaceGui2 + str(h) + SurfaceGui3)
elif outputformat == 2:
    clear(f + '.lua')
    lua = open(f + '.lua', 'a')
    if outputtype == 1:
        if outputcolor == 1:
            lua.write(BCPartScript1)
        elif outputcolor == 2:
            lua.write(C3PartScript1)
    elif outputtype == 2:
        if outputcolor == 1:
            lua.write(BBGBCFrameScript1)
        elif outputcolor == 2:
            lua.write(BBGC3FrameScript1)
    elif outputtype == 3:
        if outputcolor == 1:
            lua.write(SBCFrameScript1)
        elif outputcolor == 2:
            lua.write(SC3FrameScript1)
    elif outputtype == 4:
        if outputcolor == 1:
            lua.write(SGBCFrameScript1)
        elif outputcolor == 2:
            lua.write(SGC3FrameScript1)
elif outputformat == 3:
    clear(f + '.rbxmx')
    rbxmx = open(f + '.rbxmx', 'a')

    rbxmx.write(ScriptModel1)
    
    if outputtype == 1:
        if outputcolor == 1:
            rbxmx.write(BCPartScript1)
        elif outputcolor == 2:
            rbxmx.write(C3PartScript1)
    elif outputtype == 2:
        if outputcolor == 1:
            rbxmx.write(BBGBCFrameScript1)
        elif outputcolor == 2:
            rbxmx.write(BBGC3FrameScript1)
    elif outputtype == 3:
        if outputcolor == 1:
            rbxmx.write(SBCFrameScript1)
        elif outputcolor == 2:
            rbxmx.write(SC3FrameScript1)
    elif outputtype == 4:
        if outputcolor == 1:
            rbxmx.write(SGBCFrameScript1)
        elif outputcolor == 2:
            rbxmx.write(SGC3FrameScript1)

while y != h:
    
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((x, y))

    if outputformat == 1:
        if outputtype == 1:
            if outputcolor == 1:
                closest_colors = sorted(colors, key=lambda color: distance(color, (r, g, b)))
                closest_color = closest_colors[0]
                color_int = colors[closest_color]

                rbxmx.write(Part1 + str(color_int) + Part2 + str(x) + Part3 + str(z) + Part4 + str(y) + Part5 + Part6) #Y/Z switched because Roblox's 3D engine uses Y for the vertical axis
            elif outputcolor == 2:
                rbxmx.write(Part1 + '1' + Part2 + str(x) + Part3 + str(z) + Part4 + str(y) + Part5 + Mesh1 + str(r/255.0) + Mesh2 + str(g/255.0) + Mesh3 + str(b/255.0) + Mesh4 + Part6)
        elif outputtype == 2 or outputtype == 3 or outputtype == 4:
            if outputcolor == 1 or outputcolor == 2: #Fix this to include BrickColor frames
                bc3 = str(int('11111111' + format(r,'08b') + format(g,'08b') + format(b,'08b'),2))
                rbxmx.write(Frame1 + bc3 + Frame2 + str(x) + Frame3 + str(y) + Frame4)

    elif outputformat == 2:
        if outputtype == 1:
            if outputcolor == 1:
                closest_colors = sorted(colors, key=lambda color: distance(color, (r, g, b)))
                closest_color = closest_colors[0]
                color_int = colors[closest_color]

                if pixel == pixels-h: #This is so it doesn't end the JSON with a comma
                    #Figure out how to make this not subtract height, as it might cause loss of pixels
                    lua.write(str(color_int))
                else:
                    lua.write(str(color_int) + ',')
            elif outputcolor == 2:
                if pixel == pixels-h:
                    lua.write(str(r) + ',' + str(g) + ',' + str(b))
                else:
                    lua.write(str(r) + ',' + str(g) + ',' + str(b) + ',')
        elif outputtype == 2 or outputtype == 3 or outputtype == 4:
            if outputcolor == 1:
                closest_colors = sorted(colors, key=lambda color: distance(color, (r, g, b)))
                closest_color = closest_colors[0]
                color_int = colors[closest_color]

                if pixel == pixels-h:
                    lua.write(str(color_int))
                else:
                    lua.write(str(color_int) + ',')
            elif outputcolor == 2:
                if pixels == pixels-h:
                    lua.write(str(r) + ',' + str(g) + ',' + str(b))
                else:
                    lua.write(str(r) + ',' + str(g) + ',' + str(b) + ',')

    elif outputformat == 3: #First finish outputformat 2, then copy and paste it here, but replace .lua with .rbxmx
        if outputtype == 1:
            if outputcolor == 1:
                closest_colors = sorted(colors, key=lambda color: distance(color, (r, g, b)))
                closest_color = closest_colors[0]
                color_int = colors[closest_color]

                if pixel == pixels-h:
                    rbxmx.write(str(color_int))
                else:
                    rbxmx.write(str(color_int) + ',')
            elif outputcolor == 2:
                if pixel == pixels-h:
                    rbxmx.write(str(r) + ',' + str(g) + ',' + str(b))
                else:
                    rbxmx.write(str(r) + ',' + str(g) + ',' + str(b) + ',')
        elif outputtype == 2 or outputtype == 3 or outputtype == 4:
            if outputcolor == 1:
                closest_colors = sorted(colors, key=lambda color: distance(color, (r, g, b)))
                closest_color = closest_colors[0]
                color_int = colors[closest_color]

                if pixel == pixels-h:
                    rbxmx.write(str(color_int))
                else:
                    rbxmx.write(str(color_int) + ',')
            elif outputcolor == 2:
                if pixel == pixels-h:
                    rbxmx.write(str(r) + ',' + str(g) + ',' + str(b))
                else:
                    rbxmx.write(str(r) + ',' + str(g) + ',' + str(b) + ',')

    x += 1
    if x >= w:
        print "Processing Row ", y
        x = 1
        y += 1
    pixel += 1

if outputformat == 1: #Fix, as most of these format1's are the same string
    if outputtype == 1:
        rbxmx.write(Model2)
    elif outputtype == 2:
        rbxmx.write(BillboardGui4)
    elif outputtype == 3:
        rbxmx.write(ScreenGui2)
    elif outputtype == 4:
        rbxmx.write(SurfaceGui4)
    if outputtype == 2 or outputtype == 3 or outputtype == 4:#Delete this if statement once implemented
        if outputcolor == 1:
            print "BrickColor frames not yet supported; Exported as Color3 instead."
    rbxmx.write(ScriptModel2)
    rbxmx.close()
    
elif outputformat == 2:
    if outputtype == 1:
        if outputcolor == 1:
            lua.write(BCPartScript2 + str(w-1) + BCPartScript3) #Fix that possible loss of pixels
        elif outputcolor == 2:
            lua.write(C3PartScript2 + str(w-1) + C3PartScript3)
    elif outputtype == 2:
        if outputcolor == 1:
            lua.write(BBGBCFrameScript2 + str(w-1) + BBGBCFrameScript3 + str(w) + BBGBCFrameScript4 + str(h) + BBGBCFrameScript5) #Fix that loss of pixels
        elif outputcolor == 2:
            lua.write(BBGC3FrameScript2 + str(w-1) + BBGC3FrameScript3 + str(w) + BBGC3FrameScript4 + str(h) + BBGC3FrameScript5)
    elif outputtype == 3:
        if outputcolor == 1:
            lua.write(SBCFrameScript2 + str(w-1) + SBCFrameScript3)
        elif outputcolor == 2:
            lua.write(SC3FrameScript2 + str(w-1) + SC3FrameScript3)
    elif outputtype == 4:
        if outputcolor == 1:
            lua.write(SGBCFrameScript2 + str(w-1) + SGBCFrameScript3 + str(w) + SGBCFrameScript4 + str(h) + SGBCFrameScript5)
        elif outputcolor == 2:
            lua.write(SGC3FrameScript2 + str(w-1) + SGC3FrameScript3 + str(w) + SGC3FrameScript4 + str(h) + SGC3FrameScript5)
    lua.close()

elif outputformat == 3:
    if outputtype == 1:
        if outputcolor == 1:
            rbxmx.write(BCPartScript2 + str(w-1) + BCPartScript3)
        elif outputcolor == 2:
            rbxmx.write(C3PartScript2 + str(w-1) + C3PartScript3)
    elif outputtype == 2:
        if outputcolor == 1:
            rbxmx.write(BBGBCFrameScript2 + str(w-1) + BBGBCFrameScript3 + str(w) + BBGBCFrameScript4 + str(h) + BBGBCFrameScript5)
        elif outputcolor == 2:
            rbxmx.write(BBGC3FrameScript2 + str(w-1) + BBGC3FrameScript3 + str(w) + BBGC3FrameScript4 + str(h) + BBGC3FrameScript5)
    elif outputtype == 3:
        if outputcolor == 1:
            rbxmx.write(SBCFrameScript2 + str(w-1) + SBCFrameScript3)
        elif outputcolor == 2:
            rbxmx.write(SC3FrameScript2 + str(w-1) + SC3FrameScript3)
    elif outputtype == 4:
        if outputcolor == 1:
            rbxmx.write(SGBCFrameScript2 + str(w-1) + SGBCFrameScript3 + str(w) + SGBCFrameScript4 + str(h) + SGBCFrameScript5)
        elif outputcolor == 2:
            rbxmx.write(SGC3FrameScript2 + str(w-1) + SGC3FrameScript3 + str(w) + SGC3FrameScript4 + str(h) + SGC3FrameScript5)
    rbxmx.write(ScriptModel2)
    rbxmx.close()
