from collections import Counter


def repeated_word(string):

    # look = list(sentence.split(" "))

    # occurrence = Counter(look)

    # for i in look:

    #     if occurrence[i] > 1:
    #         return i

    string = string.lower();  
   
    words = string.split(" ");  
    
    for i in range(0, len(words)):  
        count = 1;  
        for j in range(i+1, len(words)):  
            if(words[i] == (words[j])):  
                count = count + 1;  
                
        if(count > 1 and words[i] != "0"):
            return words[i]


if __name__ == "__main__":


   
    print(repeated_word(
            "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
        ))

    print(repeated_word("Once upon a time, there was a brave princess who..."))

