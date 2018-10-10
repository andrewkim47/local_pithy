from pithy import *
import pandas as pd
# fil = 'files/logfile.txt'

data = pd.read_csv(fil,skiprows=1,names=['t','a0'])

# print data['t']
plot(data['t']/1000.,data['a0'])
showme()


#Arduino Code


# unsigned long starttime;
# unsigned long t;
# void setup() {
#   pinMode(A0,INPUT);
#   Serial.begin(9600);
#   delay(2000);
#   starttime= millis();

# }

# void loop() {
#   t = millis()-starttime;
#   Serial.print(t); Serial.print(",");
#   Serial.println(A0); 
#   delay(1000);

# }