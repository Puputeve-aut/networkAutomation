import art
def findHightesBidder(bidding_dictionary):
    winner = ''
    hightestBid = 0
    for bidder in bidding_dictionary:
        bidAmount = bidding_dictionary[bidder]
        if bidAmount > hightestBid:
            hightestBid = bidAmount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${hightestBid}.')        


bids = {}
continueBidding = True

while continueBidding:
    print(art.gavel)
    personName = input("What is your name? ")
    price = int(input("What is your bid? $"))
    
    bids[personName] = price
    
    shouldContinue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if shouldContinue == 'no':
        continueBidding = False
        findHightesBidder(bids)
    elif shouldContinue == 'yes':
        print("\n" * 100)