
# devops/aws/1-free_tier-tomwhartung.md

It is time to try out hosting in the cloud.
Most importantly, my service from forethought.net has become unreliable, and is slow at best.

This file is for notes about using the Amazon Web Services to host tomwhartung.com .

# Goals

- Compare and contrast AWS with GCP
  - Take enough notes that we can write a blog post and develop a presentation for meetups
- Try to stay on the free tier
  - Set up a notification so we know when we are exceeding the limits of the free tier
  - It looks like even if I exceed the free tier, it will not be super-expensive

# References

I have been doing some research, and the process looks reasonable.
If anything, setup is probably easier than hosting it here at home, because each instance is specialized.

## Introductory Information

- AWS free tier landing page: https://aws.amazon.com/free/
- AWS free tier terms: https://aws.amazon.com/free/terms/
- AWS elastic compute cloud (EC2): https://aws.amazon.com/ec2/

## Tutorials

- AWS getting started page with list of tutorials: https://aws.amazon.com/getting-started/
- Getting started with EC2: https://aws.amazon.com/ec2/getting-started/#console
- Links to more tutorials: https://aws.amazon.com/ec2/getting-started/#tutorials
- Install LAMP with Amazon AMI: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-LAMP.html
- Install LAMP on Amazon Linux 2: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-lamp-amazon-linux-2.html
- Getting started with Linux instances: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html
- Remote Management of instances: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/tutorial_run_command.html

## This Looks Like What I Ultimately Want to Do:

- Wordpress Blog on Amazon Linux: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hosting-wordpress.html

## Docs, Certification, and More

- AWS documentation landing page: https://aws.amazon.com/documentation/
- AWS certification landing page: https://aws.amazon.com/certification/
- AWS partners landing page: https://aws.amazon.com/partners/
- Tracking free tier usage: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.html
- Running commands remotely: https://docs.aws.amazon.com/systems-manager/latest/userguide/execute-remote-commands.html
- About Elastic IP Addresses: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html

# Process

Following is the proposed process to use, going forward:

- [X] 1. Research AWS and assess feasibility
- [ ] 2. Try out some very simple, basic, introductory tutorials
- [ ] 3. Do the Wordpress Blog on Amazon Linux tutorial
- [ ] 4. Assess whether we want to do this for tomwhartung.com
- [ ]    4.1 Backup idea: Maybe host tomhartung.com or joomoowebsites.com instead of, or in addition to, tomwhartung.com
- [ ] 5. Proceed, or not, as decided
- [ ] 6. Compare process, free tier, resulting site maintenance required, etc. of AWS to GCP

