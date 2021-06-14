from django.conf import settings
settings.configure(DEBUG=True)

# from django.core.wsgi import get_wsgi_application


# application = get_wsgi_application()


from models import User
import sys


def seed():
    print("db synced!")

    thomas= User.objects.create(
        username = "santiago",
        email =  "santiago@email.com",
        password=  "123456",
        photoUrl= 
        "https://res.cloudinary.com/dmlvthmqr/image/upload/v1607914466/messenger/775db5e79c5294846949f1f55059b53317f51e30_s3back.png",   
    )

    santiago= User.objects.create(
        username= "thomas",
        email= "thomas@email.com",
        password= "123456",
        photoUrl=
            "https://res.cloudinary.com/dmlvthmqr/image/upload/v1607914467/messenger/thomas_kwzerk.png",
    )

    chiumbo= User.objects.create(
        username= "chiumbo",
        email= "chiumbo@email.com",
        password= "123456",
        photoUrl=
        "https://res.cloudinary.com/dmlvthmqr/image/upload/v1607914468/messenger/8bc2e13b8ab74765fd57f0880f318eed1c3fb001_fownwt.png",
    )

    hualing= User.objects.create(
        username= "hualing",
        email= "hualing@email.com",
        password= "123456",
        photoUrl=
        "https://res.cloudinary.com/dmlvthmqr/image/upload/v1607914466/messenger/6c4faa7d65bc24221c3d369a8889928158daede4_vk5tyg.png",
    )

    User.objects.create(
      username= "ashanti",
      email= "ashanti@email.com",
      password= "123456",
      photoUrl=
        "https://res.cloudinary.com/dmlvthmqr/image/upload/v1607914466/messenger/68f55f7799df6c8078a874cfe0a61a5e6e9e1687_e3kxp2.png",
    )

    User.objects.create(
      username= "julia",

      email= "julia@email.com",
      password= "123456",
      photoUrl=
        "https://res.cloudinary.com/dmlvthmqr/image/upload/v1607914468/messenger/d9fc84a0d1d545d77e78aaad39c20c11d3355074_ed5gvz.png",
    )

    User.objects.create(
      username= "cheng",
      email= "cheng@email.com",
      password= "123456",
      photoUrl=
        "https://res.cloudinary.com/dmlvthmqr/image/upload/v1607914466/messenger/9e2972c07afac45a8b03f5be3d0a796abe2e566e_ttq23y.png",
    )

    print('seeded users and messages')



def runseed():
    print("Seeding...")
    try:
        seed()
    except Exception as err:
        print(err)
        sys.exit()
    finally:
        print("closing db connection")
        print("db connection closed")

runseed()

