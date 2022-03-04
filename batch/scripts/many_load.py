import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, Region, State, Iso


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header
    Iso.objects.all().delete()
    Site.objects.all().delete()
    Category.objects.all().delete()
    Region.objects.all().delete()
    State.objects.all().delete()

    # Format
    # name,description,justification,year,longitude,latitude,area_hectares,category,state,region,iso


    for row in reader:
        print(row)
        c, created = Category.objects.get_or_create(name=row[7])
        reg, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])
        st, created = State.objects.get_or_create(name=row[8])
        try:
            y=int(row[3])
        except:
            y=None

        try:
            lg=float(row[4])
        except:
            lg = None

        try:
            lt=float(row[5])
        except:
            lt = None
        try:
            a=float(row[6])
        except:
            a = None

        s, created = Site.objects.get_or_create(name=row[0], description=row[1], justification=row[2],
                                                    year=y, longitude=lg, latitude=lt,
                                                    area_hectares=a, category=c, state=st,region=reg,iso=i)
        s.save()


        #p, created = Person.objects.get_or_create(email=row[0])
        #c, created = Course.objects.get_or_create(title=row[2])

       # r = Membership.LEARNER
       # if row[1] == 'I':
        #    r = Membership.INSTRUCTOR
        #m = Membership(role=r, person=p, course=c)
       # m.save()
