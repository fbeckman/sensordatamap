// Import required libraries
#include "ESP8266WiFi.h"
#include "DHT.h"
#include "SSD1306.h" // alias for `#include "SSD1306Wire.h"`

// WiFi parameters
const char* ssid = "SSID";
const char* password = "PASSWORD";

// Host
const char* host = "dweet.io";

// Things
#define THINGNAMEWH1 "THINGNAMEWH1"
#define THINGNAMEWH2 "THINGNAMEWH2"

// Thing to send to
char* thingname = THINGNAMEWH1;

// Pin
#define DHTPIN D2

// Use DHT22 sensor
#define DHTTYPE DHT22

void setup() {

  // Initialize DHT sensor
  DHT dht(DHTPIN, DHTTYPE);
  delay(10); 
  // Init DHT 
  dht.begin();

  // We start by connecting to a WiFi network
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(450);
  }
  // Use WiFiClient class to create TCP connections
  WiFiClient client;
  const int httpPort = 80;
  if (!client.connect(host, httpPort)) {
    return;
  }
  
  // Reading temperature and humidity
  float h = dht.readHumidity();
  // Read temperature as Celsius
  float t = dht.readTemperature();
  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t)) {
  } else {
    // This will send the request to the server
    client.print(String("GET /dweet/for/") + String(thingname) + "?temperature=" + String(t) + "&humidity=" + String(h) + " HTTP/1.1\r\n" +
                 "Host: " + host + "\r\n" + 
                 "Connection: close\r\n\r\n");
    delay(10);
  }
  // Repeat every 600 seconds
  ESP.deepSleep(600e6);
  delay(100);
}

void loop() {
}

