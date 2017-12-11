# -*- coding: utf-8 -*-
#Catatan start 


#Catatan End
import LEO
from LEO.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
import requests,urllib
from gtts import gTTS
from googletrans import Translator
import gscrapper
import time,random,sys,json,codecs,threading,glob,re,shutil,os,subprocess
import tempfile

cl = LEO.LINE()
cl.login(qr=True)
cl.loginResult()


ki=cl
print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" Command!!!
Say 
[Leo help]
Global command:
[Yui join]  Will be fixed soon
[Image] "Image ayam" will be show image of ayam
[Ciduk] set point Read
[Lurking] read point read
[.music] <Judul>
Rules:
-Bot only accept group 10+ members
-Use Wisely
Ver 1.3
"""
helpMessage2=""" 
~~~~~~~~~~~~~~
How to use Command
Leo + Command
Example:
Leo respon
~~~~~~~~~~~~~~
List:
[me]
[invite] Invite Mid
[curl] close link
[ourl] open link
[gurl] Grup link
[join:] join:link grup
[out] out grup
[respon] respon bot
[yt] Search Youtube Video link
[cancel] cancel 
[gn] change grup name
[steal home] Steal cover via mention
[update] Next update concept
[tagall] Mention All member
Found Bug Take A Screenshoot and send to
line://ti/p/~@pyy9899m
Ver 1.3
"""

updateMessage="""
Ver 1.4 Concept
- Translator
- Voice Note music
- Lyric songs
- Instagram Scrapping
- Fix minor bugs
"""
mid = cl.getProfile().mid
Amid= cl.getProfile().mid

Bots=[mid,"ubd173d5694e5781f067c54a79de03e80","u5b3d509c3f01627e413ab63c41e72dcf"]
owner=["u5b3d509c3f01627e413ab63c41e72dcf"]
admin=["u5b3d509c3f01627e413ab63c41e72dcf"]
yui=["ua9f4d5169e584c79d1c2ca06f8f4779c"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":10},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Invite Me to Your Group line://ti/p/~@pyy9899m",
    "lang":"JP",
    "comment":"Invite Me To Your Group  line://ti/p/~@pyy9899m",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"Leonard #2",
    "blacklist":{},
    "wblacklist":False,
    "autoBattle":True,
    "dblacklist":False,
    "protectionOn":True,
    "atjointicket":False
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    m.es = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

def restart_program():
    """Restarts the current program, with file objects and descriptors
       cleanup
    """
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def findLyric(to,song):
    params = {'songname':song}
    r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?'+urllib.urlencode(params))
    data = r.text
    data = json.loads(data)
    for song in data:
        cl.sendText(to,"Lyrics Of " + song[0] + ":\n\n"+ song[5])

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib.request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"


#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content


#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 19:
                if admin or yui or owner in op.param3:
                  if op.param3 in op.param1:
                    if op.param2 in Bots or admin or yui or owner:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    korban = cl.getContact(op.param3)
                    cl.inviteIntoGroup(msg.to,korban)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 2:
              if '/battle' in msg.text:
                if wait['autoBattle'] == True:
                   time.sleep(5)
                   cl.sendText(msg.to,'/join')
                else:
                    pass
        if op.type == 25:
            msg = op.message
            if msg.toType == 2:
              if 'Battle off' in msg.text:
                if wait['autoBattle'] == False:
                    cl.sendText(msg.to,"Sudah Mati")
                else:
                    wait['autoBattle'] = False
                    cl.sendText(msg.to,'Dimatikan')
            if 'Battle on' in msg.text:
                if wait['autoBattle'] == True:
                    cl.sendText(msg.to,"Sudah Hidup")
                else:
                    wait['autoBattle'] = True
                    cl.sendText(msg.to,'Dihidupkan')





        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                         wait2['ROM'][op.param1][op.param2] = "・" + Name
                else:
                     cl.sendText
            except:
                pass

		
        if op.type == 59:
            print op

    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] 
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
