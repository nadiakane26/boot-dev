from functools import reduce
def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length

        def with_length(doc):
            lines = doc.split('\n')
            count = sum(1 for line in lines if sequence in line)
            return count
        
        return with_length

    return with_char

