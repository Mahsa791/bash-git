from twython import TwythonStreamer
c_k="hd8QIbEVOXYHxUnieWegxEauc"
a_t="977382146024329219-44nA8ClDeMZFxtI8P5CRuTvnJiX0GIR"
c_s="2pCmla5wd8LLW9HgHYWGu2qKlLTmZNhgG9em904jGIpAj3cJ9A"
a_s="AR84zZGASdBGvLirNc0dN09MRL8FOljkqc6dW1ypf1AO2"

class MyStreamer(TwythonStreamer):
	def on_success(self,data):
           nb=0
	   if 'text' in data:
		nb=nb+1
	    if count >= 3:
                print "found it!"
            else:
                 nb=0
                print "NOT found!"           
                        

stream=MyStreamer(c_k,c_s,a_t,a_s)
stream.statuses.filter(track="Ian G. Harris_temte")
