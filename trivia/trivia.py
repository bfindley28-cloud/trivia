if __name__ == '__main__':
    print('welcome to benecia\'s trivia game!')

    score = 0

    response = input('who is the fastest hero in the marvel universe? ')
    if response.lower() == 'the flash':
        score += 5
        print('correct!')
    else:
        print('incorrect...')

    response = input('which marvel hero weild mjolnir? ')
    if response.lower() == 'thor':
        score += 5
        print('correct!')
    else:
        print('incorrect...')

    response = input( 'how many infinity stones are there? ')
    if response.lower() == '6' or response.lower() == 'six':
        score += 5
        print('correct!')
    else:
        print('incorrect...')
        
    response = input( 'where is Captain America from? ')
    if response.lower() == 'brooklyn':
        score += 5
        print('correct!')
    else:
        print('incorrect...')
    
    response = input( 'what is the name of the "winter soldier" who was Captain America\'s enemy in the marvel movie, "Captain America: The Winter Soldier"? ')
    if response.lower() == 'bucky':
        score += 5
        print('correct!')
    else: 
        print('incorrect...')

    response = input( 'Thor\'s mjolnir is made from the metal of a dying _____ ')
    if response.lower() == 'star':
        score += 5
        print('correct!')
    else: 
        print('incorrect...')

    response = input( 'who is Odin\'s first born child? ')
    if response.lower() == 'hela':
        score += 5
        print('correct!')
    else:
        print('incorrect...')

    response = input( '"Black Panther" is set in which fictional country? ')
    if response.lower() == 'w akanda':
        score += 5
        print('correct!')
    else: 
        print('incorrect...')

    print(f'congratulations! you scored {score}')