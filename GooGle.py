#!/usr/bin/python3
import socket

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "irc.efnet.org" # Server
channel = "#jcgtBOTSMASH" # Channel
botnick = "GooGle" # Your bots nick
adminname = "jcgter" #Your IRC nickname. On IRC (and most other places) I go by OrderChaos so that’s what I am using for this example.
exitcode = "bye " + botnick

ircsock.connect((server, 6697)) # Here we connect to the server using the port 6667
ircsock.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick + " " + botnick + "\n", "UTF-8")) #We are basically filling out a form with this line and saying to set all the fields to the bot nickname.
ircsock.send(bytes("NICK "+ botnick +"\n", "UTF-8")) # assign the nick to the bot

def joinchan(chan): # join channel(s).
  ircsock.send(bytes("JOIN "+ chan +"\n", "UTF-8")) 
  ircmsg = ""
  while ircmsg.find("End of /NAMES list.") == -1:  
    ircmsg = ircsock.recv(2048).decode("UTF-8")
    ircmsg = ircmsg.strip('\n\r')
    print(ircmsg)
    
def ping(): # respond to server Pings.
  ircsock.send(bytes("PONG :pingis\n", "UTF-8"))
  
def sendmsg(msg, target=channel): # sends messages to the target.
  ircsock.send(bytes("PRIVMSG "+ target +" :"+ msg +"\n", "UTF-8"))
