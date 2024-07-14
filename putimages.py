
import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('Bill_Gates.jpeg','Bill Gates'),
      ('Elon_Musk.jpeg','Elon Musk'),
      ('Mark_Zuckerberg.jpeg','Mark Zuckerberg'),
      ('Satya_Nadella.jpeg','Satya Nadella'),
      ('Sunder_Pichai.jpeg','Sunder Pichai'),
      ('David_Solomon.jpg','David Solomon')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('employee-img','images/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})
