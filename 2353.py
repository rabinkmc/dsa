# Algorithm
#
#     Create a class Food containing foodRating and foodName properties,
#     and overload less than operator method to keep the highest rated or
#     lexicographically smaller named element on the top in the priority queue.
#
#     Create three hash maps:
#         foodRatingMap, to store ratings associated with the respective food.
#         foodCuisineMap, to store the cuisine name of the respective food.
#         cuisineFoodMap, to store Food(foodRating, foodName) elements in a
#         priority queue associated with the respective cuisine.
#
#     Initialization. Iterate on all indices of the foods array, and for each index i:
#         Store (foods[i], ratings[i]) and (foods[i], cuisines[i]) key-value pairs
#         in foodRatingMap and foodCuisineMap respectively. Insert Food(ratings[i], foods[i])
#         element in the priority queue of cuisines[i] key of cuisineFoodMap.
#
#     Implementing changeRating(food, newRating) method:
#         Update new rating in foodRatingMap. Fetch the cuisine name
#         for food from foodRatingMap. Insert the Food(newRating, food)
#         element in the priority queue of the cuisine name in cuisineFoodMap.
#
#     Implementing highestRated(cuisine) method:
#         Get the top element (i.e. highestRated) from the priority queue of
#         cuisine in cuisineFoodMap. If the rating of the top element and the
#         rating of the corresponding food in foodRatingMap are not the same, i.e.
#         highestRated.foodRating != foodRatingMap[highestRated.foodName], then
#         we discard and remove the current top element and fetch the next top
#         element from the priority queue. Repeat this step until ratings are the same.
#         Return the food name of the top element, i.e. highestRated.foodName.
from typing import List
from collections import defaultdict
import heapq


class Food:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def __lt__(self, other):
        if self.rating == other.rating:
            return self.name < other.name
        return self.rating > other.rating


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_ratings = dict()
        self.food_cuisines = dict()
        self.cuisine_foods = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_ratings[food] = rating
            self.food_cuisines[food] = cuisine
            heapq.heappush(self.cuisine_foods[cuisine], Food(food, rating))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_ratings[food] = newRating
        cuisine = self.food_cuisines[food]
        heapq.heappush(self.cuisine_foods[cuisine], Food(food, newRating))

    def highestRated(self, cuisine: str) -> str:
        highest_rated = self.cuisine_foods[cuisine][0]
        while self.food_ratings[highest_rated.name] != highest_rated.rating:
            heapq.heappop(self.cuisine_foods[cuisine])
            highest_rated = self.cuisine_foods[cuisine][0]
        return highest_rated.name


# foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
# cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
# ratings = [9, 12, 8, 15, 14, 7]
foods = ["emgqdbo", "jmvfxjohq", "qnvseohnoe", "yhptazyko", "ocqmvmwjq"]
cuisines = ["snaxol", "snaxol", "snaxol", "fajbervsj", "fajbervsj"]
ratings = [2, 6, 18, 6, 5]
obj = FoodRatings(foods, cuisines, ratings)
obj.changeRating("emgqdbo", 14)
obj.highestRated("snaxol")
