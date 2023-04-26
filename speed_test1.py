# Пример крошечного преимущества карты в скорости при использовании точно такой же функции:

# $ python -m timeit -s'xs=range(10)' 'map(hex, xs)'
# 100000 loops, best of 3: 4.86 usec per loop

# $ python -m timeit -s'xs=range(10)' '[hex(x) for x in xs]'
# 100000 loops, best of 3: 5.58 usec per loop
# Пример того, как сравнение производительности становится полностью обратным, когда карте нужна лямбда:

# $ python -m timeit -s'xs=range(10)' 'map(lambda x: x+2, xs)'
# 100000 loops, best of 3: 4.24 usec per loop

# $ python -m timeit -s'xs=range(10)' '[x+2 for x in xs]'
# 100000 loops, best of 3: 2.32 usec per loop

# https://stackoverflow.com/questions/1247486/list-comprehension-vs-map
# есть много разных мнений 


import datetime

def decorator_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        print(datetime.datetime.now() - start)
        return result

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

#------------------------------------------------

# @decorator_time
# def one1():
#     return list(range(0, 13 ** 7, 2))

# one1()

# #------------------------------------------------

# @decorator_time
# def one2():
#     return [x for x in range(0, 13 ** 7, 2)]

# one2()

# #------------------------------------------------

# @decorator_time
# def one3():
#     return [x for x in range(13 ** 7) if not x & 1]

# one3()

# #------------------------------------------------

# @decorator_time
# def one():
#     return [x for x in range(13 ** 7) if not x % 2]

# one()

#------------------------------------------------

# @decorator_time
# def one4():
#     return list(filter(lambda x: not x & 1 ,range(13 ** 7)))

# one4()

# #------------------------------------------------

# numbers = list(range(1, 10000000))

#------------------------------------------------

# @decorator_time
# def two(numbers):
#     return list(filter(lambda x: not x&1, numbers)) 

# two(numbers)

# #------------------------------------------------

# @decorator_time
# def two1(numbers):
#     return [x for x in numbers if not x&1]

# two1(numbers)

# #------------------------------------------------

# @decorator_time
# def count_strings(*args):
#     count = 0 
#     for i in args:
#         if isinstance(i, str):
#             count += 1
#     return count

# count_strings(numbers)

# #------------------------------------------------

# @decorator_time
# def count_strings1(*args):
#     return sum(map(lambda x: isinstance(x, str), args))

# count_strings1(numbers)

# #------------------------------------------------

# @decorator_time
# def count_strings2(*args):
#     return sum(1 for v in args if isinstance(v, str))

# count_strings2(numbers)

# #------------------------------------------------
# # без if считаем True быстрее остальных

# @decorator_time
# def count_strings3(*args):
#     return sum(isinstance(x, str) for x in args)

# count_strings3(numbers)


#------------------------------------------------

# s = '''It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.

# The hallway smelt of boiled cabbage and old rag mats. At one end of it a coloured poster, too large for indoor display, had been tacked to the wall. It depicted simply an enormous face, more than a metre wide: the face of a man of about forty-five, with a heavy black moustache and ruggedly handsome features. Winston made for the stairs. It was no use trying the lift. Even at the best of times it was seldom working, and at present the electric current was cut off during daylight hours. It was part of the economy drive in preparation for Hate Week. The flat was seven flights up, and Winston, who was thirty-nine and had a varicose ulcer above his right ankle, went slowly, resting several times on the way. On each landing, opposite the lift-shaft, the poster with the enormous face gazed from the wall. It was one of those pictures which are so contrived that the eyes follow you about when you move. BIG BROTHER IS WATCHING YOU, the caption beneath it ran.

# Inside the flat a fruity voice was reading out a list of figures which had something to do with the production of pig-iron. The voice came from an oblong metal plaque like a dulled mirror which formed part of the surface of the right-hand wall. Winston turned a switch and the voice sank somewhat, though the words were still distinguishable. The instrument (the telescreen, it was called) could be dimmed, but there was no way of shutting it off completely. He moved over to the window: a smallish, frail figure, the meagreness of his body merely emphasized by the blue overalls which were the uniform of the party. His hair was very fair, his face naturally sanguine, his skin roughened by coarse soap and blunt razor blades and the cold of the winter that had just ended.

# Outside, even through the shut window-pane, the world looked cold. Down in the street little eddies of wind were whirling dust and torn paper into spirals, and though the sun was shining and the sky a harsh blue, there seemed to be no colour in anything, except the posters that were plastered everywhere. The blackmoustachio’d face gazed down from every commanding corner. There was one on the house-front immediately opposite. BIG BROTHER IS WATCHING YOU, the caption said, while the dark eyes looked deep into Winston’s own. Down at street level another poster, torn at one corner, flapped fitfully in the wind, alternately covering and uncovering the single word INGSOC. In the far distance a helicopter skimmed down between the roofs, hovered for an instant like a bluebottle, and darted away again with a curving flight. It was the police patrol, snooping into people’s windows. The patrols did not matter, however. Only the Thought Police mattered. Behind Winston’s back the voice from the telescreen was still babbling away about pig-iron and the overfulfilment of the Ninth Three-Year Plan. The telescreen received and transmitted simultaneously. Any sound that Winston made, above the level of a very low whisper, would be picked up by it, moreover, so long as he remained within the field of vision which the metal plaque commanded, he could be seen as well as heard. There was of course no way of knowing whether you were being watched at any given moment. How often, or on what system, the Thought Police plugged in on any individual wire was guesswork. It was even conceivable that they watched everybody all the time. But at any rate they could plug in your wire whenever they wanted to. You had to live—did live, from habit that became instinct—in the assumption that every sound you made was overheard, and, except in darkness, every movement scrutinized.

# Winston kept his back turned to the telescreen. It was safer, though, as he well knew, even a back can be revealing. A kilometre away the Ministry of Truth, his place of work, towered vast and white above the grimy landscape. This, he thought with a sort of vague distaste—this was London, chief city of Airstrip One, itself the third most populous of the provinces of Oceania. He tried to squeeze out some childhood memory that should tell him whether London had always been quite like this. Were there always these vistas of rotting nineteenth-century houses, their sides shored up with baulks of timber, their windows patched with cardboard and their roofs with corrugated iron, their crazy garden walls sagging in all directions? And the bombed sites where the plaster dust swirled in the air and the willow-herb straggled over the heaps of rubble; and the places where the bombs had cleared a larger patch and there had sprung up sordid colonies of wooden dwellings like chicken-houses? But it was no use, he could not remember: nothing remained of his childhood except a series of bright-lit tableaux occurring against no background and mostly unintelligible.

# The Ministry of Truth—Minitrue, in Newspeak [Newspeak was the official language of Oceania. For an account of its structure and etymology see Appendix.]—was startlingly different from any other object in sight. It was an enormous pyramidal structure of glittering white concrete, soaring up, terrace after terrace, 300 metres into the air. From where Winston stood it was just possible to read, picked out on its white face in elegant lettering, the three slogans of the Party: The Ministry of Truth contained, it was said, three thousand rooms above ground level, and corresponding ramifications below. Scattered about London there were just three other buildings of similar appearance and size. So completely did they dwarf the surrounding architecture that from the roof of Victory Mansions you could see all four of them simultaneously. They were the homes of the four Ministries between which the entire apparatus of government was divided. The Ministry of Truth, which concerned itself with news, entertainment, education, and the fine arts. The Ministry of Peace, which concerned itself with war. The Ministry of Love, which maintained law and order. And the Ministry of Plenty, which was responsible for economic affairs. Their names, in Newspeak: Minitrue, Minipax, Miniluv, and Miniplenty.

# The Ministry of Love was the really frightening one. There were no windows in it at all. Winston had never been inside the Ministry of Love, nor within half a kilometre of it. It was a place impossible to enter except on official business, and then only by penetrating through a maze of barbed-wire entanglements, steel doors, and hidden machine-gun nests. Even the streets leading up to its outer barriers were roamed by gorilla-faced guards in black uniforms, armed with jointed truncheons.

# Winston turned round abruptly. He had set his features into the expression of quiet optimism which it was advisable to wear when facing the telescreen. He crossed the room into the tiny kitchen. By leaving the Ministry at this time of day he had sacrificed his lunch in the canteen, and he was aware that there was no food in the kitchen except a hunk of dark-coloured bread which had got to be saved for tomorrow’s breakfast. He took down from the shelf a bottle of colourless liquid with a plain white label marked VICTORY GIN. It gave off a sickly, oily smell, as of Chinese rice-spirit. Winston poured out nearly a teacupful, nerved himself for a shock, and gulped it down like a dose of medicine.

# Instantly his face turned scarlet and the water ran out of his eyes. The stuff was like nitric acid, and moreover, in swallowing it one had the sensation of being hit on the back of the head with a rubber club. The next moment, however, the burning in his belly died down and the world began to look more cheerful. He took a cigarette from a crumpled packet marked VICTORY CIGARETTES and incautiously held it upright, whereupon the tobacco fell out on to the floor. With the next he was more successful. He went back to the living-room and sat down at a small table that stood to the left of the telescreen. From the table drawer he took out a penholder, a bottle of ink, and a thick, quarto-sized blank book with a red back and a marbled cover. For some reason the telescreen in the living-room was in an unusual position. Instead of being placed, as was normal, in the end wall, where it could command the whole room, it was in the longer wall, opposite the window. To one side of it there was a shallow alcove in which Winston was now sitting, and which, when the flats were built, had probably been intended to hold bookshelves. By sitting in the alcove, and keeping well back, Winston was able to remain outside the range of the telescreen, so far as sight went. He could be heard, of course, but so long as he stayed in his present position he could not be seen. It was partly the unusual geography of the room that had suggested to him the thing that he was now about to do.

# But it had also been suggested by the book that he had just taken out of the drawer. It was a peculiarly beautiful book. Its smooth creamy paper, a little yellowed by age, was of a kind that had not been manufactured for at least forty years past. He could guess, however, that the book was much older than that. He had seen it lying in the window of a frowsy little junk-shop in a slummy quarter of the town (just what quarter he did not now remember) and had been stricken immediately by an overwhelming desire to possess it. Party members were supposed not to go into ordinary shops (’dealing on the free market’, it was called), but the rule was not strictly kept, because there were various things, such as shoelaces and razor blades, which it was impossible to get hold of in any other way. He had given a quick glance up and down the street and then had slipped inside and bought the book for two dollars fifty. At the time he was not conscious of wanting it for any particular purpose. He had carried it guiltily home in his briefcase. Even with nothing written in it, it was a compromising possession.

# The thing that he was about to do was to open a diary. This was not illegal (nothing was illegal, since there were no longer any laws), but if detected it was reasonably certain that it would be punished by death, or at least by twenty-five years in a forced-labour camp. Winston fitted a nib into the penholder and sucked it to get the grease off. The pen was an archaic instrument, seldom used even for signatures, and he had procured one, furtively and with some difficulty, simply because of a feeling that the beautiful creamy paper deserved to be written on with a real nib instead of being scratched with an ink-pencil. Actually he was not used to writing by hand. Apart from very short notes, it was usual to dictate everything into the speak-write which was of course impossible for his present purpose. He dipped the pen into the ink and then faltered for just a second. A tremor had gone through his bowels. To mark the paper was the decisive act. In small clumsy letters he wrote: He sat back. A sense of complete helplessness had descended upon him. To begin with, he did not know with any certainty that this was 1984. It must be round about that date, since he was fairly sure that his age was thirty-nine, and he believed that he had been born in 1944 or 1945; but it was never possible nowadays to pin down any date within a year or two.

# For whom, it suddenly occurred to him to wonder, was he writing this diary? For the future, for the unborn. His mind hovered for a moment round the doubtful date on the page, and then fetched up with a bump against the Newspeak word DOUBLETHINK. For the first time the magnitude of what he had undertaken came home to him. How could you communicate with the future? It was of its nature impossible. Either the future would resemble the present, in which case it would not listen to him: or it would be different from it, and his predicament would be meaningless.

# For some time he sat gazing stupidly at the paper. The telescreen had changed over to strident military music. It was curious that he seemed not merely to have lost the power of expressing himself, but even to have forgotten what it was that he had originally intended to say. For weeks past he had been making ready for this moment, and it had never crossed his mind that anything would be needed except courage. The actual writing would be easy. All he had to do was to transfer to paper the interminable restless monologue that had been running inside his head, literally for years. At this moment, however, even the monologue had dried up. Moreover his varicose ulcer had begun itching unbearably. He dared not scratch it, because if he did so it always became inflamed. The seconds were ticking by. He was conscious of nothing except the blankness of the page in front of him, the itching of the skin above his ankle, the blaring of the music, and a slight booziness caused by the gin.

# Suddenly he began writing in sheer panic, only imperfectly aware of what he was setting down. His small but childish handwriting straggled up and down the page, shedding first its capital letters and finally even its full stops:

# April 4th, 1984. Last night to the flicks. All war films. One very good one of a ship full of refugees being bombed somewhere in the Mediterranean. Audience much amused by shots of a great huge fat man trying to swim away with a helicopter after him, first you saw him wallowing along in the water like a porpoise, then you saw him through the helicopters gunsights, then he was full of holes and the sea round him turned pink and he sank as suddenly as though the holes had let in the water, audience shouting with laughter when he sank. then you saw a lifeboat full of children with a helicopter hovering over it. there was a middle-aged woman might have been a jewess sitting up in the bow with a little boy about three years old in her arms. little boy screaming with fright and hiding his head between her breasts as if he was trying to burrow right into her and the woman putting her arms round him and comforting him although she was blue with fright herself, all the time covering him up as much as possible as if she thought her arms could keep the bullets off him. then the helicopter planted a 20 kilo bomb in among them terrific flash and the boat went all to matchwood. then there was a wonderful shot of a child’s arm going up up up right up into the air a helicopter with a camera in its nose must have followed it up and there was a lot of applause from the party seats but a woman down in the prole part of the house suddenly started kicking up a fuss and shouting they didnt oughter of showed it not in front of kids they didnt it aint right not in front of kids it aint until the police turned her turned her out i dont suppose anything happened to her nobody cares what the proles say typical prole reaction they never——'''


# @decorator_time
# def free2(s):
#     return 'ought ' in s.lower()

# print(free2(s))


# @decorator_time
# def free(s):
#     return any(map(lambda x: x.endswith('ought'), s.lower().split()))

# print(free(s))


# # этото быстрее чем map
# @decorator_time
# def free1(s):
#     return any(w.endswith('ought') for w in s.lower().split())

# print(free1(s))