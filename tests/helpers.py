import string
import random

def generate_unique_email(cohort_number):
  #Генератор email
  random_part = ''.join(random.choices(string.digits, k=3))
  return f"olegandreev{cohort_number}{random_part}@yandex.ru"

def generate_password(length):
  #Генератор пароля
  characters = string.ascii_letters + string.digits + "!@#$%^&*()"
  return ''.join(random.choices(characters, k=length))