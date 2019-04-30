// Example 6 - Receiving binary data

const byte numBytes = 84;
byte receivedBytes[numBytes];
byte numReceived = 0;
byte msg[84];    
long val;
int low = 3;
int high =8;
int sensorval;
int pin_val[] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
byte Pins[] = {A0,A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19,A20,A21,A22};
int test[]={0,0,0,0,0,600};
boolean newData = false;


void setup() {
    Serial2.begin(9600);
    Serial.println("<Arduino is ready>");
}

void loop() {
    sensorval =checksensor(Pins,pin_val);
    //tobyte();
    sendbytedata();
    recvBytesWithStartEndMarkers();
    showNewData();
}
/*
 void tobyte()
  {
   // Serial.println("converting");
    for(int j=0;j<3; j++)
    {
      for(int i = 0; i < 8; i++)  
      {
     
            msg[j] = msg[j] | (pin_val[i+(j*8)] << i+(j*8));
         
         // Serial.print("the msg");
          //Serial.println(j);
          //Serial.println(msg[j]);
      }
    }
    Serial.println(msg[0]);
    Serial.println(msg[1]);
    Serial.println(msg[2]);

  }
 */
int checksensor(byte pins[],int pin_val[])
{
//int pin_val[] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
  //Serial.println("checking");
  int result =0;
  int val =0;
  int checking =0;
 //Serial.println("lol");
 for (int i = 0; i <= 22; i++) 
 {
     val=analogRead(pins[i]);
     val =val/100;
     if(val<=low)
      {
        checking=1;
      }

      else if(val>=high)
      {
        checking=2;
        
      }
      else
      {
        checking=1;   
      }
   //Serial.println(checking);
   result+=pow(checking*2, (i));
   msg[i]=checking;
  }
  //Serial.println(result);
  return result;
}



void sendbytedata()
{

  //Serial.println("sending");
  byte startMarker = 0xFF;
  byte endMarker = 0xFF;
  int msglen =84;
  /*
  msg[0]=0x31;
  msg[1]=0x32;
  msg[2]=0x33;
  msg[4]=0x34; */
  //Serial.println("start_sending");
  Serial2.write(startMarker);
    
  msg[0]=0x31;
  msg[1]=0x32;
  msg[2]=0x33;
  msg[4]=0x34; 
  for(int i=0;i<msglen;i++)
  {
    if(i>22)
    {
      msg[i]=receivedBytes[i-22];
    }
  
  Serial2.write(msg[i]);
  //Serial.println(msg[i]);
 
  }
   Serial2.write(startMarker);
   
   //Serial.println("stop_sending");
}

void recvBytesWithStartEndMarkers() {
  
    static boolean recvInProgress = false;
    static byte ndx = 0;
    byte startMarker = 0xFF;
    byte endMarker = 0xFF;
    byte rb;
   

    while (Serial2.available() > 0 && newData == false) {
      //Serial.println("recieving");
        rb = Serial2.read();
        Serial.print(rb);
        

        if (recvInProgress == true) {
            if (rb != endMarker) {
                receivedBytes[ndx] = rb;
                ndx++;
                if (ndx >= numBytes) {
                    ndx = numBytes - 1;
                }
            }
            else {
                receivedBytes[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                numReceived = ndx;  // save the number for use when printing
                ndx = 0;
                newData = true;
            }
        }

        else if (rb == startMarker) {
            recvInProgress = true;
        }
    }
}

void showNewData() {
    if (newData == true) {
        Serial.print("This just in (HEX values)... ");
        for (byte n = 0; n < numReceived; n++) {
            Serial.print(receivedBytes[n], DEC);
            Serial.print(' ');
        }
        Serial.println();
        newData = false;
    }
}
