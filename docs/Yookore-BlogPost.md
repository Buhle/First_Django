# Yookore Blog Posts
This yookore services are designed to access all services related to blog posts.

This service is deployed on  **192.168.10.123:8000**

If the server is down, you can restart it by going to the folder

/Documents/yookore_po/projects/yookore_django

Run:

**./manage.py runserver 0.0.0.0:8000**


# Blog Posts
Notes related resources of the **Blog posts API**
**/api/blogposts/post/uuid**

## Blog Post Collection [/api/blogposts/post]
### List of blog posts belonging to a particular user [GET]
+ Request

        GET /api/blogposts/post/username/

+ Response 200 (application/json)
    + Header

            Code: HTTP 200 OK
            Vary: Accept
            Allow: POST, OPTIONS, GET
    + Body  

            [
                {
                    "id": "e81029b0-c3ef-11e4-8ba2-685b35b7fe48",
                    "author": "nwells7",
                    "content_type": "blogpost",
                    "created_at": "2015-03-06T12:57:32.517000",
                    "updated_at": null,
                    "view_count": 0,
                    "like_count": 0,
                    "comment_count": 0,
                    "title": "Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.",
                    "body": "Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum.\n\nCurabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.\n\nPhasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.",
                    "location": "Pretoria"
                },
                {
                    "id": "322bae05-c3ee-11e4-bfb3-685b35b7fe48",
                    "author": "nwells7",
                    "content_type": "blogpost",
                    "created_at": "2015-03-06T12:45:56.814000",
                    "updated_at": "2015-03-06T13:16:48.499000",
                    "view_count": 6,
                    "like_count": 2,
                    "comment_count": 1,
                    "title": "Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.",
                    "body": "Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum.\n\nCurabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est.\n\nPhasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.",
                    "location": "Kimberley"
                }
            ]

### Creating a blog post for a specific user [POST]

+ Request
Two fields are required for this request: author, title, body
The location can be added as well

            POST /api/blogposts/post/username/

    + Body

            {
                "author": "jwhite8",
                "title": "Title os this blog post",
                "body": "Former South African great Shaun Pollock Friday predicted the Proteas would win a first World Cup by beating Australia in the final, helping to make-up for his own personal setbacks against the four-time champions.",
                "location": "Kavieng"
            }


+ Response 201 (application/json)

    + Header

            Code: HTTP 201 CREATED
            Vary: Accept
            Allow: POST, OPTIONS, GET

    + Body

            {
                "author": "jwhite8",
                "title": "Title os this blog post",
                "body": "Former South African great Shaun Pollock Friday predicted the Proteas would win a first World Cup by beating Australia in the final, helping to make-up for his own personal setbacks against the four-time champions.",
                "location": "Kavieng"
            }


### Retrieving a blog post by its id (uuid) [GET]

+ Request

        GET /api/blogposts/post/id/

        GET /api/content/id/


+ Response 200 (application/json)

        [
            {
                "id": "060d8e6e-c409-11e4-ae7c-685b35b7fe48",
                "author": "nwells7",
                "content_type": "blogpost",
                "created_at": "2015-03-06T15:10:16.895000",
                "updated_at": null,
                "view_count": 1,
                "like_count": 0,
                "comment_count": 0,
                "title": "Title os this blog post",
                "body": "Former South African great Shaun Pollock Friday predicted the Proteas would win a first World Cup by beating Australia in the final, helping to make-up for his own personal setbacks against the four-time champions.",
                "location": "Kavieng"
            }
        ]

### Editing a Blog Post [PUT]

The blog post's id and author (username) are required fields
title, body and location can be updated

+ Request

        PUT /api/blogposts/post/id/

    + Body

            {
                "id": "060d8e6e-c409-11e4-ae7c-685b35b7fe48",
                "author": "nwells7",
                "title": "Updated title of the blog post",
                "body": "Former South African great Shaun Pollock Friday predicted the Proteas would win a first World Cup by beating Australia in the final, helping to make-up for his own personal setbacks against the four-time champions.",
                "location": "Kavieng"
            }

+ Response 202

    + Header

            Code: HTTP 202 ACCEPTED
            Content-Type: application/json
            Vary: Accept
            Allow: PUT, GET, OPTIONS, DELETE

    + Body

            [
                {
                    "id": "060d8e6e-c409-11e4-ae7c-685b35b7fe48",
                    "author": "nwells7",
                    "content_type": "blogpost",
                    "created_at": "2015-03-06T15:10:16.895000",
                    "updated_at": "2015-03-06T16:05:28.168372",
                    "view_count": 1,
                    "like_count": 0,
                    "comment_count": 0,
                    "title": "Updated title of the blog post",
                    "body": "Former South African great Shaun Pollock Friday predicted the Proteas would win a first World Cup by beating Australia in the final, helping to make-up for his own personal setbacks against the four-time champions.",
                    "location": "Kavieng"
                }
            ]


## Blog posts Likes [/api/blogposts/like]

### Liking a Blog Post [POST]

Blog post's id and author (username) are required fields

+ Request

        POST /api/blogposts/like/id/

        POST /api/content/id/likes/

    + Body

            {
                "object_id": "060d8e6e-c409-11e4-ae7c-685b35b7fe48",
                "author": "nwells7"
            }

+ Response 201

    + Header

            Code: HTTP 201 CREATED
            Content-Type: application/json
            Vary: Accept
            Allow: POST, GET, OPTIONS

    + Body

            {
                "object_id": "060d8e6e-c409-11e4-ae7c-685b35b7fe48",
                "author": "nwells7"
            }

### List of likes on a specific blog post [GET]


+ Request

        GET /api/blogposts/like/id/

        GET /api/content/id/likes/


+ Response 200

    + Header

            Code: HTTP 200 OK
            Content-Type: application/json
            Vary: Accept
            Allow: POST, GET, OPTIONS

    + Body

            [
                {
                    "id": "e160df38-c40a-11e4-8869-685b35b7fe48",
                    "object_id": "060d8e6e-c409-11e4-ae7c-685b35b7fe48",
                    "author": "nwells7"
                },
                {
                    "id": "1c9d86fa-c40b-11e4-abf8-685b35b7fe48",
                    "object_id": "060d8e6e-c409-11e4-ae7c-685b35b7fe48",
                    "author": "jwhite8"
                }
            ]

## Blog post Comments [/api/blogposts/comment]

### Commenting on a blog post [POST]

Blog post's id and author (username) and body are required fields

+ Request

        POST /api/blogposts/comment/id/

        POST /api/content/id/comments/

    + Body

                {
                    "object_id": "060d8e6e-c409-11e4-ae7c-685b35b7fe48",
                    "author": "jwhite8",
                    "body": "This is really amazing!"
                }

+ Response 201

    + Header

            Code: HTTP 201 CREATED
            Content-Type: application/json
            Vary: Accept
            Allow: POST, GET, OPTIONS

    + Body

                {
                    "object_id": "060d8e6e-c409-11e4-ae7c-685b35b7fe48",
                    "author": "jwhite8",
                    "body": "This is really amazing!"
                }

### List of comments on a specific blog post [GET]


+ Request

        GET /api/blogposts/comment/id/

        GET /api/content/id/comments/


+ Response 200

    + Header

            Code: HTTP 200 OK
            Content-Type: application/json
            Vary: Accept
            Allow: POST, GET, OPTIONS

    + Body

            [
                {
                    "id": "99fee985-c40b-11e4-ad87-685b35b7fe48",
                    "object_id": "060d8e6e-c409-11e4-ae7c-685b35b7fe48",
                    "author": "jwhite8",
                    "created_at": "2015-03-06T15:10:16.898000",
                    "updated_at": null,
                    "view_count": 0,
                    "like_count": 0,
                    "body": "This is really amazing!"
                },
                {
                    "id": "df817a00-c40b-11e4-8fa2-685b35b7fe48",
                    "object_id": "060d8e6e-c409-11e4-ae7c-685b35b7fe48",
                    "author": "nwells7",
                    "created_at": "2015-03-06T15:10:16.898000",
                    "updated_at": null,
                    "view_count": 0,
                    "like_count": 0,
                    "body": "I agree with jwhite8 :P"
                }
            ]
