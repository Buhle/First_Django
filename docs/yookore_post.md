# Yookore Post

[Creating a post](#creation-simple)

[Creating a post with a location](#creation-with-location)

[Creating a post with a photo](#creation-with-photo)

[Creating a post and @mentioning some friends](#creation-with-at-mention)

[Creating a post and tagging some friends](#creation-with-tagging)

[List of post for a specific user](#list-blog-post)

[View a specific blog post using id](#view-blog-post)

[Editing a post](#editing-status-update)

[Deleting a post](#deleting-status-update)

When creating a post, the field *author* , *target_id*, *target_type* and *body* should always be in the payload

target_type can only be **person, page or group** 

target_id is the **username** if the target_type is person 

target_id is the **uuid** if the target_type is group or page

<a id="creation-simple"></a>

### Creating new post for a user

Fields that are Required in order to create post : username , target_id , target_type and body 

* Request

		POST /api/v1/posts/
		
* Content-Type

		application/json
		
* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS

* Request Body

		{
			"author": "pat",
			"target_id": "john",
			"target_type": "person" 
			"body": "hi friends " 
		}
		

* Response Code

		201 CREATED

* Response Body

		{
    		"id": null,
    		"author": "pat",
    		"view_count": null,
    		"like_count": null,
    		"comment_count": null,
    		"target_id": "john",
    		"target_type": "person",
    		"body": "hi friend",
    		"location": null,
    		"at_mention": [],
    		"tags": [],
    		"url": null,
    		"image_url": null
		}  
		  		
<a id="creation-with-location"></a>

### Creating new post with location


Fields that are Required in order to create post : username , target_id , target_type, body and location

* Request

		POST /api/v1/posts/

* Content-Type

		application/json
		
* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS

* Request Body

		{
    		"author": "dan", 
    		"target_id": "bf2ef1d7-0df8-11e5-8566-685b35b7fe48",
			"target_type": "page"
    		"body": "adding location ", 
    		"location": "zimbabwe"
		}
		
* Response Code

		201 CREATED

* Response Body

		{
    		"id": null,
    		"author": "dan",
    		"view_count": null,
    		"like_count": null,
    		"comment_count": null,
    		"target_id": "bf2ef1d7-0df8-11e5-8566-685b35b7fe48",
    		"target_type": "page",
    		"body": "adding location",
    		"location": "zimbabwe",
    		"at_mention": [],
    		"tags": [],
    		"url": null,
    		"image_url": null
		}
        
<a id="creation-with-at-mention"></a>
      
### Create new post with @mention


Fields that are Required in order to create post : username , target_id , target_type , body and @mention

* Request

		POST /api/v1/posts/

* Content-Type

		application/json

* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS

* Request Body

		{
    		"author": "dan",
    		"target_id": "pat",
			"target_type": "person"
    		"body": "mention friends", 
    		"at_mention": ['john',
    			 		'pat', 
    			 		'test_user'],
		}


* Response Code

		201 CREATED

* Response Body

		{
    		"id": null,
    		"author": "dan",
    		"view_count": null,
    		"like_count": null,
    		"comment_count": null,
    		"target_id": "bf2ef1d7-0df8-11e5-8566-685b35b7fe48",
    		"target_type": "group",
    		"body": "mention friends",
    		"location": null,
    		"at_mention": [],
    		"tags": [],
    		"url": null,
    		"image_url": null
		}
		
<a id="creation-with-tagging"></a>

### Creating new post tag friends


Fields that are Required in order to create post : username , target_id , target_type , body and tag friend name

* Request

		POST /api/v1/posts/

* Content-Type

		application/json
		
* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS

* Request Body

		{
    		"author": "dan",
    		"target_id": "bf2ef1d7-0df8-11e5-8566-685b35b7fe48",
			"target_type": "page"
    		"body": "you have been tagged ", 
    		"tags": ['john', 'pat'],
		} 
    		 
		
* Response Code

		201 CREATED

* Response Body

		{
    		"id": null,
    		"author": "dan",
    		"view_count": null,
    		"like_count": null,
    		"comment_count": null,
    		"target_id": "bf2ef1d7-0df8-11e5-8566-685b35b7fe48",
    		"target_type": "page",
    		"body": "you have been tagged",
    		"location": null,
    		"at_mention": [],
    		"tags": [],
    		"url": null,
    		"image_url": null
		}

<a id="creation-with-photo"></a>

### Creating new post with a photo


Fields that are Required in order to create post : username , target_id , target_type , body and image 

* Request

		POST /api/v1/posts/

* Content-Type

		application/json

* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS

* Request Body

		{
    		"author": "john", 
    		"target_id": "test_user",
			"target_type": "person"
    		"body": "selfeee ", 
    		"image": "cat.png"
		}
		
* Response Code

		201 CREATED

* Response Body

		{
    		"id": null,
    		"author": "joy",
    		"view_count": null,
    		"like_count": null,
    		"comment_count": null,
    		"target_id": "test_user",
    		"target_type": "person",
    		"body": "selfeee",
    		"location": null,
    		"at_mention": [],
    		"tags": [],
    		"url": null,
    		"image_url": "cat.png"
		}
	
<a id="list-blog-post"></a>

### List of post for a specific user


To view post for a specific user should provide : username

* Request
		
		GET /api/v1/posts/usename/

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
    	"list": [
        	{
            	"id": "d909d49c-0e91-11e5-82a0-685b35b7fe48",
            	"author": "pat",
            	"created_at": "2015-06-09T12:25:27.901000",
            	"updated_at": "2015-06-09T12:25:27.901000",
            	"view_count": 0,
            	"like_count": 0,
            	"comment_count": 0,
            	"target_id": "john",
            	"target_type": "person",
            	"body": "hi friend",
            	"location": null,
            	"at_mention": [],
            	"tags": [],
            	"url": null,
            	"image_url": null
        	},
        	{
            	"id": "13c0c20c-0e86-11e5-bd3c-685b35b7fe48",
            	"author": "pat",
            	"created_at": "2015-06-09T11:01:12.447000",
            	"updated_at": "2015-06-09T11:01:12.447000",
            	"view_count": 0,
            	"like_count": 0,
            	"comment_count": 0,
            	"target_id": "patrick",
            	"target_type": "person",
            	"body": "Je ne savais pas!",
            	"location": null,
            	"at_mention": [],
            	"tags": [],
            	"url": null,
            	"image_url": null
        	},
        	{
            	"id": "bf2ef1d7-0df8-11e5-8566-685b35b7fe48",
            	"author": "pat",
            	"created_at": "2015-06-08T18:09:31.524000",
            	"updated_at": "2015-06-08T18:09:31.524000",
            	"view_count": 0,
            	"like_count": 0,
            	"comment_count": 0,
            	"target_id": "test_user",
            	"target_type": "person",
            	"body": "my post on this wall",
            	"location": null,
            	"at_mention": [],
            	"tags": [],
            	"url": null,
            	"image_url": null
        	}
    	],
    	"page": {
        	"totalPages": 1,
        	"totalElements": 3,
        	"number": 1,
        	"size": 25
    	},
    	"links": {
        	"previous": null,
        	"next": null
    	}
		}
		
<a id="view-blog-post"></a>	

### View specific post using user id


To view specific post user must provide : id

* Request
		
		GET /api/v1/posts/id/

* Content-Type

		application/json
		
* Header 

		Vary: Accept
		Allow: GET, PUT, DELETE, HEAD, OPTIONS
		
* Request Body

		None
			
* Response Code

		200 OK

* Response Body

		{
    		"id": "d909d49c-0e91-11e5-82a0-685b35b7fe48",
    		"author": "pat",
    		"created_at": "2015-06-09T12:25:27.901000",
    		"updated_at": "2015-06-09T14:17:33.751554",
    		"view_count": 1,
    		"like_count": 0,
    		"comment_count": 0,
    		"target_id": "john",
    		"target_type": "person",
    		"body": "hi friend",
    		"location": "Randburg JHB",
    		"at_mention": [],
    		"tags": [],
    		"url": "/media/uploaded_photos/2015/06/09/cats.jpeg",
    		"image_url": null
		}

<a id="editing-status-update"></a>

### Editing post using user id


To edit post user must provide : id

* Request
		
		GET /api/v1/posts/id/

* Content-Type

		application/json
		
* Header 

		Vary: Accept
		Allow: GET, PUT, DELETE, HEAD, OPTIONS
		
* Request Body

		{
    		"id": "d909d49c-0e91-11e5-82a0-685b35b7fe48",
    		"author": "pat",
    		"created_at": "2015-06-09T12:25:27.901000",
    		"updated_at": "2015-06-09T12:25:27.901000",
    		"view_count": 1,
    		"like_count": 0,
    		"comment_count": 0,
    		"target_id": "john",
    		"target_type": "person",
    		"body": "hi friend",
    		"location": null,
    		"at_mention": [],
    		"tags": [],
    		"url": null,
    		"image_url": null
		}
			
* Response Code

		202 ACCEPTED

* Response Body

		{
    		"id": "d909d49c-0e91-11e5-82a0-685b35b7fe48",
    		"author": "pat",
    		"created_at": "2015-06-09T12:25:27.901000",
    		"updated_at": "2015-06-09T14:17:33.751554",
    		"view_count": 1,
    		"like_count": 0,
    		"comment_count": 0,
    		"target_id": "john",
    		"target_type": "person",
    		"body": "hi friend",
    		"location": "Randburg JHB",
    		"at_mention": [],
    		"tags": [],
    		"url": "/media/uploaded_photos/2015/06/09/cats.jpeg",
    		"image_url": null
		}
		
<a id="deleting-status-update"></a>
		
### Delete a post


To delete post user should provide : id

* Request

		DELETE /api/v1/posts/id/

* Content-Type

		application/json

* Header

		Vary: Accept
		Allow: GET, PUT, DELETE, HEAD, OPTIONS

* Request Body

		{
    		"id": "d6cc0f23-0e93-11e5-bb07-685b35b7fe48",
    		"author": "john",
    		"created_at": "2015-06-09T12:39:43.134000",
    		"updated_at": "2015-06-09T12:39:43.134000",
    		"view_count": 1,
    		"like_count": 0,
    		"comment_count": 0,
    		"target_id": "pat",
    		"target_type": "group",
    		"body": "Good  day friends",
    		"location": null,
    		"at_mention": [],
    		"tags": [],
    		"url": null,
    		"image_url": null
		}

* Response Code

		204 NO CONTENT

* Response Body

		None





