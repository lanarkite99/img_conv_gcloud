# Build and deploy to Google cloud

Command to build the application. PLease remember to change the project name and application name
```
gcloud builds submit --tag gcr.io/initial-streamlit-project/image_conv_aws  --project=initial-streamlit-project
```

Command to deploy the application
```
gcloud run deploy --image gcr.io/initial-streamlit-project/image_conv_aws --platform managed  --project=initial-streamlit-project --allow-unauthenticated
```