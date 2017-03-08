
# Heroku

Finally got some exposure to (and a reason to look at) heroku in the Real Python class.

## References

### "How Heroku Works:"

- https://devcenter.heroku.com/articles/how-heroku-works#defining-an-application

This is meant to be read sequentially.

### "Docker vs. Heroku:"

- https://tuhrig.de/docker-vs-heroku/

His English is a little choppy but it's brief and to the point.

## Terminology

These are really just copied and pasted from the reference - so I have them all in one easily-accessible place.

**So pretty much everything in this file should be "in quotes," but it seems like a silly waste of time to do so.**

### Applications

Applications consist of your source code and a description of any dependencies.

### Procfiles

Procfiles list process types - named commands that you may want executed.

Examples:

```
web: java -jar lib/foobar.jar $PORT
queue: java -jar lib/queue-processor.jar
```

### Applications

Applications consist of your source code, a description of any dependencies, and a Procfile.

### Deployment

Deploying applications involves sending the application to Heroku using either git, GitHub, Dropbox, or via an API.

```
git push **heroku** master
```

### Buildpacks (similar to a Docker Dockerfile)

Buildpacks lie behind the slug compilation process.
Buildpacks take your application, its dependencies, and the language runtime, and produce slugs.
They’re open source - enabling you to extend Heroku to other languages and frameworks.

### Slug (similar to a Docker Image)

A slug is a bundle of your source, fetched dependencies, the language runtime, and
compiled/generated output of the build system - ready for execution.

### Dynos (similar to a Docker container)

Dynos are isolated, virtualized Unix containers, that provide the environment required to run an application.

You can start 5 dynos, 3 for the web and 2 for the queue process types, as follows:

```
heroku ps:scale web=3 queue=2
```

### Dyno Formation

Your application’s dyno formation is the total number of currently-executing dynos,
divided between the various process types you have scaled.

To understand what’s executing, you just need to know what dynos are running which process types:

```
heroku ps
== web: 'java lib/foobar.jar $PORT'
web.1: up 2013/02/07 18:59:17 (~ 13m ago)
web.1: up 2013/02/07 18:52:08 (~ 20m ago)
web.2: up 2013/02/07 18:31:14 (~ 41m ago)

== queue: `java lib/queue-processor.jar`
queue.1: up 2013/02/07 18:40:48 (~ 32m ago)
queue.2: up 2013/02/07 18:40:48 (~ 32m ago)
```

### Config vars

Config vars contain customizable configuration data that can be changed independently of your source code.
The configuration is exposed to a running application via environment variables.

```
heroku config:set ENCRYPTION_KEY=my_secret_launch_codes
Adding config vars and restarting demoapp... done, v14
ENCRYPTION_KEY:     my_secret_launch_codes
```

### Releases (1 of 2)

Releases are an append-only ledger of slugs and config vars.

```
heroku releases
== demoapp Releases
v103 Deploy 582fc95  jon@heroku.com   2013/01/31 12:15:35
v102 Deploy 990d916  jon@heroku.com   2013/01/31 12:01:12
```

The number next to the deploy message, for example 582fc95, corresponds to the commit hash of the repository you deployed to Heroku.

All releases are automatically persisted in an append-only ledger.

#### Rolling Back is easy:

It’s very easy to rollback and deploy a previous release:

```
$ heroku releases:rollback v102
Rolling back demoapp... done, v102
$ heroku releases
== demoapp Releases
v104 Rollback to v102 jon@heroku.com   2013/01/31 14:11:33 (~15s ago)
v103 Deploy 582fc95   jon@heroku.com   2013/01/31 12:15:35
v102 Deploy 990d916   jon@heroku.com   2013/01/31 12:01:12
```

### Dyno Manager

The dyno manager of the Heroku platform is responsible for managing dynos across all applications running on Heroku.

Dynos are cycled at least once per day, or whenever the dyno manager detects a fault in the running application
(such as out of memory exceptions)....

This dyno cycling happens transparently and automatically on a regular basis, and is logged.

#### Free dyno type details

Applications that use the free dyno type will sleep.
When a sleeping application receives HTTP traffic, it will be awakened - causing a delay of a few seconds.
Using one of the other dyno types will avoid sleeping.

### One-off dynos

One-off Dynos are temporary dynos that can run with their input/output attached to your local terminal.
They’re loaded with your latest release.

Because Heroku manages and runs applications, there’s no need to manage operating systems or other internal system configuration.
One-off dynos can be run with their input/output attached to your local terminal.
These can also be used to carry out admin tasks that modify the state of shared resources,
for example database configuration - perhaps periodically through a scheduler.

```
heroku run bash
Running `bash` attached to terminal... up, run.8963
~ $ ls
```

This will spin up a new dyno, loaded with your release, and then run the bash command....

### Ephemeral filesystem

Each dyno gets its own ephemeral filesystem - with a fresh copy of the most recent release.
It can be used as temporary scratchpad, but changes to the filesystem are not reflected to other dynos.

**If you create a one-off dyno by running heroku run bash, the Unix shell on the dyno,
and then create a file on that dyno, and then terminate your session - the change is lost.**

### Add-ons

Add-ons are third party, specialized, value-added cloud services that can be easily attached to an application,
extending its functionality.

```
heroku addons:create heroku-redis:hobby-dev
```

Applications typically make use of add-ons to provide backing services such as
databases, queueing & caching systems, storage, email services and more.
Add-ons are provided as services by Heroku and third parties - there’s a large marketplace of add-ons you can choose from.

### Releases (2 of 2)

Releases are an append-only ledger of slugs, config vars and **add-ons.**
Heroku maintains an append-only ledger of releases you make.

### Logplex

Logplex automatically collates log entries from all the running dynos of your app,
as well as other components such as the routers, providing a single source of activity.

```
heroku logs
2013-02-11T15:19:10+00:00 heroku[router]: at=info method=GET path=/articles/custom-domains host=mydemoapp.heroku.com fwd=74.58.173.188 dyno=web.1 queue=0 wait=0ms connect=0ms service=1452ms status=200 bytes=5783
2013-02-11T15:19:10+00:00 app[web.2]: Started GET "/" for 1.169.38.175 at 2013-02-11 15:19:10 +0000
2013-02-11T15:19:10+00:00 app[web.1]: Started GET "/" for 2.161.132.15 at 2013-02-11 15:20:10 +0000
```

Tailing logs:

```
heroku logs --ps web.1 --tail
2013-02-11T15:19:10+00:00 app[web.2]: Started GET "/" for 1.169.38.175 at 2013-02-11 15:19:10 +0000
```

### HTTP routing (scaling)

Scaling an app’s capacity to handle web traffic involves scaling the number of web dynos:

```
heroku ps:scale web+5
```

### 

## Commands

#### Check the installed version:

```
heroku --version    ## heroku-cli/5.6.29-ac5c0de (linux-amd64) go1.7.5
```

#### See what's running:

```
heroku ps:scale web=3 queue=2
heroku ps
```

#### Tailing logs:

```
heroku logs --ps web.1 --tail
```

#### Set a config variable:

```
heroku config:set ENCRYPTION_KEY=my_secret_launch_codes
```

#### Create and attach to a one-off dyno:

```
heroku run bash
```

#### List releases and rollback to a previous one:

```
heroku releases
heroku releases:rollback v102
```

```
```

```

