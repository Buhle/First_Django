# Yookore Status Updates

### List of status updates for a specific user

To view status updates for a specific user should provide : username

* Request
		
		GET /api/v1/statusupdates/author/

* Content-Type

		application/json
		
* Header 

		Vary: Accept
		Allow: GET, HEAD, OPTIONS

* Request Body
		
		None
		
* Response Code

		200 OK
			
* Response Body

		{
            "id": "f54854eb-0940-11e5-8b7d-685b35b7fe48", 
            "author": "test_user", 
            "created_at": "2015-06-02T18:03:50.238000", 
            "updated_at": "2015-06-02T18:03:50.238000", 
            "view_count": 0, 
            "like_count": 0, 
            "comment_count": 0, 
            "body": "Reminder about things", 
            "location": null, 
            "at_mention": [], 
            "tags": [], 
            "url": "/media/uploaded_photos/				2015/06/02/6e3a8fafd8ec2dbb17d00e36b7bb1bca.jpg", 
            "image_url": null
        }, 
        {
            "id": "c707fcc5-0644-11e5-a794-685b35b7fe48", 
            "author": "test_user", 
            "created_at": "2015-05-29T22:53:37.139000", 
            "updated_at": "2015-05-29T22:53:37.139000", 
            "view_count": 11, 
            "like_count": 0, 
            "comment_count": 0, 
            "body": "Garden", 
            "location": null, 
            "at_mention": [], 
            "tags": [], 
            "url": "/media/uploaded_photos/2015/05/29/hs-2015-02-a-hires_jpg.jpg", 
            "image_url": null
        }



### Editing status updates using user id

To edit status user must provide : id

* Request
		
		GET /api/v1/statusupdates/id/

* Content-Type

		application/json
		
* Header 

		Vary: Accept
		Allow: GET, PUT, DELETE, HEAD, OPTIONS
		
* Request Body

		{ 
		    "body": "Reminder about things", 
		    "location": null, 
		    "at_mention": [], 
		    "tags": [], 
		    "url": "/media/uploaded_photos/2015/06/02/6e3a8fafd8ec2dbb17d00e36b7bb1bca.jpg", 
		    "image_url": null
		}
		
* Response Code

		202 ACCEPTED

* Response Body

		{
		    "id": "f54854eb-0940-11e5-8b7d-685b35b7fe48", 
		    "author": "test_user", 
		    "created_at": "2015-06-02T18:03:50.238000", 
		    "updated_at": "2015-06-03T16:58:35.162626", 
		    "view_count": 4, 
		    "like_count": 0, 
		    "comment_count": 0, 
		    "body": "Reminder about things that happened ", 
		    "location": null, 
		    "at_mention": [], 
		    "tags": [], 
		    "url": "/media/uploaded_photos/				2015/06/02/6e3a8fafd8ec2dbb17d00e36b7bb1bca.jpg", 
		    "image_url": null
		}


### Creating new status update for a user

Fields that are Required in order to create status : username and body 

* Request

		POST /api/v1/statusupdates/
		
* Content-Type

		application/json
		
* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS

* Request Body

		{
			"id": null, 
			"author": "test_user", 
			"view_count": null, 
			"like_count": null, 
			"body": "Good day ", 
			"location": null, 
    		"at_mention": [], 
    		"tags": [], 
    		"url": null, 
    		"image_url": null
		}

* Response Code

		201 CREATED

* Response Body

		{
            "id": "b0ccfdc5-0a8b-11e5-b5a2-685b35b7fe48", 
            "author": "test_user", 
            "created_at": "2015-06-04T09:31:18.762000", 
            "updated_at": "2015-06-04T09:31:18.762000", 
            "view_count": 0, 
            "like_count": 0, 
            "comment_count": 0, 
            "body": "Good day ", 
            "location": null, 
            "at_mention": [], 
            "tags": [], 
            "url": null, 
            "image_url": null
        }, 


### Creating new status updates with location

Fields that are Required in order to create status : username body and location

* Request

		POST /api/v1/statusupdates/

* Content-Type

		application/json
		
* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS

* Request Body

		{
    		"id": null, 
    		"author": "test_user", 
    		"view_count": null, 
    		"like_count": null, 
    		"comment_count": null, 
    		"body": "Good morning ", 
    		"location": "Randburg", 
    		"at_mention": [], 
    		"tags": [], 
    		"url": null, 
    		"image_url": null
		}
		
* Response Code

		201 CREATED

* Response Body

		{
            "id": "0460d16b-0a8f-11e5-a1ba-685b35b7fe48", 
            "author": "test_user", 
            "created_at": "2015-06-04T09:55:07.472000", 
            "updated_at": "2015-06-04T09:55:07.472000", 
            "view_count": 0, 
            "like_count": 0, 
            "comment_count": 0, 
            "body": "Good morning ", 
            "location": "Randburg", 
            "at_mention": [], 
            "tags": [], 
            "url": null, 
            "image_url": null
        }


### Creating new status updates with image

Fields that are Required in order to create status : username , body and image 

* Request

		POST /api/v1/statusupdates/

* Content-Type

		application/json

* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS

* Request Body

		{
    		"id": null, 
    		"author": "test_user", 
    		"view_count": null, 
    		"like_count": null, 
    		"comment_count": null, 
    		"body": "Hellow world", 
    		"location": null, 
    		"at_mention": [], 
    		"tags": [], 
    		"url": null, 
    		"image_url": "cats.jpeg"
		}
		
* Response Code

		201 CREATED

* Response Body

		{
            "id": "4887d64a-0a91-11e5-b930-685b35b7fe48", 
            "author": "test_user", 
            "created_at": "2015-06-04T10:11:20.806000", 
            "updated_at": "2015-06-04T10:11:20.806000", 
            "view_count": 0, 
            "like_count": 0, 
            "comment_count": 0, 
            "body": "Hellow world", 
            "location": null, 
            "at_mention": [], 
            "tags": [], 
            "url": "/media/uploaded_photos/2015/06/04/cats.jpeg", 
            "image_url": null
        }
        
### Create new status update with @mention

Fields that are Required in order to create status : username , body and 
@mention

* Request

		POST /api/v1/statusupdates/

* Content-Type

		application/json

* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS

* Request Body

		None

* Response Code

		201 CREATED

* Response Body

		{
    		"id": null,
    		"author": "thoko",
    		"view_count": null,
    		"like_count": null,
    		"comment_count": null,
    		"body": "today late",
    		"location": null,
    		"at_mention": [],
    		"tags": [],
    		"url": null,
    		"image_url": null
		}

### Creating new status updates tag friends

Fields that are Required in order to create status : username , body and tag friend name

* Request

		POST /api/v1/statusupdates/

* Content-Type

		application/json
		
* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS

* Request Body

		{
    		"id": null, 
    		"author": "test_user", 
    		"view_count": null, 
    		"like_count": null, 
    		"comment_count": null, 
    		"body": "Thursday", 
    		"location": "Randburg JHB", 
    		"at_mention": [], 
    		"tags": [], 
    		"url": null, 
    		"image_url": "cat.png"
		}
		
* Response Code

		201 CREATED

* Response Body

		{
            "id": "13fad9f8-0a92-11e5-855c-685b35b7fe48", 
            "author": "test_user", 
            "created_at": "2015-06-04T10:17:02.137000", 
            "updated_at": "2015-06-04T10:17:02.137000", 
            "view_count": 0, 
            "like_count": 0, 
            "comment_count": 0, 
            "body": "Thursday", 
            "location": "Randburg JHB", 
            "at_mention": [], 
            "tags": [
                "John"
            ], 
            "url": "/media/uploaded_photos/2015/06/04/cat.png", 
            "image_url": null
        } 
		
### Delete status update

Fields that are Required in order to delete status : id

* Request

		DELETE /api/v1/statusupdates/id/

* Content-Type

		application/json

* Header

		Vary: Accept
		Allow: GET, PUT, DELETE, HEAD, OPTIONS

* Request Body

		{
    		"id": "4887d64a-0a91-11e5-b930-685b35b7fe48", 
    		"author": "test_user", 
    		"created_at": "2015-06-04T10:11:20.806000", 
    		"updated_at": "2015-06-04T10:11:20.806000", 
    		"view_count": 1, 
    		"like_count": 0, 
    		"comment_count": 0, 
    		"body": "Hellow world", 
    		"location": null, 
    		"at_mention": [], 
    		"tags": [], 
    		"url": "/media/uploaded_photos/2015/06/04/cats.jpeg", 
    		"image_url": null
		}

* Response Code

		204 NO CONTENT

* Response Body

		None





