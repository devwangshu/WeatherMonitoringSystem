//CONVERGENCE //
#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>

// Replace with your network credentials
const char* ssid = "MM";
const char* password = "noaccess";


ESP8266WebServer server(80);  
float tempe;

String page = "";
double data; 
void setup(void){

 pinMode(A0, INPUT);
 
 delay(1000);
 Serial.begin(115200);
 WiFi.begin(ssid, password); //begin WiFi connection3
 Serial.println("");
 IPAddress ip(192,168,1,202);   
 IPAddress gateway(192,168,1,1);   
 IPAddress subnet(255,255,255,0);   
 WiFi.config(ip, gateway, subnet);
 
 // Wait for connection
 while (WiFi.status() != WL_CONNECTED) {
   delay(500);
   Serial.print(".");
 }
 Serial.println("");
 Serial.print("Connected to ");
 Serial.println(ssid);
 Serial.print("IP address: ");
 Serial.println(WiFi.localIP());
 server.on("/", [](){
   page = String(tempe)+","+0.88+","+6.34+","+5.22+","+4.56+","+2.22+","+1.56+","+9.22+","+3.56;
 //  page = String(tempe);
   server.send(200, "text/html", page);
 });
 
 server.begin();
 Serial.println("Web server started!");
}

void loop(void){
 float sensorValue = analogRead(A0);
 float value = 3.22265625*sensorValue;
 tempe = value/10;
 delay(1000);
 server.handleClient();
}


