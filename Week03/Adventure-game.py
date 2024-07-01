print('You find yourself at a crossroads deep within the Enchanted Forest. To proceed, you must choose your path wisely. The dense TREES or mysterious CAVE')
first_chose = ""
second_chose = ""
thirt_chose = ""

first_chose = str(input('Your Choise is?... '))
first_chose = first_chose.lower()
print(first_chose)
if first_chose == 'trees':
    print('As he progressed, the environment became cooler and more humid. The trees seemed to whisper to each other in an unknown language, and luminescent fungi illuminated the ground. He found a clearing with a pool of silver water, reflecting the stars above. He felt watched, with shadows moving around. You will enter in the POOL or RUN')
elif first_chose == 'cave':
    print('Upon entering the cave, he found a labyrinth of tunnels with walls gleaming from mineral deposits. After hours of exploration, he discovered a chamber illuminated by an ethereal blue glow, filled with crystals reflecting light in a mesmerizing manner. You enter the CHAMBER or PICK the mineral')

second_chose = str(input('Your Choise is?...'))
second_chose = second_chose.lower()
print(second_chose)
if first_chose == 'cave':
    if second_chose == 'chamber':
        print('He decides to enter the chamber illuminated by the crystals in the cave, and he is amazed by the stunning beauty of the environment. The crystals cast an ethereal blue glow that fills the space, creating mesmerizing reflections in every direction. The atmosphere is tranquil and charged with a mysterious energy that seems to permeate him as he explores the area. Suddenly ou see a red button you PRESS the button or NO')
    elif second_chose == 'pick':
        print('While gathering the shimmering minerals in the cave, Kael discovers crystals of extraordinary beauty that reflect light in mesmerizing patterns. They emanate a subtle energy of peace and harmony, leaving you intrigued by their magical properties. Suddenly ou see a red button you PRESS the button or NO')
elif first_chose == 'trees':
    if second_chose == 'pool':
        print('Fascinated by the pool of silver water, you decide to enter. He experiences a deep sense of calm and renewal, feeling connected to the essence of the forest. The water seems to have magical properties, revitalizing him and providing insights into the mysteries of the place. With respect, he emerges, aware of the gift received and the importance of not abusing that power. Suddenly ou see a red button you PRESS the button or NO')
    elif second_chose == 'run':
        print('After noticing shadows moving around him in the forest, he decides to run towards what he believes to be the way out. The sprint takes him deeper into the forest, where he comes upon a moonlit clearing. Suddenly ou see a red button you PRESS the button or NO')

thirt_chose = str(input('Your Choise is?...'))
thirt_chose = thirt_chose.lower()
if thirt_chose == 'press':
    print('You wake up and realize it was all a dream.')
elif thirt_chose == 'no':
    print('The button enlarges and presses against you, crushing your face, then you awaken.')