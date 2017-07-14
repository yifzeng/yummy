import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yummy.settings")
import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
import json

def main():
    from person.models import Person
    with open("1.json") as jsonfile:
        json_data = json.load(jsonfile)
        PersonList = []
        for dicobj in json_data:
            person = Person(volume=dicobj["volume"], postdate=dicobj["postdate"], gender=dicobj["gender"],idnum=dicobj["idnum"],city=dicobj["city"],dec=dicobj["dec"],image_urls=dicobj["image_urls"][0] )
            PersonList.append(person)
    Person.objects.bulk_create(PersonList)

if __name__ == "__main__":
    main()
    print('Done!')
