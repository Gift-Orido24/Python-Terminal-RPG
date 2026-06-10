import json
import time
class Player_data:
      def __init__(self):
          self.plyer_data = self.load()
      def load(self):
          with open("plyr.json","r") as file:
              return json.load(file)
      def save(self):
          with open("plyr.json","w") as file:
              return json.dump(self.plyer_data,file)
      def get(self,data):
          return self.plyer_data.get(data)
      def loading(self):
          count = 0
          while count < 6:
              for n in range(6):
                  for i in [".  ",".. ","..."]:
                      print(f"Loading{i}{n}",end="\r",flush=True)
                      time.sleep(0.2)
                  time.sleep(0.3)
                  count+=1
 
 
              

      