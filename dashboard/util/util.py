# *** reformat index: credit_card, payment_type, etc. ***
# to Credit Card, Payment Type, so on.
# the function is used for text printing
def reformatIndexToStr(str_to_reformat:str) -> str:
    str_partitions = str_to_reformat.partition('_')
    str_formatted = str_partitions[0].capitalize()+' '+str_partitions[2].capitalize()

    return str_formatted