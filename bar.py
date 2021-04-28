import sys
import time

class Bar():
    def __init__(self,total : int ,time : bool = False,lenght : int = 100,progress : int = 0,start_char : str = "[",start_middle_char : str = '=',middle_char : str = '=',white_char : str = " ",end_middle_char : str = ">",end_char : str = ']'):

        self.total = total
        self.lenght = lenght
        self.start_char = start_char
        self.start_middle_char = start_middle_char
        self.middle_char = middle_char
        self.end_middle_char = end_middle_char
        self.end_char = end_char
        self.progress = progress
        self.time = time
        self.white_char = white_char
        self.killed = False



    def _s_to_hms(self,s):
        (h, s)=divmod(s, 3600)
        (m, s)=divmod(s, 60)
        return f"{h}h {m}mn {s}s"



    def _delete(self):
        sys.stdout.write("\r"+" "*(self.lenght + 15) + "\r")



    def _loading(self):
        what_to_print = f"{self.start_char}"
        for _ in range( round( (self.progress / self.total)*self.lenght  )):
            what_to_print += f"{self.middle_char}"

        what_to_print += f"{self.end_middle_char}"



        for _ in range( round(self.lenght - (self.progress/self.total)*self.lenght  )):
            what_to_print += " "
        
        what_to_print += f"{self.end_char}"
        return what_to_print



    def kill(self):
        self._delete()
        self.killed = True



    def update(self, message : str = None, time : int = 0):
        if self.killed:
            return False
        
        if self.progress == self.total:
            return False
       
        message = str(message)
        self._delete()

        self.progress += 1

        if self.time:
            if len(message) > 0:
                sys.stdout.write(f"{message}\n"+self._loading()+self._s_to_hms(time))
                sys.stdout.flush()
                return True
            sys.stdout.write(self._loading()+self._s_to_hms(time))
            sys.stdout.flush()
            return True


        if len(message) > 0:
            sys.stdout.write(f"{message}\n"+self._loading())
            sys.stdout.flush()
            return True
        sys.stdout.write(self._loading())
        sys.stdout.flush()
        return True

