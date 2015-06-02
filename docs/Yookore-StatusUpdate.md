
# Yookore Status Updates

This yookore services are designed to access all services related to status updates.

This service is deployed on  **192.168.10.123:8000**

Use the prefix **http://41.160.30.173:3002/** for connection

If the server is down, you can restart it by going to the folder

/Documents/yookore_po/projects/yookore_django

Run:

**./manage.py runserver 0.0.0.0:8000**


**When a photo is attached the field 'img' will be available and contains an array of bytes that represents the picture **


# Status update
Notes related resources of the **Status Updates API**
**/api/status_updates/post/id**

## Status update Collection [/api/status_updates/post]
### List of status updates belonging to a particular user [GET]
+ Request

        GET /api/status_updates/post/username/

+ Response 200 (application/json)
    + Header

            Code: HTTP 200 OK
            Vary: Accept
            Allow: POST, OPTIONS, GET

    + Body  

            [
                {
                    "id": "9e5814e8-c351-11e4-a2f4-685b35b7fe48",
                    "author": "jwhite8",
                    "content_type": "statusupdate",
                    "created_at": "2015-03-05T18:06:44.429000",
                    "updated_at": null,
                    "view_count": 1,
                    "like_count": 0,
                    "comment_count": 0,
                    "body": "Excelent tutorial for Apache Cassandra by Ronald Mathies of Sodeso. Installing and using Apache",
                    "location": "Kavieng"
                },
                {
                    "id": "eda51380-c288-11e4-9e78-685b35b7fe48",
                    "author": "jwhite8",
                    "content_type": "statusupdate",
                    "created_at": "2015-03-04T18:07:39.834000",
                    "updated_at": "2015-03-05T17:13:17.762000",
                    "view_count": 35,
                    "like_count": 0,
                    "comment_count": 0,
                    "body": "This is a new status update. I am feeling awesome :)",
                    "location": "Kavieng"
                }
            ]

### Creating a status update for a specific user [POST]

+ Request

Two fields are required for this request: author, body

The location can be added as well

        POST /api/status_updates/post/username/

    + Body

            {
                "author": "jwhite8",
                "body": "Excelent tutorial for Apache Cassandra by Ronald Mathies of Sodeso. Installing and using Apache",
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
                "body": "Excelent tutorial for Apache Cassandra by Ronald Mathies of Sodeso. Installing and using Apache",
                "location": "Kavieng"
            }

### Creating a status update with a photo for a specific user [POST]

+ Request


        POST /api/status_updates/post_with_photo/username/


    + Body

            {
                "author": "jwhite8",
                "body": "Excelent tutorial for Apache Cassandra by Ronald Mathies of Sodeso. Installing and using Apache",
                "location": "Kavieng",
                "images": "my_photo.jpg"
            }

            File: my_photo.jpg

+ Response 201 (application/json)

    + Header

            Code: HTTP 201 CREATED
            Vary: Accept
            Allow: POST, OPTIONS, GET

    + Body

            {
                "author": "jwhite8",
                "body": "Excelent tutorial for Apache Cassandra by Ronald Mathies of Sodeso. Installing and using Apache",
                "location": "Kavieng",
                "img":"xxxxbbbttthjkkkddlllllldldlldlldldldldldldldldldlddl"
            }


### Retrieving a status update by id (uuid) [GET]

id represents the id of a specific the Status Update

+ Request

        GET /api/status_updates/post/id/


+ Response 200 (application/json)

        [
            {
                "id": "eda51380-c288-11e4-9e78-685b35b7fe48",
                "author": "jwhite8",
                "content_type": "statusupdate",
                "created_at": "2015-03-04T18:07:39.834000",
                "updated_at": "2015-03-05T15:39:32.851000",
                "view_count": 25,
                "like_count": 0,
                "comment_count": 0,
                "body": "Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio.@@@@ %%%%%",
                "location": "Kavieng"
            }
        ]

### Editing a status update [PUT]

status' id and author (username) are required fields
body and location can be updated

+ Request

        PUT /api/status_updates/post/id/

    + Body

            {
                "id": "9e5814e8-c351-11e4-a2f4-685b35b7fe48",
                "author": "jwhite8",
                "body": "Excelent tutorial for Apache Cassandra by Ronald Mathies of Sodeso. Installing and using Apache",
                "location": "Johannesburg"
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
                    "id": "9e5814e8-c351-11e4-a2f4-685b35b7fe48",
                    "author": "jwhite8",
                    "content_type": "statusupdate",
                    "created_at": "2015-03-05T18:06:44.429000",
                    "updated_at": "2015-03-05T18:28:23.687440",
                    "view_count": 2,
                    "like_count": 0,
                    "comment_count": 0,
                    "body": "Excelent tutorial for Apache Cassandra by Ronald Mathies of Sodeso. Installing and using Apache",
                    "location": "Johannesburg"
                }
            ]


## Status update Likes [/api/status_updates/like/]

### Liking a status update [POST]

object' id and author (username) are required fields

+ Request

        POST /api/status_updates/like/uuid/

        POST /api/content/uuid/likes/

    + Body

            {
                "object_id": "9e5814e8-c351-11e4-a2f4-685b35b7fe48",
                "author": "jwhite8"
            }

+ Response 201

    + Header

            Code: HTTP 201 CREATED
            Content-Type: application/json
            Vary: Accept
            Allow: POST, GET, OPTIONS

    + Body

            {
                "object_id": "9e5814e8-c351-11e4-a2f4-685b35b7fe48",
                "author": "jwhite8"
            }

### List of likes on a specific status update [GET]


+ Request

        GET /api/status_updates/like/id/

        GET /api/content/uuid/likes/


+ Response 200

    + Header

            Code: HTTP 200 OK
            Content-Type: application/json
            Vary: Accept
            Allow: POST, GET, OPTIONS

    + Body

            [
                {
                    "id": "88f9ecd4-c356-11e4-a723-685b35b7fe48",
                    "object_id": "9e5814e8-c351-11e4-a2f4-685b35b7fe48",
                    "author": "nwells7"
                },
                {
                    "id": "029733d9-c356-11e4-ab44-685b35b7fe48",
                    "object_id": "9e5814e8-c351-11e4-a2f4-685b35b7fe48",
                    "author": "jwhite8"
                },
                {
                    "id": "7fc13e1c-c356-11e4-99b8-685b35b7fe48",
                    "object_id": "9e5814e8-c351-11e4-a2f4-685b35b7fe48",
                    "author": "jwhite8"
                }
            ]

## Status update Comments [/api/status_updates/comment/]

### Commenting on a status update [POST]

object' id and author (username) and body are required fields

+ Request

        POST /api/status_updates/comment/id/

        POST /api/content/uuid/comments/

    + Body

            {
                "object_id": "9e5814e8-c351-11e4-a2f4-685b35b7fe48",
                "author":"jwhite8",
                "body":"I like this status too much :)"
            }

+ Response 201

    + Header

            Code: HTTP 201 CREATED
            Content-Type: application/json
            Vary: Accept
            Allow: POST, GET, OPTIONS

    + Body

            {
                "object_id": "9e5814e8-c351-11e4-a2f4-685b35b7fe48",
                "author":"jwhite8",
                "body":"I like this status too much :)"
            }

### List of comments on a specific status update [GET]


+ Request

        GET /api/status_updates/comment/id/

        GET /api/content/uuid/comments/


+ Response 200

    + Header

            Code: HTTP 200 OK
            Content-Type: application/json
            Vary: Accept
            Allow: POST, GET, OPTIONS

    + Body

            [
                {
                    "id": "73425197-c357-11e4-8fca-685b35b7fe48",
                    "object_id": "9e5814e8-c351-11e4-a2f4-685b35b7fe48",
                    "author": "nwells7",
                    "created_at": "2015-03-05T18:06:39.984000",
                    "updated_at": null,
                    "view_count": 0,
                    "like_count": 0,
                    "body": "I like this status a little bit more  :)"
                },
                {
                    "id": "0eb243fa-c357-11e4-9c22-685b35b7fe48",
                    "object_id": "9e5814e8-c351-11e4-a2f4-685b35b7fe48",
                    "author": "jwhite8",
                    "created_at": "2015-03-05T18:06:39.984000",
                    "updated_at": null,
                    "view_count": 0,
                    "like_count": 0,
                    "body": "I like this status too much :)"
                }
            ]
