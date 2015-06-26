# Yookore Blog Post

[Creating a blog post](#creation-simple)

[Creating a blog post with a location](#creation-with-location)

[Creating a blog post with a photo](#creation-with-photo)

[Creating a blog post and @mentioning some friends](#creation-with-at-mention)

[Creating a blog post and tagging some friends](#creation-with-tagging)

[List of blog post for a specific user](#list-blog-post)

[Editing a blog post](#editing-status-update)

[Deleting a blog post](#deleting-status-update)

When creating a blog post, the field *author* , *title* and *body* should always be in the payload

<a id="creation-simple"></a>

### Creating new blog post for a user


Fields that are Required in order to create blog post : username , title and body 

* Request

		POST /api/v1/blogposts/
		
* Content-Type

		application/json
		
* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS

* Request Body

		{
			"author": "pat", 
			"body": "Tuesday " 
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
    		"title": "mr",
    		"body": "Tuesday",
    		"location": null,
    		"at_mention": [],
    		"tags": [],
    		"url": null,
    		"image_url": null
		}  
		  		
<a id="creation-with-location"></a>

### Creating new blog post with location


Fields that are Required in order to create blog post : username , title , body and location

* Request

		POST /api/v1/blogposts/

* Content-Type

		application/json
		
* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS

* Request Body

		{
    		"author": "john", 
    		"title": "mr"
    		"body": "Good morning ", 
    		"location": "Johannesburg"
		}
		
* Response Code

		201 CREATED

* Response Body

		{
    		"id": null,
    		"author": "john",
    		"view_count": null,
    		"like_count": null,
    		"comment_count": null,
    		"title": "mr",
    		"body": "Good morning",
    		"location": "Johannesburg",
    		"at_mention": [],
    		"tags": [],
    		"url": null,
    		"image_url": null
		}
        	
<a id="creation-with-photo"></a>

### Creating new blog post with a photo


Fields that are Required in order to create blog post : username , title , body and image 

* Request

		POST /api/v1/blogposts/

* Content-Type

		application/json

* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS

* Request Body

		{
    		"author": "john", 
    		"title": "mr"
    		"body": "Good morning ", 
    		"image": "butterfly.jpeg"
		}
		
* Response Code

		201 CREATED

* Response Body

		{
    		"id": null,
    		"author": "john",
    		"view_count": null,
    		"like_count": null,
    		"comment_count": null,
    		"title": "mr",
    		"body": "Good morning",
    		"location": "Johannesburg",
    		"at_mention": [],
    		"tags": [],
    		"url": null,
    		"image_url": "butterfly.jpeg"
		}

<a id="creation-with-at-mention"></a>
      
### Create new blog post with @mention


Fields that are Required in order to create blog post : username , title , body and @mention

* Request

		POST /api/v1/blogposts/

* Content-Type

		application/json

* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS

* Request Body

		{
    		"author": "pat",
    		"title": "mr " 
    		"body": "adding at mention", 
    		"at_mention": ['user1',
    			 		'user2', 
    			 		'user3'],
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
    		"title": "mr",
    		"body": "adding at mention",
    		"location": null,
    		"at_mention": [],
    		"tags": [],
    		"url": null,
    		"image_url": null
		}
		
<a id="creation-with-tagging"></a>

### Creating new blog post tag friends


Fields that are Required in order to create blog post : username , title , body and tag friend name

* Request

		POST /api/v1/blogposts/

* Content-Type

		application/json
		
* Header

		Vary: Accept
		Allow: GET, POST, HEAD, OPTIONS

* Request Body

		{
    		"author": "pat", 
    		"body": "tagging my friends", 
    		"tags": ['thoko', 'zama'],
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
    		"title": "mr",
    		"body": "tagging my friends",
    		"location": null,
    		"at_mention": [],
    		"tags": [],
    		"url": null,
    		"image_url": null
		} 
        		
<a id="list-blog-post"></a>

### List of blog post for a specific user


To view blog post for a specific user should provide : username

* Request
		
		GET /api/v1/blogposts/usename/

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
            	"id": "cfee6a75-0e86-11e5-8241-685b35b7fe48",
            	"author": "john",
            	"created_at": "2015-06-09T11:06:28.158000",
            	"updated_at": "2015-06-09T11:06:28.158000",
            	"view_count": 0,
            	"like_count": 0,
            	"comment_count": 0,
            	"title": "mr",
            	"body": "Good morning",
            	"location": "Johannesburg",
            	"at_mention": [],
            	"tags": [],
            	"url": "/media/uploaded_photos/2015/06/09/butterfly.jpeg",
            	"image_url": null
        	},
        	{
            	"id": "8fca5051-0e86-11e5-a4fc-685b35b7fe48",
            	"author": "john",
            	"created_at": "2015-06-09T11:04:40.547000",
            	"updated_at": "2015-06-09T11:04:40.547000",
            	"view_count": 0,
            	"like_count": 0,
            	"comment_count": 0,
           		"title": "mr",
            	"body": "Good morning",
            	"location": "Johannesburg",
            	"at_mention": [],
            	"tags": [],
            	"url": null,
            	"image_url": null
        	}
    		],
    	"page": {
        	"totalPages": 1,
        	"totalElements": 2,
        	"number": 1,
        	"size": 25
    		},
    	"links": {
        	"previous": null,
        	"next": null
    	}
		}

<a id="editing-status-update"></a>

### Editing blog post using user id


To edit blog post user must provide : id

* Request
		
		GET /api/v1/blogposts/id/

* Content-Type

		application/json
		
* Header 

		Vary: Accept
		Allow: GET, PUT, DELETE, HEAD, OPTIONS
		
* Request Body

		{
    		"id": "d8686ee8-0e84-11e5-b14c-685b35b7fe48",
    		"author": "pat",
    		"created_at": "2015-06-09T10:52:23.386000",
    		"updated_at": "2015-06-09T10:52:23.386000",
    		"view_count": 1,
    		"like_count": 0,
    		"comment_count": 0,
    		"title": "mr",
    		"body": "Tuesday",
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
    		"id": "d8686ee8-0e84-11e5-b14c-685b35b7fe48",
    		"author": "pat",
    		"created_at": "2015-06-09T10:52:23.386000",
    		"updated_at": "2015-06-09T11:29:41.154678",
    		"view_count": 1,
    		"like_count": 0,
    		"comment_count": 0,
    		"title": "mr",
    		"body": "Tuesday documentation",
    		"location": "Randburg",
    		"at_mention": [],
    		"url": null,
    		"image_url": null
		}
		
<a id="deleting-status-update"></a>
		
### Delete blog post


To delete blog post user should provide : id

* Request

		DELETE /api/v1/blogposts/id/

* Content-Type

		application/json

* Header

		Vary: Accept
		Allow: GET, PUT, DELETE, HEAD, OPTIONS

* Request Body

		{
    		"id": "8fca5051-0e86-11e5-a4fc-685b35b7fe48",
    		"author": "john",
    		"created_at": "2015-06-09T11:04:40.547000",
    		"updated_at": "2015-06-09T11:04:40.547000",
    		"view_count": 1,
    		"like_count": 0,
    		"comment_count": 0,
    		"title": "mr",
    		"body": "Good morning",
    		"location": "Johannesburg",
    		"at_mention": [],
    		"tags": [],
    		"url": null,
    		"image_url": null
		}

* Response Code

		204 NO CONTENT

* Response Body

		None





