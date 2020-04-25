import os
try:
   import pyqrcode
except ImportError:
   os.system('pip install pyqrcode &> /dev/null')

from pyqrcode import QRCode 
try:
    import pyshorteners
except ImportError:
	os.system('pip install pyshorteners &> /dev/null')


logo = """
                        Short URL
   ______            __  __  _____  __ 
  / __/ /  ___  ____/ /_/ / / / _ \/ / 
 _\ \/ _ \/ _ \/ __/ __/ /_/ / , _/ /__ By khaz
/___/_//_/\___/_/  \__/\____/_/|_/____/
                                       """

def menu():

  print ("""
[01] Adfly
[02] Bitly
[03] Chilp
[04] Clck
[05] Cutt
[06] Dadg
[07] Gitio
[08] Isgd
[09] Nullpointer
[10] Osdb
[11] Owly
[12] Tinyurl
[13] QRcode Generate

[99] Admin info
[00] Exit\n""")

if __name__=="__main__":
   import os, sys

   stop=False
   while(not stop):
      os.system('clear')
      print (logo)
      menu()
      try:
          pil = str(input("> "))
          print ("")
          if pil == "1":
             url = str(input("[?]URL: "))
             s = pyshorteners.Shortener(api_key='f1875d2c782b48267cfbb1b369cf7f74', user_id='23243451',
                               domain='test.us', group_id=12, type='int')
             print("[!]Short: {}".format(s.adfly.short(url)))

          elif pil == "2":
             url2 = input("[?]URL: ")
             s = pyshorteners.Shortener(api_key='56027c4d584682c8a07ff26dafaec3dd76bd79b7')
             print("[!]Short: "+s.bitly.short(url2))

          elif pil == "3":
             url = str(input("[?]URL: "))
             s = pyshorteners.Shortener()
             print("[!]Short: {}".format(s.chilpit.short(url)))

          elif pil == "4":
              url = str(input("[?]URL: "))
              s = pyshorteners.Shortener()
              print("[!]Short: {}".format(s.clckru.short(url)))

          elif pil == "5":
              url = str(input("[?]URL: "))
              s = pyshorteners.Shortener(api_key='dc5bdb55c54c6ae578f2db663013ae5e143a2')
              print("[!]Short: {}".format(s.cuttly.short(url)))

          elif pil == "6":
             url = str(input("[?]URL: "))
             s = pyshorteners.Shortener()
             print("[!]Short: {}".format(s.dagd.short(url)))

          elif pil == "7":
             url = str(input("[?]URL: "))
             s = pyshorteners.Shortener(code='12345')
             print("[!]Short: {}".format(s.gitio.short(url)))

          elif pil == "8":
             url = str(input("[?]URL: "))
             s = pyshorteners.Shortener()
             print("[!]Short: {}".format(s.isgd.short(url)))

          elif pil == "9":
             url = str(input("[?]URL: "))
             s = pyshorteners.Shortener(domain='https://0x0.st')
             print("[!]Short: {}".format(s.nullpointer.short(url)))

          elif pil == "10":
            url = str(input("[?]URL: "))
            s = pyshorteners.Shortener()
            print("[!]Short: {}".format(s.osdb.short(url)))

          elif pil == "11":
             url = str(input("[?]URL: "))
             s = pyshorteners.Shortener()
             print("[!]Short: {}".format(s.owly.short(url)))

          elif pil == "12":
             url = str(input("[?]URL: "))
             s = pyshorteners.Shortener()
             print("[!]Short: {}".format(s.tinyurl.short(url)))

          elif pil == "13":
             s = str(input("[?]Nama/url/code: "))

             url=pyqrcode.create(s)
             url.png("myqr.png", scale=6)

             print ("[!]File save in : /sdcard/myqr.png")

          elif pil == "99":
             admin = """

Nama  : Khazul yussery shadiq
Whats : +601136956558"""
             print (admin)

          else:
              exit()


          nanya=input("\nShort lagi? (y/n) ")
          if(nanya=="n"):
                  stop=True

      except:
         exit()
