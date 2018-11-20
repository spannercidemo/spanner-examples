#include <stdio.h>
#include <string.h>

// Constants
const size_t READ_BUF_SIZE = 64;

// Forward declarations
void processBuffer();

// Global variables
char readBuf[READ_BUF_SIZE];
size_t readBufOffset = 0;

void setup() {
  // Serial TX (1) is connected to Photon RX
  // Serial RX (0) is connected to Photon TX
  // Ardiuno GND is connected to Photon GND
  Serial.begin(9600);
  
  //while(!Serial) delay(500);
  
  // Initiate handshake
  Serial.write("Hello Testboard\n");
}

void loop() {
  // Read data from serial
  while(Serial.available()) {
    if (readBufOffset < READ_BUF_SIZE) {
      char c = Serial.read();
      if (c != '\n') {
        // Add character to buffer
        readBuf[readBufOffset++] = c;
      }
      else {
        // End of line character found, process line
        readBuf[readBufOffset] = 0;
        processBuffer();
        readBufOffset = 0;
      }
    }
    else {
      readBufOffset = 0;
    }
  }

}

void processBuffer() {
  // handshake is completed
  if (strcmp(readBuf, "Hello device\n") == 0) {
    Serial.print('a', DEC);
  }
}