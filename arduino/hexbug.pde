/*
  HexBug Network Control

  Controls a HexBug InchWorm - http://hexbug.com/inchworm

  The Circut:
  * Forward switch connected to digital pin 10
  * Reverse switch connected to digital pin 11
  * Right switch connected to digital pin 12
  * Left switch connected to digital pin 13

  Serial Communication:
  * 'f': Begins forward movement
  * 'r': Begins reverse movement
  * 'R': Begins a spin to the right
  * 'l': Begins a spin to the left
  * 's': Stops forward/reverse movement
  * 'S': Stops spin
  * 'k': Stops all movement

  Created October 30th 2009
  By Ben Morris - Ben@bnmrrs.com
  http://github.com/bnmrrs/hexbugnc

*/


// Define the avaliable serial commands
#define MOVE_FORWARD 'f'
#define MOVE_REVERSE 'r'
#define SPIN_RIGHT 'R'
#define SPIN_LEFT 'l'
#define STOP_MOVEMENT 's'
#define STOP_SPIN 'S'
#define STOP_ALL 'k'

// Set up the pins we'll use
int forwardPin = 10;
int reversePin = 11;
int rightPin = 12;
int leftPin = 13;

/*
  Environment initialization
*/
void setup()
{
  // Initialize the digital pins as input to stop all movement
  pinMode(forwardPin, INPUT);
  pinMode(reversePin, INPUT);
  pinMode(rightPin, INPUT);
  pinMode(leftPin, INPUT);

  // Initialize all pins to LOW.  Totally kills the pin
  digitalWrite(forwardPin, LOW);
  digitalWrite(reversePin, LOW);
  digitalWrite(rightPin, LOW);
  digitalWrite(leftPin, LOW);

  // Initialize the serial library
  Serial.begin(9600);
}


/*
  Main loop for Arduino
*/
void loop()
{
  // Make sure we actually have a serial connection avaliable
  if (Serial.available() > 0) {

    // Read input from the USB serial connection
    int inByte = Serial.read();

    switch (inByte) {

      case MOVE_FORWARD:
        move(forwardPin, reversePin);
        break;

      case MOVE_REVERSE:
        move(reversePin, forwardPin);
        break;

      case SPIN_RIGHT:
        move(rightPin, leftPin);
        break;

      case SPIN_LEFT:
        move(leftPin, rightPin);
        break;

      case STOP_MOVEMENT:
        stop(forwardPin);
        stop(reversePin);
        break;

      case STOP_SPIN:
        stop(leftPin);
        stop(rightPin);
        break;

      case ALL_STOP:
      default:
        stop(forwardPin);
        stop(reversePin);
        stop(leftPin);
        stop(rightPin);
    }
  }
}

/* 
  Starts forward/reverse movement or a spin

  Switches both pins to OUTPUT
  Connects 5v to highPin
  Connects gnd to lowPin
*/
void move(int highPin, int lowPin)
{
  // Set both pins as OUTPUT to prepare for writing
  pinMode(highPin, OUTPUT);
  pinMode(lowPin, OUTPUT);

  digitalWrite(highPin, HIGH); // Connect 5v to the highPin
  digitalWrite(lowPin, LOW); // Connect gnd to the lowPin
}

/*
  Cuts all current to the specified pin
*/
void stop(int pin)
{
  pinMode(pin, INPUT); // Disconnect current by switching pin to INPUT
  digitalWrite(pin, LOW); // Kill the pin
}
