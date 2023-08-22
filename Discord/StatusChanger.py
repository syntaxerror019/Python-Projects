### TYPING DISCORD STATUS SCRIPT
import requests, json, time
import os
token = "Your Discord Token HERE"
print("Running")
class main:
    

    def __init__(self, token):
        self.token = token
       
        while True:
            try:
                self.set_status("FPV Pilot.", "✈")

                self.set_status("Active Dev.", "👨‍💻")

                

                self.set_status("bots 4 life!", "💣")

                self.set_status("Recycle More.", "♻️")

                self.set_status("w cats","🐈")

                #self.set_status("Stop Littering.","🚯")

                self.set_status("cracked Solderer?","⚡")

                #self.set_status("MIT","🎓")
                self.set_status("Bot Owner","🤖")
                #self.set_status("100% CPU","🔥")
                #self.set_status("ESP8266 Better","✅")
                self.set_status("taskkill /f brain.exe","💀")
                #self.set_status("plz dont ban me!","🙏")
                self.set_status("Slow Global Warming!","🌎")
                #self.set_status("🥒🥒🥒🥒🥒","🥒")
            except:
                print("error connnecting. trying again!")
                time.sleep(3)
          
          
        
 
    
    def set_status(self, text, emoji):
        # Print text character by character
        print("Operational!")
        for i in range(1, len(text) + 1):
            #print(text[:i])
            requests.patch("https://discord.com/api/v9/users/@me/settings", headers={"authorization": self.token,"content-type": "application/json"}, data=json.dumps({"custom_status":{"text":text[:i],"emoji_name":emoji}}))
            

        # Simulate blinking cursor effect
        for _ in range(4):
            #print(text + "|")
            requests.patch("https://discord.com/api/v9/users/@me/settings", headers={"authorization": self.token,"content-type": "application/json"}, data=json.dumps({"custom_status":{"text":text + " |","emoji_name":emoji}}))
            time.sleep(0.16)
            #print(text)
            requests.patch("https://discord.com/api/v9/users/@me/settings", headers={"authorization": self.token,"content-type": "application/json"}, data=json.dumps({"custom_status":{"text":text,"emoji_name":emoji}}))
            time.sleep(0.16)

        # Print text in reverse
        for i in range(len(text), 0, -1):
            #print(text[:i])
            requests.patch("https://discord.com/api/v9/users/@me/settings", headers={"authorization": self.token,"content-type": "application/json"}, data=json.dumps({"custom_status":{"text":text[:i],"emoji_name":emoji}}))
            

        

if __name__ == "__main__":
    
    if requests.patch("https://discord.com/api/v9/users/@me", headers={"authorization": token,"content-type": "application/json"}).status_code == 400:
        main(token)
    else:
        print("Failed to connect to token")
        exit()

