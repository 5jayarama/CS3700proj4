# represents a memory buffer for received data
class RecvBuffer:
    def __init__(self):
        self.buffer = []
        self.received_seq_nums = set()
        self.last_seq_num_print = -1

    # takes in a new data packet and adds it to the buffer
    def add(self, seq_num, data):
        # if the packet has already been received, ignore it
        if seq_num in self.received_seq_nums:
            return
        # insert the data packet in the correct place
        index = -1
        for i, (seq, _) in enumerate(self.buffer):
            if seq > seq_num:
                index = i
                break
        if index == -1:
            self.buffer.append((seq_num, data))
        else:
            self.buffer.insert(index, (seq_num, data))
        # record the addition in the list of received sequence numbers
        self.received_seq_nums.add(seq_num)

    # flushes out invalid data packets from the buffer
    def flush(self):
        flushed_packets = []
        # locate any consecutive packets
        for seq_num, data in self.buffer:
            if seq_num == self.last_seq_num_print + 1:
                flushed_packets.append((seq_num, data))
                self.last_seq_num_print += 1
            else:
                break
        # remove the flushed packets from the buffer
        self.buffer = self.buffer[len(flushed_packets):]
        return flushed_packets

    # returns a list of recieved sequence numbers
    def get_received_seq_nums(self):
        return list(self.received_seq_nums)


if __name__ == "__main__":
    recv = RecvBuffer()

