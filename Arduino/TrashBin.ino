#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"

// Device id
const int TRASHBIN_ID = 1;

// Hardware configuration
RF24 radio(9, 10);

// Radio pipe addresses for the 2 nodes to communicate.
const uint64_t pipes[2] = { 0xF0F0F0F0E1, 0xF0F0F0F0D2 };

const int MAX_PAYLOAD_SIZE = 32;
char payload[MAX_PAYLOAD_SIZE + 1];

int byteArrayToInt(char* arr, int len)
{
  int value = 0;
  for (int i = 0; i < len; i++)
  {
    value = value * 10 + (int)(arr[i] - 48);
  }
  return value;
}

int byteToInt(char data)
{
  return (int)(data - 48);
}

void setup(void)
{
  Serial.begin(115200);

  Serial.println("Start:");

  radio.begin();

  radio.enableDynamicPayloads();

  radio.setRetries(5, 15);

  radio.openWritingPipe(pipes[1]);
  radio.openReadingPipe(1, pipes[0]);

  radio.startListening();
}

void loop(void)
{
  if ( radio.available() )
  {
    uint8_t len = radio.getDynamicPayloadSize();

    if (!len) {
      return;
    }

    radio.read(payload, len);

    if (byteToInt(payload[0]) == TRASHBIN_ID)
    {
      if ()
    }
  }
}