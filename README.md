# Deploy manager

## Create Service account

* Please create new GCP Service Account with role `CloudBuild Editor`
* Generate credentials file in JSON format

### Set correct path to Service Account JSON file

Please replace `/path/to/google-credentials.json` in `docker-compose.yaml` and set correct path to Google Service Account credentials JSON file.

### Optionally: set GCS Project ID

Please set `PROJECT_ID` environment value in `docker-compose.yaml`

## Deploy using docker-compose

    docker-compose up -d
    
Please open [http://localhost:5000](http://localhost:5000)