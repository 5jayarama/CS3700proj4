Project 4: Reliable Transport Protocol

4 classes:

3700recv
This class represents a receiver within a TCP data exchange, acting as a client. It receives data packets sent over UDP from the sender class and performs the necessary actions to handle packet reception, validation, and acknowledgement.
The main method in this class is the run method which continuously looks for and processes incoming data packets

3700send
This class represents a sender within a TCP data exchange, acting as a server. It sends data packets over UDP to the receiver class and performs the necessary actions to handle detecting packet loss and retransmission, TCP congestion control, and send_buffer management.
The main method here is also the run method.

recv_buffer.py
This class represents a memory buffer for received data. It manages received data packets, ensures proper packet ordering, and flushes out invalid packets

send_buffer.py
This class represents the buffer and window management system for sent data in the TCP exchange system. It manages elements of packet sending, acknowledgements, and adjusts window size based on the TCP congestion protocol. 

Challenges faced:
I spent a lot of time on the level 4 tests, especially due to some problems while testing on the linux environment. The features I had to implement for level 4 tests were pretty complicated as well, such as managing the expiry and retransmitting the packets. I had to meticulously debug this program to fit the logic of the expiry calculations, and I ended up using datetime instead of time because I found a less complicated way to make the functions under that logic. There were so many calculations, and I had to introduce and manage many different varaibles to the init of 3700send in order to make the level 4 tests pass.

Level 8 tests were very difficult as well. I searched online and in the class slides for ways to improve performance. Although I heard that 1, 2, and 4 were the best window sizes (from google search), most of them caused some bugs, so I ended up using 5 as my window size. I used the standard formulas for additive increase and multiplicative decrease and I used hashlib for efficiently going through the messages. Eventually, after tweaking the code to improve performance in the RTT recalculation function, I got a surprisingly good performance runtime.

Testing:
I used the config files to test my code in the khoury linux environment. I would write the code and then run the test, and debug until I got the success message. I mainly used the prints and logs to debug. I did find this program much harder to debug than previous programs though, because there was less comprehensive instructions for this project.

