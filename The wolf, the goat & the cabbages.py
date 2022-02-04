#The wolf,the goat & the cabbages

Ready = input ("Are you ready to play 'The wolf, the goat & the cabbages'? If you are then press P, if you don't understand the rules then press Q:")

if Ready == ('Q'):
    print (" ")
    print ("OK, let's learn!"
           "You start of on one side of a river with a WOLF a GOAT and some CABBAGES. you need to get eveyone across to the other side. There is one boat in the water but it can hold only you and one other thing. But the problem is that you can't leave the WOLF AND THE GOAT alone together or the wolf will eat the goat and you can't leave the GOAT WITH THE CABBAGES alone or the goat will eat the cabbages. Can you geet everyone across without anyone eating each other?")
    Ready_To_Play = input ('Do you understand? Yes or no:')
    Boat = ('boat left')
    Wolf = ('wolf left')
    Goat = ('goat left')
    Cabbages = ('cabbages left')
    Win_Check = ('false')
    End_Phrase = (' 0 ')

#confused play no
    if Ready_To_Play == ('no'):
        Help = input ('What do you need help? Please answer in short phrases like objective, movement pattern or possible lose. You can ask another question straight away or press P to play.')

        while Help != ('P'):
            if Help == ('objective'):
                print ('learn yourself!')
            if Help == ('movement pattern'):
                print ('use you two brain cells really hard and maybe something will happen')
            if Help == ('possible lose'):
                print ('were you not listening?!')
            Help = input ('Do you need any more help? If not, press P.')

        if Help == ('P'):
            print ('Nice! lets play!')
        print ("UPDATE: wolf left, goat left, cabbages left, boat left")

        while Win_Check == ('false'):
            for x in range (1):
                Movement = input ("Movement:")
                if Movement == ('boat left'):
                    Boat = ('boat left')
                if Movement == ('boat right'):
                    Boat = ('boat right')
                if Movement == ('wolf left') and Boat == ('boat right'):
                    Wolf = ('wolf left')
                    Boat = ('boat left')
                if Movement == ('wolf right') and Boat == ('boat left'):
                    Wolf = ('wolf right')
                    Boat = ('boat right')
                if Movement == ('goat left') and Boat == ('boat right'):
                    Goat = ('goat left')
                    Boat = ('boat left')
                if Movement == ('goat right') and Boat == ('boat left'):
                    Goat = ('goat right')
                    Boat = ('boat right')
                if Movement == ('cabbages left') and Boat == ('boat right'):
                    Cabbages = ('cabbages left')
                    Boat = ('boat left')
                if Movement == ('cabbages right') and Boat == ('boat left'):
                    Cabbages = ('cabbages right')
                    Boat = ('boat right')

                if Wolf == ('wolf right') and Goat == ('goat right') and Cabbages == ('cabbages right') and Boat == ('boat right'):
                    Win_Check = ('true')

                if Wolf == ('wolf left') and Goat == ('goat left') and Cabbages == ('cabbages right') and Boat == ('boat right'):
                    Win_Check = ('true')
                if Wolf == ('wolf right') and Goat == ('goat right') and Cabbages == ('cabbages left') and Boat == ('boat left'):
                    Win_Check = ('true')
                if Goat == ('goat left') and Cabbages == ('cabbages left') and Wolf == ('wolf right') and Boat == ('boat right'):
                    Win_Check = ('true')
                if Goat == ('goat right') and Cabbages == ('cabbages right') and Wolf == ('wolf left') and Boat == ('boat left'):
                    Win_Check = ('true')

                print ("UPDATE: ", Wolf, ", ",Goat, ", ",Cabbages, ", ",Boat)

        if Wolf == ('wolf right') and Goat == ('goat right') and Cabbages == ('cabbages right') and Boat == ('boat right'):
            End_Phrase = ('Woooooo! you won!')
        if Wolf == ('wolf left') and Goat == ('goat left') and Cabbages == ('cabbages right') and Boat == ('boat right'):
            End_Phrase = ('Oof, you left the wolf and the goat alone together and the wolf ate the the goat!')
        if Wolf == ('wolf right') and Goat == ('goat right') and Cabbages == ('cabbages left') and Boat == ('boat left'):
            End_Phrase = ('Oh oh, your wolf has eaten your goat!')
        if Goat == ('goat left') and Cabbages == ('cabbages left') and Wolf == ('wolf right') and Boat == ('boat right'):
            End_Phrase = ('Nooooooo, your goat ate the cabbages')
        if Goat == ('goat right') and Cabbages == ('cabbages right') and Wolf == ('wolf left') and Boat == ('boat left'):
            End_Phrase = ('Nom nom, the cabbages have been devoured by the goat')

        print (End_Phrase)

            
        







#confused play yes

    if Ready_To_Play == ('yes'):
        print ('Nice! lets play!')
        print ("UPDATE: wolf left, goat left, cabbages left, boat left")

        while Win_Check == ('false'):
            for x in range (1):
                Movement = input ("Movement:")
                if Movement == ('boat left'):
                    Boat = ('boat left')
                if Movement == ('boat right'):
                    Boat = ('boat right')
                if Movement == ('wolf left') and Boat == ('boat right'):
                    Wolf = ('wolf left')
                    Boat = ('boat left')
                if Movement == ('wolf right') and Boat == ('boat left'):
                    Wolf = ('wolf right')
                    Boat = ('boat right')
                if Movement == ('goat left') and Boat == ('boat right'):
                    Goat = ('goat left')
                    Boat = ('boat left')
                if Movement == ('goat right') and Boat == ('boat left'):
                    Goat = ('goat right')
                    Boat = ('boat right')
                if Movement == ('cabbages left') and Boat == ('boat right'):
                    Cabbages = ('cabbages left')
                    Boat = ('boat left')
                if Movement == ('cabbages right') and Boat == ('boat left'):
                    Cabbages = ('cabbages right')
                    Boat = ('boat right')

                if Wolf == ('wolf right') and Goat == ('goat right') and Cabbages == ('cabbages right') and Boat == ('boat right'):
                    Win_Check = ('true')

                if Wolf == ('wolf left') and Goat == ('goat left') and Cabbages == ('cabbages right') and Boat == ('boat right'):
                    Win_Check = ('true')
                if Wolf == ('wolf right') and Goat == ('goat right') and Cabbages == ('cabbages left') and Boat == ('boat left'):
                    Win_Check = ('true')
                if Goat == ('goat left') and Cabbages == ('cabbages left') and Wolf == ('wolf right') and Boat == ('boat right'):
                    Win_Check = ('true')
                if Goat == ('goat right') and Cabbages == ('cabbages right') and Wolf == ('wolf left') and Boat == ('boat left'):
                    Win_Check = ('true')

                print ("UPDATE: ", Wolf, ", ",Goat, ", ",Cabbages, ", ",Boat)

        if Wolf == ('wolf right') and Goat == ('goat right') and Cabbages == ('cabbages right') and Boat == ('boat right'):
            End_Phrase = ('Woooooo! you won!')
        if Wolf == ('wolf left') and Goat == ('goat left') and Cabbages == ('cabbages right') and Boat == ('boat right'):
            End_Phrase = ('Oof, you left the wolf and the goat alone together and the wolf ate the the goat!')
        if Wolf == ('wolf right') and Goat == ('goat right') and Cabbages == ('cabbages left') and Boat == ('boat left'):
            End_Phrase = ('Oh oh, your wolf has eaten your goat!')
        if Goat == ('goat left') and Cabbages == ('cabbages left') and Wolf == ('wolf right') and Boat == ('boat right'):
            End_Phrase = ('Nooooooo, your goat ate the cabbages')
        if Goat == ('goat right') and Cabbages == ('cabbages right') and Wolf == ('wolf left') and Boat == ('boat left'):
            End_Phrase = ('Nom nom, the cabbages have been devoured by the goat')

        print (End_Phrase)

#Play programe

if Ready == ('P'):
    print ("let's play!")
    print ("What you need to do is say for example 'wolf right' or 'wolf left' and then you will get an update on where everyone is after each movment for example 'wolf left, goat right, cabbages right'. Let's do this!")
    Boat = ('boat left')
    Wolf = ('wolf left')
    Goat = ('goat left')
    Cabbages = ('cabbages left')
    Win_Check = ('false')
    End_Phrase = (' 0 ')
    print ("UPDATE: wolf left, goat left, cabbages left, boat left")

#Movment programme

    while Win_Check == ('false'):
        for x in range (1):
            Movement = input ("Movement:")
            if Movement == ('boat left'):
                Boat = ('boat left')
            if Movement == ('boat right'):
                Boat = ('boat right')
            if Movement == ('wolf left') and Boat == ('boat right'):
                Wolf = ('wolf left')
                Boat = ('boat left')
            if Movement == ('wolf right') and Boat == ('boat left'):
                Wolf = ('wolf right')
                Boat = ('boat right')
            if Movement == ('goat left') and Boat == ('boat right'):
                Goat = ('goat left')
                Boat = ('boat left')
            if Movement == ('goat right') and Boat == ('boat left'):
                Goat = ('goat right')
                Boat = ('boat right')
            if Movement == ('cabbages left') and Boat == ('boat right'):
                Cabbages = ('cabbages left')
                Boat = ('boat left')
            if Movement == ('cabbages right') and Boat == ('boat left'):
                Cabbages = ('cabbages right')
                Boat = ('boat right')

            if Wolf == ('wolf right') and Goat == ('goat right') and Cabbages == ('cabbages right') and Boat == ('boat right'):
                Win_Check = ('true')

            if Wolf == ('wolf left') and Goat == ('goat left') and Cabbages == ('cabbages right') and Boat == ('boat right'):
                Win_Check = ('true')
            if Wolf == ('wolf right') and Goat == ('goat right') and Cabbages == ('cabbages left') and Boat == ('boat left'):
                Win_Check = ('true')
            if Goat == ('goat left') and Cabbages == ('cabbages left') and Wolf == ('wolf right') and Boat == ('boat right'):
                Win_Check = ('true')
            if Goat == ('goat right') and Cabbages == ('cabbages right') and Wolf == ('wolf left') and Boat == ('boat left'):
                Win_Check = ('true')

            print ("UPDATE: ", Wolf, ", ",Goat, ", ",Cabbages, ", ",Boat)

    if Wolf == ('wolf right') and Goat == ('goat right') and Cabbages == ('cabbages right') and Boat == ('boat right'):
        End_Phrase = ('Woooooo! you won!')
    if Wolf == ('wolf left') and Goat == ('goat left') and Cabbages == ('cabbages right') and Boat == ('boat right'):
        End_Phrase = ('Oof, you left the wolf and the goat alone together and the wolf ate the the goat!')
    if Wolf == ('wolf right') and Goat == ('goat right') and Cabbages == ('cabbages left') and Boat == ('boat left'):
        End_Phrase = ('Oh oh, your wolf has eaten your goat!')
    if Goat == ('goat left') and Cabbages == ('cabbages left') and Wolf == ('wolf right') and Boat == ('boat right'):
        End_Phrase = ('Nooooooo, your goat ate the cabbages')
    if Goat == ('goat right') and Cabbages == ('cabbages right') and Wolf == ('wolf left') and Boat == ('boat left'):
        End_Phrase = ('Nom nom, the cabbages have been devoured by the goat')

    print (End_Phrase)
