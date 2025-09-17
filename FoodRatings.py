from sortedcontainers import SortedSet

class FoodRatings:
    def __init__(self, foods: List[str], cuisine: List[str], ratings: List[int]):
        self.cuisines = defaultdict(lambda: SortedSet(key=lambda x: (-x[0], x[1])))
        self.food_to_cuisine = dict()
        self.food_to_rating = dict()
        
        for index in range(len(foods)):
            _cuisine, food, rating = cu[index], foods[index], ratings[index]
            
            self.cuisines[_cuisine].add((rating, food))
            self.food_to_cuisine[food] = _cuisine
            self.food_to_rating[food] = rating
            
    def changeRating(self, food: str, new_rating: int) -> None:
        old_rating = self.food_to_rating[food]
        cuisine = self.food_to_cuisine[food]
        
        self.cuisines[cuisine].discard((old_rating, food))
        self.cuisines[cuisine].add((new_rating, food))
        self.food_to_rating[food] = new_rating
        
    def highestRated(self, cuisine: str) -> str:
        return self.cuisines[cuisine][0][1]
