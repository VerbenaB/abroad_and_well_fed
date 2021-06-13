from db.run_sql import run_sql
from models.review import Review

import repositories.user_repository as user_repository
import repositories.restaurant_repository as restaurant_repository


def save(review):
    sql = "INSERT INTO reviews(user_id, restaurant_id, review) VALUES (%s, %s, %s) RETURNING id"
    values = [review.user.id, review.restaurant.id, review.review]
    results = run_sql(sql, values)
    review.id = results[0]['id']
    return review

def select_all():
    reviews = []
    sql = "SELECT * FROM reviews"
    results = run_sql(sql)

    for row in reviews:
        user = user = user_repository.select(row['user_id'])
        restaurant = restaurant_repository.select(row['location_id'])
        review = Review(user, restaurant, row['review'], row['id'])
        reviews.append(review)
    return reviews

def delete_all():
    sql = "DELETE FROM reviews"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM reviews WHERE id = %s"
    values = [id]
    run_sql(sql, values)