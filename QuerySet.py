python manage.py shell

from task1.models import Buyer, Game

# создаем покупателей
buyer1 = Buyer.objects.create(name="Buyer1", balance=100.00, age=20)
buyer2 = Buyer.objects.create(name="Buyer2", balance=150.00, age=17)
buyer3 = Buyer.objects.create(name="Buyer3", balance=200.00, age=30)

# создаем игры
game1 = Game.objects.create(title="Game1", cost=50.00, size=1.5,
                            description="game1111", age_limited=True)
game2 = Game.objects.create(title="Game2", cost=75.00, size=2.0,
                            description="game2222", age_limited=True)
game3 = Game.objects.create(title="Game3", cost=100.00, size=2.5,
                            description="game3333", age_limited=False)

# Buyer1 владеет всеми играми
buyer1.games.set([game1, game2, game3])

# Buyer2 (возраст < 18) владеет только игрой без ограничения возраста
buyer2.games.set([game3])


# Buyer3 владеет двумя играми с ограничением возраста
buyer3.games.set([game1, game2])
