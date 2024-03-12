from typing import List
import sys

# represents a buffer and window for sent data
class SendBuffer:
    def __init__(self, max_buff):
        self.buffer = []
        self.last_sent = -1
        self.max_buffer_size = max_buff
        self.last_successful_ack = -1
        self.packets_in_transit = 0
        self.received_acks = []

    # log a message in the standard error stream(stderr)
    def log(self, message):
        sys.stderr.write(message + "\n")
        sys.stderr.flush()

    # adds data to the buffer
    def add_data(self, data):
        self.buffer.append(data)

    # gets the data of a particular sequence number
    def get_data_of_seq_num(self, target):
        # finds the data in the buffer and returns it, or returns empty string
        for seq_num, data in enumerate(self.buffer):
            if seq_num == target:
                return data
        return ""

    # returns data that can be sent but has not been acknowledged
    def get_data_to_send(self):
        if self.last_sent >= len(self.buffer):
            return []
        # calculate the last transmissible index based on the space in the buffer
        if self.last_sent == -1:
            last_transmissible_idx = min(self.max_buffer_size - self.packets_in_transit + 1, len(self.buffer))
        else:
            last_transmissible_idx = min(self.last_sent + 1 + (self.max_buffer_size - self.packets_in_transit), len(self.buffer))
        # iterate through the buffer to find data that can be sent
        data_to_send = []
        for i in range(self.last_sent + 1, last_transmissible_idx):
            self.last_sent += 1
            data_to_send.append((self.last_sent, self.buffer[i]))
            self.packets_in_transit += 1
        return data_to_send

    # update the acknowledgement number and process received acknowledgements
    def update_ack(self, ack_num):
        if ack_num == 1 + self.last_successful_ack:
            acks_processed = 0
            self.last_successful_ack = ack_num
            for ack in self.received_acks:
                if ack == self.last_successful_ack + 1:
                    self.last_successful_ack = ack
                    acks_processed += 1
            self.received_acks = self.received_acks[acks_processed:]
        else:
            # store the acknowledgements that are out of order for later processing
            self.received_acks.append(ack_num)
            self.received_acks.sort()
        self.packets_in_transit -= 1

    # get the data to be retransmitted
    def get_retransmit_data(self, ack, selective_ack):
        # calculate the number of packets that can be retransmitted
        num_packets = self.max_buffer_size - self.packets_in_transit + 1
        retransmit_list = []
        # add all the sequence numbers that are NOT in selective acknowledgement list(SACK) to retransmit_list
        for seq_num in range(ack + 1, ack + num_packets):
            if seq_num not in selective_ack:
                retransmit_list.append((seq_num, self.buffer[seq_num]))
        return retransmit_list

    # adds one to the window size
    def additive_increase(self):
        self.max_buffer_size += 1
        self.log(f"Increasing window {self.max_buffer_size}")

    # divides the window size by 2
    def multiplicative_decrease(self):
        self.max_buffer_size = self.max_buffer_size // 2 + 1
        self.log(f"Decreasing window: {self.max_buffer_size}")

    # checks if all sent data has been acknowledged
    def all_data_acked(self):
        return self.last_sent == self.last_successful_ack

if __name__ == "__main__":
    buf = SendBuffer(3)
