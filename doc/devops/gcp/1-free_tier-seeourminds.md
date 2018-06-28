
# devops/gcp/1-free_tier-seeourminds.md

It is time to try out hosting in the cloud.
Most importantly, my service from forethought.net has become unreliable, and is slow at best.

This file is for notes about using the Google Cloud Platform to host seeourminds.com .

# Goals

- Compare and contrast GCP with AWS
  - Take enough notes that we can write a blog post and develop a presentation for meetups
- Try to stay on the free tier
  - Try to set up a notification so we know when we are exceeding the limits of the free tier
  - It looks like even if I exceed the free tier, it will not be super-expensive

# References

I have been doing some research, and the process looks reasonable.
If anything, setup is probably easier than hosting it here at home, because each instance is specialized.

## Introductory Information

- GCP Free Tier Portal: https://cloud.google.com/free/
- GCP Free Tier FAQ: https://cloud.google.com/free/docs/frequently-asked-questions
- Translating AWS jargon to GCP: https://cloud.google.com/free/docs/map-aws-google-cloud-platform
- GCP Docs landing page: https://cloud.google.com/docs/

## Tutorials

- Create a VM: https://cloud.google.com/compute/docs/instances/create-start-instance
- Quickstart Linux VM: https://cloud.google.com/compute/docs/quickstart-linux
- Running an Apache Webserver: https://cloud.google.com/compute/docs/tutorials/basic-webserver-apache
- Compute Engine Quickstart
  - To-do app using Mongo DB:
  -  https://console.cloud.google.com/getting-started?tutorial=compute_quickstart&project=actions-codelab-f5fa4&folder&organizationId

