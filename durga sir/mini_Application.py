class Movie:
    '''This is Doc String developed by Ajay For Demo'''

    def __init__(self,title,hero,heroine):
        self.title=title
        self.hero=hero
        self.heroine=heroine

    def info(self):
        print("Movie Name Is:",self.title)
        print("Hero Name Is:",self.hero)
        print("Heroine Name Is:",self.heroine)

list_of_movie=[]

while True:
    title=input("Enter Movie Name:")
    hero=input("Enter Hero Name:")
    heroine=input("Enter Heroine Name:")
    m=Movie(title,hero,heroine)
    m.info()
    list_of_movie.append(m)
    print("Movie Added Successfully")
    option=input("Do you want to add one more movie[yes/no]:")
    if option.lower()=='no':
        break
print(list_of_movie)

for movie in list_of_movie:
    print(movie)
    movie.info()
    print()
