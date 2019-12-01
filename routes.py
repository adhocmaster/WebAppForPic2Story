from app import app


@app.route('/')
def hello_world():
   return 'Hello World'


@app.route("/api/doodle2story")
def doodle2Story():
    return """
    LITERATURE
    A Summary and Analysis of the ‘Puss in Boots’ Fairy Tale
    An introduction to a classic fairy tale – analysed by Dr Oliver Tearle

    A classic example of the fairy tale featuring ‘the animal as helper’, ‘Puss in Boots’ entered the canon of classic fairy tales when Charles Perrault included it (as ‘Le Chat Botté’) in his 1697 collection of fairy stories, although like many of the greatest fairy tales, an earlier version can be found in the 1634 Pentamerone, a collection of oral folk tales compiled by Giambattista Basile. How we should analyse ‘Puss in Boots’ has troubled authors, commentators, and illustrators over the years. George Cruikshank objected to ‘a system of imposture being rewarded by the greatest worldly advantages’. Before we look more closely at this aspect of the tale, here’s a brief summary of the ‘Puss in Boots’ tale:

    A miller dies and leaves his three sons all he has: he leaves his mill to his eldest son, an ass to the middle son, and to the youngest son, he leaves his cat. The youngest son thinks he’s drawn the short straw with the cat, but the cat promises that if the son gets him some boots made, he will prove to be a worthy and helpful pet. Once the cat has some boots and a little bag he can wear, he goes off and hunts for rabbits. Having caught a rabbit, Puss in Boots takes it to the King, telling him that it’s a gift from the Lord Marquis of Carabas, the cat’s master.


    Shortly after this, Puss in Boots caught some partridges, and once again he took them to the King and announced that they were a gift from the Lord Marquis of Carabas. This happened for several months. Then, one day, Puss in Boots hatched his big plan: he commanded his master to wash at a certain point in the river, and waited until the King’s coach came riding by, with the Princess accompanying the King in the coach. Then, having concealed his master’s clothes under a rock, Puss in Boots jumped out in front of the coach and asked for help, claiming that his master, the Lord Marquis of Carabas, had been robbed, and all of his clothes had been taken.
    """

