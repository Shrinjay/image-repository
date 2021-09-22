# DaGallery: My submission to the Shopify Winter 2022 Intern Challenge.

### Features
* Upload and retrieve photos.
* Find photos by the objects within them, powered by YOLOv5 object detection.
* Find photos by the location they were taken using EXIF data.

#### Implementation Details
* The backend is built in Python with Flask, and the front-end is in React.
* The backend stores files in an AWS S3 Bucket and stores the object keys 
and associated features, such as location and objects
in the file system on a sqlite database.
* When users upload an image, the object detection model and exif 
processing is applied to extract object and location features, before
uploading the photo into S3 and creating a record in the sqlite database.
* When the user retrieves images, a query is first run on the sqlite database
to filter images by title, objects in them or location. Then the object key
is used to retrieve the image from AWS S3.

## Demo
![Demo](demofy.gif)
  
## Get Started

1. Install all required python pacakges with*
   
```pip install -r requirements.txt```

*Note that your pip command may vary, such as pip3

2. Install all required JavaScript packages with:

```
cd client
npm install
cd ../
   ```
   
4. If desired, you can run tests with pytest:

```pytest```

5. Start the server*:

```
python main.py
```
*Note that your python command may vary, such as python3

6. In a new terminal, start the client:
```
cd client
npm start
```
