
def right_to_left(phrases):
    return ','.join(phrases).replace('right', 'left')


right_to_left(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
right_to_left(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
right_to_left(("brightness wright",)) == "bleftness wleft", "One phrase"
right_to_left(("enough", "jokes")) == "enough,jokes", "Nothing to replace"