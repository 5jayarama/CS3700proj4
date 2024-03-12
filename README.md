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
level 4 tests did not pass in the linux environment, so I spent a lot of time researching about how to do it properly and why it would fail. It passed on gradescope though, when I submitted. Level 8 tests were very difficult, since I am not familiar with how to improve performance. I usually just focus on getting my projects to run, and I usually only have to care about time complexity on simpler projects. This project was pretty long and complicated, so I experimented with some different formulas for window size and RTT calculations. Eventually, I landed on window size of 5, because it had good performance and didn't cause too many errors.

Testing:
I used the config files to test my code in the khoury linux environment. I would write the code and then run the test, and debug until I got the success message. I mainly used the prints and logs to debug. I did find this program much harder to debug than previous programs though, because there was less comprehensive instructions for this project.

