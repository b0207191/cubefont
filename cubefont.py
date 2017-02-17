import matplotlib.pyplot as plt 
import matplotlib.patches as patches
import matplotlib

ttynumber=80
width_size=16*80
space_size=4
height_size=16*80

lastx=0
lasty=0
charcount=0

charpix={' ':[0,0,0,0,0,0,0,0,0],
         ',':[0,0,0,0,0,1,0,1,0],
         '.':[0,0,0,0,0,0,0,1,0],
         'a':[0,1,0,1,1,1,1,0,1],
         'b':[1,1,0,1,1,1,1,1,0],
         'c':[1,1,1,1,0,0,1,1,1],
         'd':[1,1,0,1,0,1,1,1,0],
         'e':[1,1,1,1,1,0,1,1,1],            
         'f':[1,1,1,1,1,0,1,0,0],
         'g':[1,1,1,1,0,1,1,1,0],               
         'h':[1,0,1,1,1,1,1,0,1],                   
         'i':[0,1,0,0,1,0,0,1,0],
         'j':[1,1,1,0,1,0,1,1,0],
         'k':[1,0,1,1,1,0,1,0,1],
         'l':[1,0,0,1,0,0,1,1,1],
         'm':[1,1,1,1,1,1,1,0,1],                
         'n':[1,1,1,1,0,1,1,0,1],    
         'o':[1,1,1,1,0,1,1,1,1],                   
         'p':[1,1,1,1,1,1,1,0,0],
         'q':[1,1,1,1,1,1,0,0,1],
         'r':[1,0,1,1,1,0,1,0,0],
         's':[0,1,1,0,1,0,1,1,0],
         't':[1,1,1,0,1,0,0,1,0],     
         'u':[1,0,1,1,0,1,1,1,1],
         'v':[1,0,1,1,0,1,0,1,0],
         'w':[1,0,1,1,1,1,1,1,1],
         'x':[1,0,1,0,1,0,1,0,1],
         'y':[1,0,1,0,1,0,0,1,0],                
         'z':[1,1,0,0,1,0,0,1,1],                                     
        }

'''
'0':[1,1,1,1,1,1,1,1,1],                   
'1':[1,1,1,1,1,1,1,1,1],
'2':[1,1,1,1,1,1,1,1,1],
'3':[1,1,1,1,1,1,1,1,1],
'4':[1,1,1,1,1,1,1,1,1],
'5':[1,1,1,1,1,1,1,1,1],                
'6':[1,1,1,1,1,1,1,1,1],                    
'''    
    
char_offset=[[0,9],[4,9],[8,9],[0,5],[4,5],[8,5],[0,1],[4,1],[8,1]]

def drawchar_pix(x,y,char):
    print 'drawchar_pix:',x,y,char
    global ax
    
    '''
    #print test
    ax.add_patch(
    patches.Rectangle(
        (x, y-12),   # (x,y)
        12,          # width
        12,          # height
    ))
    '''
    
    basex=x
    basey=y-12
    
    if char not in charpix:
        return
    tmppix = charpix[char]
    for i in range(0,9):
        if tmppix[i]==1:
            print 'rect:',basex+char_offset[i][0],basey++char_offset[i][1]
            ax.add_patch(
            patches.Rectangle(
                (basex+char_offset[i][0], basey++char_offset[i][1]),   # (x,y)
                1,          # width
                1,          # height
                color='red'
            ))

            
    return
    

def drawchar(x,y,char):
    global height_size,space_size
    print 'drawchar',x,y,' pix ',16*x,height_size-20*y,char
    drawchar_pix(space_size+16*x,height_size-20*y,char)
    return
    
def putchar(char):
    global lastx,lasty,ttynumber,charcount
    #print 'putchar:',char
    drawchar(lastx,lasty,char)                
    if charcount % ttynumber == ttynumber-1:
        lastx=0
        lasty+=1
    else:
        lastx+=1
        #lasty
    charcount+=1
    return
 
maxdpi=600
#fig = plt.figure(figsize=(16,16))  #1 for 80 pix   
fig = plt.figure(dpi=maxdpi,edgecolor='g')  #1 for 80 pix   
ax = fig.add_subplot(111, aspect='equal')
plt.axis('off')
plt.xlim(xmax=width_size+space_size)
plt.ylim(ymax=height_size)

#ctx = 'abc'    
ctx = 'the quick brown fox jumps over the lazy dog. in view,a humble vaudevillian veteran cast vicariously as both victim and villain by the vicissitudes of fate.this visage,no mere veneer of vanity is a vestige of the vox populi,now vacant,vanished.however,this valorous visitation of a bygone vexation stands vivified and has vowed to vanquish these venal and virulent vermin vanguarding vice and vouchsafing the violently vicious and voracious violation of volition.the only verdict is vengeance,a vendetta held as a votive not in vain,for the value and veracity of such shall one day vindicate the vigilant and the virtuous.verily,this vichyssoise of verbiage veers most verbose. so let me simply add that it s my very good honor to meet you and you may call me v'    
for ch in ctx:    
    putchar(ch)    

ax.set_xticks([])
ax.set_yticks([])


#plt.savefig("test.png",dpi=600)
plt.savefig("test.svg",format="svg",dpi=600) 
#plt.show()
#print plt.xlim()