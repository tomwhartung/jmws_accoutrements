
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

## Tutorials

- Create a VM: https://cloud.google.com/compute/docs/instances/create-start-instance
- Quickstart Linux VM: https://cloud.google.com/compute/docs/quickstart-linux
- Running an Apache Webserver: https://cloud.google.com/compute/docs/tutorials/basic-webserver-apache
- Compute Engine Quickstart
  - To-do app using Mongo DB:
  -  https://console.cloud.google.com/getting-started?tutorial=compute_quickstart&project=actions-codelab-f5fa4&folder&organizationId

## This Looks Like What I Ultimately Want to Do:

- GCP Cloud Launcher: https://cloud.google.com/launcher/

## Docs, Certification, and More

- GCP Documentation Home: https://cloud.google.com/docs/
- GCP Documentation Overview: https://cloud.google.com/docs/overview/
- GCP Certifications: https://cloud.google.com/certification/

# Process

Following is the proposed process to use, going forward:

[X] 1. Research AWS and assess feasibility
[ ] 2. Try out some very simple, basic, introductory tutorials
[ ] 3. Do the Wordpress Blog on Amazon Linux tutorial
[ ] 4. Assess whether we want to do this for seeourminds.com
[ ]    4.1 Backup idea: Maybe host groja.com instead of, or in addition to, seeourminds.com
[ ] 5. Proceed, or not, as decided
[ ] 6. Compare process, free tier, resulting site maintenance required, etc. of GCP to AWS

