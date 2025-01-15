variable "credentials" {
  description = "My Credentials"
  default = "./keys/my-creds.json"
}


variable "project" {
  description = "Project Location"
  default = "seismic-sunbeam-447702-m7"
}


variable "region" {
  description = "Project Location"
  default = "us-central"
}


variable "location" {
  description = "Project Location"
  default = "US"
}


variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "seismic-sunbeam-447702-m7-bucket1"   
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
