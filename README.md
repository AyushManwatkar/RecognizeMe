<h1>RecognizeMe: Facial Recognition App on AWS</h1>

<p>Explore how to build a Facial Recognition App on AWS using powerful services such as Amazon Rekognition, AWS Lambda, Amazon DynamoDB, Amazon API Gateway, and Amazon S3 with a React front end. Let’s dive into the step-by-step process of creating this application.</p>

<h2>Architecture</h2>
<img src="Architecture.jpg" alt="Architecture">

<h2>Flows</h2>

<h3>Flow #1: Registration Flow</h3>
<ol>
    <li><strong>Employee Image Upload</strong>: Employee pictures are uploaded to the 'employee-bucket-image' S3 bucket.</li>
    <li><strong>Trigger Registration Lambda</strong>: The upload triggers the Registration Lambda function.</li>
    <li><strong>Index Employee Pictures</strong>: The Registration Lambda function uses Amazon Rekognition to index the employee pictures.</li>
    <li><strong>Generate Rekognition ID</strong>: This process generates a unique Rekognition ID for each employee.</li>
    <li><strong>Store Employee Data</strong>: The employee's information, including the Rekognition ID, is stored in a DynamoDB table.</li>
</ol>

<h3>Flow #2: Authentication Flow</h3>
<ol>
    <li><strong>Visitor/Employee Image Upload</strong>: A visitor or employee uploads an image using the React front end.</li>
    <li><strong>Call API Gateway</strong>: The front end calls the API Gateway to handle the upload.</li>
    <li><strong>Store Image in Visitor S3 Bucket</strong>: The image is stored in the 'visitor-bucket-image' S3 bucket.</li>
    <li><strong>Trigger Authentication Lambda</strong>: The upload triggers the Authentication Lambda function.</li>
    <li><strong>Generate Unique Key</strong>: The Authentication Lambda function uses Amazon Rekognition to generate a unique key.</li>
    <li><strong>Check Rekognition ID</strong>: The Rekognition ID is checked against the entries in the DynamoDB table for authentication.</li>
</ol>
